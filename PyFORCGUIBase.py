# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\PyFORCGUIBase.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 909)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtWidgets.QSpacerItem(609, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 1, 2, 1, 1)
        self.b_undo = QtWidgets.QPushButton(self.centralwidget)
        self.b_undo.setObjectName("b_undo")
        self.gridLayout_5.addWidget(self.b_undo, 1, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.b_import = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_import.setFont(font)
        self.b_import.setObjectName("b_import")
        self.verticalLayout_2.addWidget(self.b_import)
        self.b_slope = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_slope.setFont(font)
        self.b_slope.setObjectName("b_slope")
        self.verticalLayout_2.addWidget(self.b_slope)
        self.b_normalize = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_normalize.setFont(font)
        self.b_normalize.setObjectName("b_normalize")
        self.verticalLayout_2.addWidget(self.b_normalize)
        self.b_offset = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_offset.setFont(font)
        self.b_offset.setObjectName("b_offset")
        self.verticalLayout_2.addWidget(self.b_offset)
        self.b_gauss = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_gauss.setFont(font)
        self.b_gauss.setObjectName("b_gauss")
        self.verticalLayout_2.addWidget(self.b_gauss)
        self.b_forc = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_forc.setFont(font)
        self.b_forc.setObjectName("b_forc")
        self.verticalLayout_2.addWidget(self.b_forc)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.b_paths = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_paths.setFont(font)
        self.b_paths.setObjectName("b_paths")
        self.gridLayout_3.addWidget(self.b_paths, 0, 0, 1, 1)
        self.b_major_loop = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_major_loop.setFont(font)
        self.b_major_loop.setObjectName("b_major_loop")
        self.gridLayout_3.addWidget(self.b_major_loop, 0, 1, 1, 1)
        self.b_contours = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_contours.setFont(font)
        self.b_contours.setObjectName("b_contours")
        self.gridLayout_3.addWidget(self.b_contours, 1, 1, 1, 1)
        self.b_hc_axis = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_hc_axis.setFont(font)
        self.b_hc_axis.setObjectName("b_hc_axis")
        self.gridLayout_3.addWidget(self.b_hc_axis, 2, 0, 1, 1)
        self.b_hb_axis = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_hb_axis.setFont(font)
        self.b_hb_axis.setObjectName("b_hb_axis")
        self.gridLayout_3.addWidget(self.b_hb_axis, 2, 1, 1, 1)
        self.b_h_axis = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_h_axis.setFont(font)
        self.b_h_axis.setObjectName("b_h_axis")
        self.gridLayout_3.addWidget(self.b_h_axis, 3, 0, 1, 1)
        self.b_hr_axis = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_hr_axis.setFont(font)
        self.b_hr_axis.setObjectName("b_hr_axis")
        self.gridLayout_3.addWidget(self.b_hr_axis, 3, 1, 1, 1)
        self.b_data_points = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_data_points.setFont(font)
        self.b_data_points.setObjectName("b_data_points")
        self.gridLayout_3.addWidget(self.b_data_points, 1, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_6.setFlat(True)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.b_contour_moment = QtWidgets.QPushButton(self.groupBox_6)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_contour_moment.setFont(font)
        self.b_contour_moment.setObjectName("b_contour_moment")
        self.verticalLayout_3.addWidget(self.b_contour_moment)
        self.b_contour_rho = QtWidgets.QPushButton(self.groupBox_6)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_contour_rho.setFont(font)
        self.b_contour_rho.setObjectName("b_contour_rho")
        self.verticalLayout_3.addWidget(self.b_contour_rho)
        self.b_contour_rho_uncertainty = QtWidgets.QPushButton(self.groupBox_6)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_contour_rho_uncertainty.setFont(font)
        self.b_contour_rho_uncertainty.setObjectName("b_contour_rho_uncertainty")
        self.verticalLayout_3.addWidget(self.b_contour_rho_uncertainty)
        self.b_contour_temperature = QtWidgets.QPushButton(self.groupBox_6)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_contour_temperature.setFont(font)
        self.b_contour_temperature.setObjectName("b_contour_temperature")
        self.verticalLayout_3.addWidget(self.b_contour_temperature)
        self.gridLayout_3.addWidget(self.groupBox_6, 4, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.b_heat_moment = QtWidgets.QPushButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_heat_moment.setFont(font)
        self.b_heat_moment.setObjectName("b_heat_moment")
        self.verticalLayout_4.addWidget(self.b_heat_moment)
        self.b_heat_rho = QtWidgets.QPushButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_heat_rho.setFont(font)
        self.b_heat_rho.setObjectName("b_heat_rho")
        self.verticalLayout_4.addWidget(self.b_heat_rho)
        self.b_heat_rho_uncertainty = QtWidgets.QPushButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_heat_rho_uncertainty.setFont(font)
        self.b_heat_rho_uncertainty.setObjectName("b_heat_rho_uncertainty")
        self.verticalLayout_4.addWidget(self.b_heat_rho_uncertainty)
        self.b_heat_temperature = QtWidgets.QPushButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_heat_temperature.setFont(font)
        self.b_heat_temperature.setObjectName("b_heat_temperature")
        self.verticalLayout_4.addWidget(self.b_heat_temperature)
        self.gridLayout_3.addWidget(self.groupBox_5, 4, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_7.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_7.setFlat(True)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.b_map_curves_moment = QtWidgets.QPushButton(self.groupBox_7)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_map_curves_moment.setFont(font)
        self.b_map_curves_moment.setObjectName("b_map_curves_moment")
        self.verticalLayout_5.addWidget(self.b_map_curves_moment)
        self.b_map_curves_rho = QtWidgets.QPushButton(self.groupBox_7)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_map_curves_rho.setFont(font)
        self.b_map_curves_rho.setObjectName("b_map_curves_rho")
        self.verticalLayout_5.addWidget(self.b_map_curves_rho)
        self.b_map_curves_rho_uncertainty = QtWidgets.QPushButton(self.groupBox_7)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_map_curves_rho_uncertainty.setFont(font)
        self.b_map_curves_rho_uncertainty.setObjectName("b_map_curves_rho_uncertainty")
        self.verticalLayout_5.addWidget(self.b_map_curves_rho_uncertainty)
        self.b_map_curves_temperature = QtWidgets.QPushButton(self.groupBox_7)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_map_curves_temperature.setFont(font)
        self.b_map_curves_temperature.setObjectName("b_map_curves_temperature")
        self.verticalLayout_5.addWidget(self.b_map_curves_temperature)
        self.gridLayout_3.addWidget(self.groupBox_7, 5, 0, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox_4, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 2, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 3, 2, 1)
        self.t_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.t_tabs.setDocumentMode(True)
        self.t_tabs.setTabsClosable(False)
        self.t_tabs.setTabBarAutoHide(False)
        self.t_tabs.setObjectName("t_tabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_9.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_9.setFlat(True)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.f_drift = QtWidgets.QCheckBox(self.groupBox_9)
        self.f_drift.setChecked(True)
        self.f_drift.setObjectName("f_drift")
        self.gridLayout_7.addWidget(self.f_drift, 0, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.groupBox_9)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_9)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_9)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_9)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 4, 0, 1, 1)
        self.f_step_auto = QtWidgets.QCheckBox(self.groupBox_9)
        self.f_step_auto.setChecked(True)
        self.f_step_auto.setObjectName("f_step_auto")
        self.gridLayout_7.addWidget(self.f_step_auto, 4, 1, 1, 2)
        self.f_step_manual = QtWidgets.QLineEdit(self.groupBox_9)
        self.f_step_manual.setEnabled(False)
        self.f_step_manual.setObjectName("f_step_manual")
        self.gridLayout_7.addWidget(self.f_step_manual, 4, 3, 1, 1)
        self.f_dataset_interpolation_type = QtWidgets.QComboBox(self.groupBox_9)
        self.f_dataset_interpolation_type.setObjectName("f_dataset_interpolation_type")
        self.f_dataset_interpolation_type.addItem("")
        self.f_dataset_interpolation_type.addItem("")
        self.f_dataset_interpolation_type.addItem("")
        self.gridLayout_7.addWidget(self.f_dataset_interpolation_type, 3, 3, 1, 1)
        self.f_drift_radius = QtWidgets.QSpinBox(self.groupBox_9)
        self.f_drift_radius.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.f_drift_radius.setMaximum(999999999)
        self.f_drift_radius.setProperty("value", 4)
        self.f_drift_radius.setObjectName("f_drift_radius")
        self.gridLayout_7.addWidget(self.f_drift_radius, 2, 3, 1, 1)
        self.f_drift_density = QtWidgets.QSpinBox(self.groupBox_9)
        self.f_drift_density.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.f_drift_density.setMaximum(999999999)
        self.f_drift_density.setProperty("value", 3)
        self.f_drift_density.setObjectName("f_drift_density")
        self.gridLayout_7.addWidget(self.f_drift_density, 1, 3, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_9, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(331, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem2, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.f_slope_curve_to_fit = QtWidgets.QSpinBox(self.groupBox)
        self.f_slope_curve_to_fit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.f_slope_curve_to_fit.setMaximum(999999999)
        self.f_slope_curve_to_fit.setObjectName("f_slope_curve_to_fit")
        self.gridLayout.addWidget(self.f_slope_curve_to_fit, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 2)
        self.f_auto_slope = QtWidgets.QCheckBox(self.groupBox)
        self.f_auto_slope.setChecked(True)
        self.f_auto_slope.setObjectName("f_auto_slope")
        self.gridLayout.addWidget(self.f_auto_slope, 2, 0, 1, 1)
        self.f_slope = QtWidgets.QLineEdit(self.groupBox)
        self.f_slope.setEnabled(False)
        self.f_slope.setObjectName("f_slope")
        self.gridLayout.addWidget(self.f_slope, 2, 2, 1, 1)
        self.f_slope_h_sat = QtWidgets.QLineEdit(self.groupBox)
        self.f_slope_h_sat.setObjectName("f_slope_h_sat")
        self.gridLayout.addWidget(self.f_slope_h_sat, 1, 2, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.f_smoothing_factor = QtWidgets.QSpinBox(self.groupBox_2)
        self.f_smoothing_factor.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.f_smoothing_factor.setAccelerated(False)
        self.f_smoothing_factor.setMinimum(0)
        self.f_smoothing_factor.setMaximum(999999999)
        self.f_smoothing_factor.setProperty("value", 3)
        self.f_smoothing_factor.setObjectName("f_smoothing_factor")
        self.gridLayout_2.addWidget(self.f_smoothing_factor, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.f_extension_type = QtWidgets.QComboBox(self.groupBox_2)
        self.f_extension_type.setObjectName("f_extension_type")
        self.f_extension_type.addItem("")
        self.f_extension_type.addItem("")
        self.f_extension_type.addItem("")
        self.gridLayout_2.addWidget(self.f_extension_type, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setEnabled(False)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.f_extension_n_fit_points = QtWidgets.QSpinBox(self.groupBox_2)
        self.f_extension_n_fit_points.setEnabled(False)
        self.f_extension_n_fit_points.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.f_extension_n_fit_points.setMinimum(10)
        self.f_extension_n_fit_points.setMaximum(999999999)
        self.f_extension_n_fit_points.setObjectName("f_extension_n_fit_points")
        self.gridLayout_2.addWidget(self.f_extension_n_fit_points, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 397, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem3, 3, 0, 1, 1)
        self.t_tabs.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_11.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_11.setFlat(True)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_14 = QtWidgets.QLabel(self.groupBox_11)
        self.label_14.setObjectName("label_14")
        self.gridLayout_10.addWidget(self.label_14, 0, 0, 1, 1)
        self.f_2d_mask = QtWidgets.QComboBox(self.groupBox_11)
        self.f_2d_mask.setObjectName("f_2d_mask")
        self.f_2d_mask.addItem("")
        self.f_2d_mask.addItem("")
        self.f_2d_mask.addItem("")
        self.gridLayout_10.addWidget(self.f_2d_mask, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_11)
        self.label_16.setObjectName("label_16")
        self.gridLayout_10.addWidget(self.label_16, 1, 0, 1, 1)
        self.f_2d_cmap = QtWidgets.QLineEdit(self.groupBox_11)
        self.f_2d_cmap.setObjectName("f_2d_cmap")
        self.gridLayout_10.addWidget(self.f_2d_cmap, 1, 1, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_11, 0, 0, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_10.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_10.setFlat(True)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_15 = QtWidgets.QLabel(self.groupBox_10)
        self.label_15.setObjectName("label_15")
        self.gridLayout_9.addWidget(self.label_15, 0, 0, 1, 2)
        self.f_paths_mask = QtWidgets.QComboBox(self.groupBox_10)
        self.f_paths_mask.setObjectName("f_paths_mask")
        self.f_paths_mask.addItem("")
        self.f_paths_mask.addItem("")
        self.f_paths_mask.addItem("")
        self.gridLayout_9.addWidget(self.f_paths_mask, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_10)
        self.label_13.setObjectName("label_13")
        self.gridLayout_9.addWidget(self.label_13, 1, 0, 1, 1)
        self.f_paths_cmap = QtWidgets.QComboBox(self.groupBox_10)
        self.f_paths_cmap.setObjectName("f_paths_cmap")
        self.f_paths_cmap.addItem("")
        self.gridLayout_9.addWidget(self.f_paths_cmap, 1, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_10)
        self.label_12.setObjectName("label_12")
        self.gridLayout_9.addWidget(self.label_12, 2, 0, 1, 1)
        self.f_paths_points = QtWidgets.QComboBox(self.groupBox_10)
        self.f_paths_points.setObjectName("f_paths_points")
        self.f_paths_points.addItem("")
        self.f_paths_points.addItem("")
        self.f_paths_points.addItem("")
        self.gridLayout_9.addWidget(self.f_paths_points, 2, 2, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_10, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 585, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem4, 2, 0, 1, 1)
        self.t_tabs.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_8.setFlat(True)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_8)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_6.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_8)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_6.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_8)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.gridLayout_6.addWidget(self.groupBox_8, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(571, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem5, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 659, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem6, 1, 0, 1, 1)
        self.t_tabs.addTab(self.tab_3, "")
        self.gridLayout_5.addWidget(self.t_tabs, 0, 1, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.d_jobs = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d_jobs.sizePolicy().hasHeightForWidth())
        self.d_jobs.setSizePolicy(sizePolicy)
        self.d_jobs.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.d_jobs.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.d_jobs.setObjectName("d_jobs")
        self.verticalLayout.addWidget(self.d_jobs)
        self.d_progress = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d_progress.sizePolicy().hasHeightForWidth())
        self.d_progress.setSizePolicy(sizePolicy)
        self.d_progress.setProperty("value", 100)
        self.d_progress.setTextVisible(False)
        self.d_progress.setObjectName("d_progress")
        self.verticalLayout.addWidget(self.d_progress)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.d_status = QtWidgets.QStatusBar(MainWindow)
        self.d_status.setObjectName("d_status")
        MainWindow.setStatusBar(self.d_status)
        self.a_load = QtWidgets.QAction(MainWindow)
        self.a_load.setObjectName("a_load")
        self.actionAdvanced_Settings = QtWidgets.QAction(MainWindow)
        self.actionAdvanced_Settings.setObjectName("actionAdvanced_Settings")
        self.menubar.addAction(self.menuFile.menuAction())
        self.label_7.setBuddy(self.f_drift_density)
        self.label_8.setBuddy(self.f_drift_radius)
        self.label_9.setBuddy(self.f_dataset_interpolation_type)
        self.label_3.setBuddy(self.f_slope_curve_to_fit)

        self.retranslateUi(MainWindow)
        self.t_tabs.setCurrentIndex(0)
        self.f_auto_slope.clicked['bool'].connect(self.f_slope.setDisabled)
        self.f_step_auto.clicked['bool'].connect(self.f_step_manual.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b_undo.setText(_translate("MainWindow", "Undo"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Processing"))
        self.b_import.setText(_translate("MainWindow", "Import Data"))
        self.b_slope.setText(_translate("MainWindow", "Slope Correction"))
        self.b_normalize.setText(_translate("MainWindow", "Normalize Moment"))
        self.b_offset.setText(_translate("MainWindow", "Offset Correction"))
        self.b_gauss.setText(_translate("MainWindow", "Gaussian Filter"))
        self.b_forc.setText(_translate("MainWindow", "FORC Distribution"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Plotting"))
        self.b_paths.setText(_translate("MainWindow", "Paths"))
        self.b_major_loop.setText(_translate("MainWindow", "Major Loop"))
        self.b_contours.setText(_translate("MainWindow", "Contour Lines"))
        self.b_hc_axis.setText(_translate("MainWindow", "Hc Axis"))
        self.b_hb_axis.setText(_translate("MainWindow", "Hb Axis"))
        self.b_h_axis.setText(_translate("MainWindow", "H Axis"))
        self.b_hr_axis.setText(_translate("MainWindow", "Hr Axis"))
        self.b_data_points.setText(_translate("MainWindow", "Data Points"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Contour Diagram"))
        self.b_contour_moment.setText(_translate("MainWindow", "Moment"))
        self.b_contour_rho.setText(_translate("MainWindow", "FORC Distribution"))
        self.b_contour_rho_uncertainty.setText(_translate("MainWindow", "FORC Uncertainty"))
        self.b_contour_temperature.setText(_translate("MainWindow", "Temperature"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Heat Map"))
        self.b_heat_moment.setText(_translate("MainWindow", "Moment"))
        self.b_heat_rho.setText(_translate("MainWindow", "FORC Distribution"))
        self.b_heat_rho_uncertainty.setText(_translate("MainWindow", "FORC Uncertainty"))
        self.b_heat_temperature.setText(_translate("MainWindow", "Temperature"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Map into Reversal Curves"))
        self.b_map_curves_moment.setText(_translate("MainWindow", "Moment"))
        self.b_map_curves_rho.setText(_translate("MainWindow", "FORC Distribution"))
        self.b_map_curves_rho_uncertainty.setText(_translate("MainWindow", "FORC Uncertainty"))
        self.b_map_curves_temperature.setText(_translate("MainWindow", "Temperature"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Import"))
        self.f_drift.setText(_translate("MainWindow", "Drift Correction"))
        self.label_7.setText(_translate("MainWindow", "Density:"))
        self.label_8.setText(_translate("MainWindow", "Kernel size:"))
        self.label_9.setText(_translate("MainWindow", "Interpolation:"))
        self.label_10.setText(_translate("MainWindow", "Fieldstep:"))
        self.f_step_auto.setText(_translate("MainWindow", "Auto"))
        self.f_step_manual.setPlaceholderText(_translate("MainWindow", "Enter step manually..."))
        self.f_dataset_interpolation_type.setItemText(0, _translate("MainWindow", "nearest"))
        self.f_dataset_interpolation_type.setItemText(1, _translate("MainWindow", "cubic"))
        self.f_dataset_interpolation_type.setItemText(2, _translate("MainWindow", "linear"))
        self.groupBox.setTitle(_translate("MainWindow", "Slope Correction"))
        self.label_3.setText(_translate("MainWindow", "Curve to fit:"))
        self.label_4.setText(_translate("MainWindow", "Hsat:"))
        self.f_auto_slope.setText(_translate("MainWindow", "Auto"))
        self.f_slope.setPlaceholderText(_translate("MainWindow", "Enter slope manually..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "FORC Distribution"))
        self.label_2.setText(_translate("MainWindow", "Extension:"))
        self.f_extension_type.setItemText(0, _translate("MainWindow", "flat"))
        self.f_extension_type.setItemText(1, _translate("MainWindow", "slope"))
        self.f_extension_type.setItemText(2, _translate("MainWindow", "truncate"))
        self.label_6.setText(_translate("MainWindow", "Fit points:"))
        self.label_5.setText(_translate("MainWindow", "Smoothing Factor:"))
        self.t_tabs.setTabText(self.t_tabs.indexOf(self.tab), _translate("MainWindow", "Settings"))
        self.groupBox_11.setTitle(_translate("MainWindow", "2D Plot Options"))
        self.label_14.setText(_translate("MainWindow", "Mask:"))
        self.f_2d_mask.setItemText(0, _translate("MainWindow", "H<Hr"))
        self.f_2d_mask.setItemText(1, _translate("MainWindow", "none"))
        self.f_2d_mask.setItemText(2, _translate("MainWindow", "outline"))
        self.label_16.setText(_translate("MainWindow", "Colormap:"))
        self.f_2d_cmap.setText(_translate("MainWindow", "RdBu_r"))
        self.groupBox_10.setTitle(_translate("MainWindow", "FORC Paths"))
        self.label_15.setText(_translate("MainWindow", "Mask:"))
        self.f_paths_mask.setItemText(0, _translate("MainWindow", "H<Hr"))
        self.f_paths_mask.setItemText(1, _translate("MainWindow", "none"))
        self.f_paths_mask.setItemText(2, _translate("MainWindow", "outline"))
        self.label_13.setText(_translate("MainWindow", "Colormap:"))
        self.f_paths_cmap.setItemText(0, _translate("MainWindow", "viridis"))
        self.label_12.setText(_translate("MainWindow", "Points:"))
        self.f_paths_points.setItemText(0, _translate("MainWindow", "none"))
        self.f_paths_points.setItemText(1, _translate("MainWindow", "reversal"))
        self.f_paths_points.setItemText(2, _translate("MainWindow", "all"))
        self.t_tabs.setTabText(self.t_tabs.indexOf(self.tab_2), _translate("MainWindow", "Plotting"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Export"))
        self.pushButton.setText(_translate("MainWindow", "VTK"))
        self.pushButton_2.setText(_translate("MainWindow", "XYZ"))
        self.pushButton_3.setText(_translate("MainWindow", "PMC Format"))
        self.t_tabs.setTabText(self.t_tabs.indexOf(self.tab_3), _translate("MainWindow", "Output"))
        self.label.setText(_translate("MainWindow", "Log"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.a_load.setText(_translate("MainWindow", "Load..."))
        self.actionAdvanced_Settings.setText(_translate("MainWindow", "Advanced Settings"))

