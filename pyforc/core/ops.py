"""Transformations which operate on ForcData objects."""
from typing import Any, List, Union

import numpy as np
import scipy.interpolate as si
import scipy.ndimage as sn
import scipy.optimize as so

from .config import Config
from .ingester import ForcData


def interpolate(
    data: ForcData,
    config: Config,
) -> ForcData:
    """Interpolate the raw dataset.

    m and t values for h < hr are set to np.nan.

    Parameters
    ----------
    step : float
        Step size along the h and hr directions to use for the interpolated dataset. Uses the
        same units given by the raw data. If None, the step will be determined from the median
        of the steps in the h-direction.
    interpolation : str
        Interpolation method to use; see docstring for scipy.interpolate.griddata for valid
        interpolation methods.

    Returns
    -------
    ForcData
        Interpolated dataset
    """
    if not config.step:
        step = data.get_step()
    else:
        step = config.step

    h_vals = np.concatenate(data.h_raw)
    hr_vals = np.concatenate(hr_vals_from_h(data.h_raw))
    m_vals = np.concatenate(data.m_raw)
    t_vals = np.concatenate(data.t_raw)

    h_min = np.min(h_vals)
    h_max = np.max(h_vals)
    hr_min = np.min(hr_vals)
    hr_max = np.max(hr_vals)

    h, hr = np.meshgrid(
        np.linspace(h_min, h_max, int((h_max - h_min) // step) + 1),
        np.linspace(hr_min, hr_max, int((hr_max - hr_min) // step) + 1),
    )

    hhr_vals = np.concatenate(
        (np.reshape(h_vals, (-1, 1)), np.reshape(hr_vals, (-1, 1))),
        axis=1
    ),

    m = si.griddata(hhr_vals, m_vals, (h, hr), method=config.interpolation)

    # Mask off the portion of the interpolated data that wasn't measured
    m[h < hr] = np.nan

    # If any temperature values are present in the raw data, interpolate over them; otherwise
    # all temperatures will be np.nan.
    if np.isnan(t_vals).any():
        t = np.full_like(m, fill_value=np.nan)
    else:
        t = si.griddata(hhr_vals, t_vals, (h, hr), method=config.interpolation)
        t[h < hr] = np.nan

    return ForcData.from_existing(
        data=data,
        h=h,
        hr=hr,
        m=m,
        t=t,
    )


def correct_drift(data: ForcData, config: Config) -> ForcData:
    """Correct the raw magnetization for drift.

    If the measurement space is Hc/Hb, dedicated drift points must have been measured. If the
    measurement is H/Hr, the last datapoint along each curve is used. In either case, the points
    used for drift correction must have been measured above the saturation field.

    Drift correction is carried out in the following steps:

        1. Calculate the average saturation magnetization, m_sat_avg
        2. Calculate a moving average of the saturation magnetization, m_sat_mov
        3. Use a cubic spline to interpolate between every nth point, m_sat_interp
        4. Subtract out the difference (m_sat_avg - m_sat_interp) from the magnetization of each
        curve

    Parameters
    ----------
    data : ForcData
        Data for which drift correction is to be applied
    config: Config
        Configuration containing a `drift_kernel_size` entry.

    Returns
    -------
    ForcData
        Drift-corrected raw data; interpolated dataset is untouched.
    """
    if len(data.m_drift) == 0:
        raise ValueError("No drift points in dataset.")

    m_sat_avg = np.mean(data.m_drift)

    m_sat_mov = decimate(
        moving_average(data.m_drift, config.drift_kernel_size),
        config.drift_density
    )
    index_mov = decimate(
        np.arange(0, len(data.m_drift)),
        config.drift_density
    )

    m_sat_interp = si.interp1d(index_mov, m_sat_mov, kind='cubic')

    m_raw = []
    for i, curve in enumerate(data.m_raw):
        m_raw.append(curve - (m_sat_interp(i) - m_sat_avg))
    return ForcData.from_existing(data=data, m_raw=m_raw)


def decimate(x: Union[List[Any], np.ndarray], step: int) -> np.ndarray:
    """Return every `step` value of x, but without removing the last value in x.

    The step slicing operator [::step] always returns the first element in the array, and then
    subsequent value which are separated by `step` indices. Therefore the last element in the array
    is included by the slice operation if `(len(x) - 1) % step == 0`; otherwise the last element
    needs to be appended.

    Parameters
    ----------
    x : Union[list[Any], np.ndarray]
        List or array to be decimated
    step : int
        Only return the first element of the array, and every `step`th element after that (but then
        also return the last element in the array, if it was going to be skipped).

    Returns
    -------
    np.ndarray:
        Decimated array, with the first and last values included from `x`.
    """
    x_dec = np.array(x)[::step]
    if (len(x) - 1) % step != 0:
        x_dec = np.append(x_dec, x[-1])
    return x_dec


def moving_average(data: np.ndarray, kernel_size: int):
    """Calculate a moving average over the data.

    Parameters
    ----------
    data : np.ndarray
        Data for which the moving average is to be calculated.
    kernel_size : int
        The size of the moving average window is (2*kernel_size + 1)
    """
    window_size = 2 * kernel_size + 1
    return sn.convolve(
        data,
        np.ones(window_size) / window_size,
        mode='nearest',
    )


def hr_vals_from_h(h: list[np.ndarray]) -> list[np.ndarray]:
    """Generate an hr dataset from a ragged set of h curves.

    Parameters
    ----------
    h: list[np.ndarray]
        Ragged list of h-values for each reversal curve

    Returns
    -------
    list[np.ndarray]
        Ragged list of hr-values for each reversal curve. Each datapoint has an hr-value equal to
        the h-value of the first datapoint in the curve.
    """
    return [np.full_like(curve, fill_value=curve[0]) for curve in h]


def normalize(data: ForcData, _) -> ForcData:
    """Normalize the magnetization to the range [-1, 1].

    Parameters
    ----------
    data : ForcData
        Data to normalize.

    Returns
    -------
    ForcData
        Normalized FORC data.
    """
    return ForcData.from_existing(
        data=data,
        m=1 - 2 * (data.m - np.nanmax(data.m)) / (np.nanmax(data.m) - np.nanmin(data.m))
    )


def correct_slope(data: ForcData, config: Config) -> ForcData:
    """Remove contributions to the magnetization which are linear in the field.

    This subtracts out para-/dia-magnetic background which is rarely of interest in magnetic
    systems.

    The fitting region is the region for which

        1. |h| > h_sat (the magnetic material is saturated)
        2. m is not NaN (ignore any NaNs introduced from interpolation)
        3. h > hr (ignore the unmeasurable region where Hc < 0)

    Parameters
    ----------
    data : ForcData
        Data for which the slope is to be corrected.
    config : Config
        Configuration containg the saturation magnetization `h_sat`, beyond which the slope is
        constant.

    Returns
    -------
    ForcData
        Data with the background subtracted out.
    """
    fit_region = (np.abs(data.h) > config.h_sat) & (~np.isnan(data.m)) & (data.h >= data.hr)

    h = data.h[fit_region].flatten()
    m = data.m[fit_region].flatten()

    (a, b), _ = so.curve_fit(line, h, m)

    return ForcData.from_existing(
        data=data,
        m=data.m - line(data.h, a, 0)
    )


def line(x: np.ndarray, a: float, b: float) -> np.ndarray:
    """Return y-values which are a linear function of x.

    Parameters
    ----------
    x : np.ndarray
        Abcissa
    a : float
        Slope of the line
    b : float
        y-intercept of the line

    Returns
    -------
    np.ndarray
        Ordinate
    """
    return a * x + b


def compute_forc_distribution(data: ForcData, config: Config) -> ForcData:
    """Compute the FORC distribution.

    This method uses a Savitzky-Golay filter to calculate the mixed partial derivative:

        ρ = -(1/2)∂²M/∂H∂Hr

    This is a convolution-based method for calculating the mixed partial derivative;
    Heslop and Muxworthy (2005) [DOI: 10.1016/j.jmmm.2004.09.002] were the first to propose using
    this method. Mathematically speaking it is equivalent to the least-squares fitting procedure
    originally used by Pike et. al. (1999) [DOI: 10.1063/1.370176], but it's orders of magnitude
    faster.

    Parameters
    ----------
    data : ForcData
        Data for which the FORC distribution is to be calculated.
    config : Config
        Configuration containing the smoothing factor.

    Returns
    -------
    ForcData
        Data with the computed FORC distribution.
    """
    step = data.get_step()
    return -0.5 * sn.convolve(
        input=data.m,
        weights=compute_sg_kernel(config.smoothing_factor, step, step),
        mode='constant',
        cval=np.nan,
    )


def compute_sg_kernel(sf: int, step_x: float, step_y: float) -> np.ndarray:
    """
    Compute the Savitzky-Golay kernel which pulls out the mixed second derivative.

    Parameters
    ----------
    sf : int
        Smoothing factor to use for the filter
    step_x : float
        Step size in the x-direction
    step_y : float
        Step size in the y-direction

    Returns
    -------
    np.ndarray:
        Kernel which, when colvolved with the data, will yield the coefficient of the "xy" term in
        the least-squares fit of the data in the neighborhood of each point.
    """
    xx, yy = np.meshgrid(
        np.linspace(sf * step_x, -sf * step_x, 2 * sf + 1),
        np.linspace(sf * step_y, -sf * step_y, 2 * sf + 1)
    )

    xx = np.reshape(xx, (-1, 1))
    yy = np.reshape(yy, (-1, 1))

    coefficients = np.linalg.pinv(np.hstack((np.ones_like(xx), xx, xx ** 2, yy, yy ** 2, xx * yy)))

    return np.reshape(coefficients[5, :], (2 * sf + 1, 2 * sf + 1))
