"""Plotting utilities for the FORC data."""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import axes
from matplotlib.collections import LineCollection
from mpl_toolkits.axes_grid1 import make_axes_locatable

from . import coordinates, forc


def imshow(
    fc: forc.Forc,
    interpolation: str = 'nearest',
    ax: axes.Axes = None,
    coords: str = 'hhr',
    mask: bool = True,
) -> axes.Axes:
    """Show the FORC data as a colormap.

    Parameters
    ----------
    fc : forc.Forc
        Forc instance to be plotted
    interpolation : str
        Interpolation to use.
    ax : axes.Axes
        Axes on which the image is to be drawn
    coords : str | coordinates.Coordinates
        Coordinates in which the data is to be drawn
    mask : bool
        If True, data for which H < Hr will be included in the calculation of the extent

    Returns
    -------
    axes.Axes
        Axes on which the image is drawn
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(20, 10))
    else:
        fig = ax.figure
    ax.set_aspect('equal')

    if isinstance(coords, coordinates.Coordinates):
        transform = coords
    else:
        transform = coordinates.Coordinates.from_str(coords)

    im = ax.imshow(
        fc.data.m,
        interpolation=interpolation,
        origin='lower',
        extent=fc.data.get_extent(mask),
        transform=transform + ax.transData
    )
    cax = make_axes_locatable(ax).append_axes("right", size="5%", pad=0.05)
    fig.colorbar(im, cax=cax)

    xlim, ylim = fc.data.get_limits(coords=transform, mask=mask)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    return ax


def curves(fc: forc.Forc, ax: axes.Axes = None) -> axes.Axes:
    """Plot the reversal curves in H-M space.

    Parameters
    ----------
    fc : forc.Forc
        Forc instance to be plotted
    ax : axes.Axes
        Axes on which the data is to be plotted

    Returns
    -------
    axes.Axes
        Axes on which the image is drawn
    """
    if ax is None:
        _, ax = plt.subplots(1, 1, figsize=(20, 10))

    ax.add_collection(
        LineCollection(
            fc.data.curves(),
            linestyles='solid',
            color='w',
            alpha=0.3,
        )
    )
    ax.set_xlim(np.nanmin(fc.data.h), np.nanmax(fc.data.h))
    ax.set_ylim(np.nanmin(fc.data.m), np.nanmax(fc.data.m))
    return ax