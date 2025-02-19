# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colorscale_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ColorScaleDialog(object):
    def setupUi(self, ColorScaleDialog):
        ColorScaleDialog.setObjectName("ColorScaleDialog")
        ColorScaleDialog.setWindowModality(QtCore.Qt.NonModal)
        ColorScaleDialog.resize(300, 211)
        ColorScaleDialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(ColorScaleDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(ColorScaleDialog)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.sb_max_percentile = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.sb_max_percentile.setDecimals(0)
        self.sb_max_percentile.setMaximum(100.0)
        self.sb_max_percentile.setSingleStep(1.0)
        self.sb_max_percentile.setProperty("value", 100.0)
        self.sb_max_percentile.setObjectName("sb_max_percentile")
        self.gridLayout_2.addWidget(self.sb_max_percentile, 2, 1, 1, 1)
        self.sb_max_tick = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.sb_max_tick.setMaximum(999999.0)
        self.sb_max_tick.setObjectName("sb_max_tick")
        self.gridLayout_2.addWidget(self.sb_max_tick, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.sb_min_tick = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.sb_min_tick.setMaximum(999999.0)
        self.sb_min_tick.setObjectName("sb_min_tick")
        self.gridLayout_2.addWidget(self.sb_min_tick, 1, 2, 1, 1)
        self.sb_min_percentile = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.sb_min_percentile.setDecimals(0)
        self.sb_min_percentile.setMaximum(100.0)
        self.sb_min_percentile.setSingleStep(1.0)
        self.sb_min_percentile.setObjectName("sb_min_percentile")
        self.gridLayout_2.addWidget(self.sb_min_percentile, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.cb_plot_type = QtWidgets.QComboBox(self.widget_2)
        self.cb_plot_type.setObjectName("cb_plot_type")
        self.cb_plot_type.addItem("")
        self.cb_plot_type.addItem("")
        self.gridLayout_2.addWidget(self.cb_plot_type, 4, 1, 1, 2)
        self.cb_colormap = QtWidgets.QComboBox(self.widget_2)
        self.cb_colormap.setObjectName("cb_colormap")
        self.gridLayout_2.addWidget(self.cb_colormap, 3, 1, 1, 2)
        self.verticalLayout.addWidget(self.widget_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(ColorScaleDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ColorScaleDialog)
        self.buttonBox.accepted.connect(ColorScaleDialog.accept)
        self.buttonBox.rejected.connect(ColorScaleDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ColorScaleDialog)
        ColorScaleDialog.setTabOrder(self.sb_min_percentile, self.sb_min_tick)
        ColorScaleDialog.setTabOrder(self.sb_min_tick, self.sb_max_percentile)
        ColorScaleDialog.setTabOrder(self.sb_max_percentile, self.sb_max_tick)
        ColorScaleDialog.setTabOrder(self.sb_max_tick, self.cb_colormap)
        ColorScaleDialog.setTabOrder(self.cb_colormap, self.cb_plot_type)

    def retranslateUi(self, ColorScaleDialog):
        _translate = QtCore.QCoreApplication.translate
        ColorScaleDialog.setWindowTitle(_translate("ColorScaleDialog", "Color Scale Editor"))
        self.label_2.setText(_translate("ColorScaleDialog", "Max"))
        self.label_3.setText(_translate("ColorScaleDialog", "Percentiles  ►►"))
        self.label_5.setText(_translate("ColorScaleDialog", "Colormap"))
        self.label.setText(_translate("ColorScaleDialog", "Min"))
        self.label_4.setText(_translate("ColorScaleDialog", "Ticks"))
        self.label_6.setText(_translate("ColorScaleDialog", "Plot type"))
        self.cb_plot_type.setItemText(0, _translate("ColorScaleDialog", "pixels"))
        self.cb_plot_type.setItemText(1, _translate("ColorScaleDialog", "contour"))
