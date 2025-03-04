# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datapattern_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataPatternWidget(object):
    def setupUi(self, DataPatternWidget):
        DataPatternWidget.setObjectName("DataPatternWidget")
        DataPatternWidget.resize(1150, 670)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DataPatternWidget.sizePolicy().hasHeightForWidth())
        DataPatternWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(DataPatternWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mplwindow = QtWidgets.QFrame(DataPatternWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow.sizePolicy().hasHeightForWidth())
        self.mplwindow.setSizePolicy(sizePolicy)
        self.mplwindow.setMinimumSize(QtCore.QSize(550, 550))
        self.mplwindow.setMaximumSize(QtCore.QSize(6000, 6000))
        self.mplwindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.mplwindow.setAutoFillBackground(False)
        self.mplwindow.setFrameShape(QtWidgets.QFrame.Box)
        self.mplwindow.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mplwindow.setObjectName("mplwindow")
        self.mplvl = QtWidgets.QHBoxLayout(self.mplwindow)
        self.mplvl.setContentsMargins(9, 9, 9, 9)
        self.mplvl.setSpacing(6)
        self.mplvl.setObjectName("mplvl")
        self.horizontalLayout.addWidget(self.mplwindow)
        self.widget_2 = QtWidgets.QWidget(DataPatternWidget)
        self.widget_2.setMaximumSize(QtCore.QSize(340, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.info_groupBox = QtWidgets.QGroupBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_groupBox.sizePolicy().hasHeightForWidth())
        self.info_groupBox.setSizePolicy(sizePolicy)
        self.info_groupBox.setObjectName("info_groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.info_groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.infotext = QtWidgets.QTextBrowser(self.info_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infotext.sizePolicy().hasHeightForWidth())
        self.infotext.setSizePolicy(sizePolicy)
        self.infotext.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.infotext.setFont(font)
        self.infotext.setAcceptRichText(True)
        self.infotext.setObjectName("infotext")
        self.verticalLayout_3.addWidget(self.infotext)
        self.verticalLayout_2.addWidget(self.info_groupBox)
        self.mask_groupBox = QtWidgets.QGroupBox(self.widget_2)
        self.mask_groupBox.setObjectName("mask_groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mask_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pb_maskpixel = QtWidgets.QPushButton(self.mask_groupBox)
        self.pb_maskpixel.setCheckable(True)
        self.pb_maskpixel.setChecked(False)
        self.pb_maskpixel.setObjectName("pb_maskpixel")
        self.bg_mask_group = QtWidgets.QButtonGroup(DataPatternWidget)
        self.bg_mask_group.setObjectName("bg_mask_group")
        self.bg_mask_group.setExclusive(False)
        self.bg_mask_group.addButton(self.pb_maskpixel)
        self.gridLayout_2.addWidget(self.pb_maskpixel, 0, 0, 1, 1)
        self.pb_maskrectangle = QtWidgets.QPushButton(self.mask_groupBox)
        self.pb_maskrectangle.setCheckable(True)
        self.pb_maskrectangle.setObjectName("pb_maskrectangle")
        self.bg_mask_group.addButton(self.pb_maskrectangle)
        self.gridLayout_2.addWidget(self.pb_maskrectangle, 0, 1, 1, 1)
        self.pb_removecentral = QtWidgets.QPushButton(self.mask_groupBox)
        self.pb_removecentral.setObjectName("pb_removecentral")
        self.bg_mask_group.addButton(self.pb_removecentral)
        self.gridLayout_2.addWidget(self.pb_removecentral, 3, 1, 1, 1)
        self.pb_maskedge = QtWidgets.QPushButton(self.mask_groupBox)
        self.pb_maskedge.setObjectName("pb_maskedge")
        self.bg_mask_group.addButton(self.pb_maskedge)
        self.gridLayout_2.addWidget(self.pb_maskedge, 3, 0, 1, 1)
        self.pb_savemask = QtWidgets.QPushButton(self.mask_groupBox)
        self.pb_savemask.setObjectName("pb_savemask")
        self.bg_mask_group.addButton(self.pb_savemask)
        self.gridLayout_2.addWidget(self.pb_savemask, 5, 1, 1, 1)
        self.pb_loadmask = QtWidgets.QPushButton(self.mask_groupBox)
        self.pb_loadmask.setObjectName("pb_loadmask")
        self.bg_mask_group.addButton(self.pb_loadmask)
        self.gridLayout_2.addWidget(self.pb_loadmask, 5, 0, 1, 1)
        self.pb_maskbelow = QtWidgets.QPushButton(self.mask_groupBox)
        self.pb_maskbelow.setObjectName("pb_maskbelow")
        self.bg_mask_group.addButton(self.pb_maskbelow)
        self.gridLayout_2.addWidget(self.pb_maskbelow, 1, 0, 1, 1)
        self.pb_maskabove = QtWidgets.QPushButton(self.mask_groupBox)
        self.pb_maskabove.setObjectName("pb_maskabove")
        self.bg_mask_group.addButton(self.pb_maskabove)
        self.gridLayout_2.addWidget(self.pb_maskabove, 1, 1, 1, 1)
        self.pb_expandmask = QtWidgets.QPushButton(self.mask_groupBox)
        self.pb_expandmask.setObjectName("pb_expandmask")
        self.bg_mask_group.addButton(self.pb_expandmask)
        self.gridLayout_2.addWidget(self.pb_expandmask, 4, 0, 1, 1)
        self.pb_clearmask = QtWidgets.QPushButton(self.mask_groupBox)
        self.pb_clearmask.setObjectName("pb_clearmask")
        self.bg_mask_group.addButton(self.pb_clearmask)
        self.gridLayout_2.addWidget(self.pb_clearmask, 4, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.mask_groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pb_buildmesh = QtWidgets.QPushButton(self.groupBox_3)
        self.pb_buildmesh.setCheckable(False)
        self.pb_buildmesh.setObjectName("pb_buildmesh")
        self.bg_manip_group = QtWidgets.QButtonGroup(DataPatternWidget)
        self.bg_manip_group.setObjectName("bg_manip_group")
        self.bg_manip_group.setExclusive(False)
        self.bg_manip_group.addButton(self.pb_buildmesh)
        self.gridLayout_4.addWidget(self.pb_buildmesh, 0, 1, 1, 2)
        self.pb_fitrange = QtWidgets.QPushButton(self.groupBox_3)
        self.pb_fitrange.setObjectName("pb_fitrange")
        self.bg_manip_group.addButton(self.pb_fitrange)
        self.gridLayout_4.addWidget(self.pb_fitrange, 4, 1, 1, 2)
        self.pb_orientchanneling = QtWidgets.QPushButton(self.groupBox_3)
        self.pb_orientchanneling.setCheckable(True)
        self.pb_orientchanneling.setObjectName("pb_orientchanneling")
        self.bg_manip_group.addButton(self.pb_orientchanneling)
        self.gridLayout_4.addWidget(self.pb_orientchanneling, 3, 1, 1, 1)
        self.pb_editorientation = QtWidgets.QPushButton(self.groupBox_3)
        self.pb_editorientation.setObjectName("pb_editorientation")
        self.bg_manip_group.addButton(self.pb_editorientation)
        self.gridLayout_4.addWidget(self.pb_editorientation, 3, 2, 1, 1)
        self.pb_compressmesh = QtWidgets.QPushButton(self.groupBox_3)
        self.pb_compressmesh.setObjectName("pb_compressmesh")
        self.bg_manip_group.addButton(self.pb_compressmesh)
        self.gridLayout_4.addWidget(self.pb_compressmesh, 1, 1, 1, 2)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.pb_setticks = QtWidgets.QGroupBox(self.widget_2)
        self.pb_setticks.setObjectName("pb_setticks")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.pb_setticks)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_colorscale = QtWidgets.QPushButton(self.pb_setticks)
        self.pb_colorscale.setObjectName("pb_colorscale")
        self.bg_vis_group = QtWidgets.QButtonGroup(DataPatternWidget)
        self.bg_vis_group.setObjectName("bg_vis_group")
        self.bg_vis_group.setExclusive(False)
        self.bg_vis_group.addButton(self.pb_colorscale)
        self.verticalLayout.addWidget(self.pb_colorscale)
        self.pb_setlabels = QtWidgets.QPushButton(self.pb_setticks)
        self.pb_setlabels.setObjectName("pb_setlabels")
        self.bg_vis_group.addButton(self.pb_setlabels)
        self.verticalLayout.addWidget(self.pb_setlabels)
        self.verticalLayout_2.addWidget(self.pb_setticks)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.widget_2)

        self.retranslateUi(DataPatternWidget)
        QtCore.QMetaObject.connectSlotsByName(DataPatternWidget)

    def retranslateUi(self, DataPatternWidget):
        _translate = QtCore.QCoreApplication.translate
        DataPatternWidget.setWindowTitle(_translate("DataPatternWidget", "Form"))
        self.info_groupBox.setTitle(_translate("DataPatternWidget", "Info"))
        self.infotext.setHtml(_translate("DataPatternWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\';\">Total counts: 0; Valid: 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\';\">Active pixels: 0; Masked: 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\';\">Angular range (x, y): 0, 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\';\">Pattern orientation (x, y, phi): 0, 0, 0</span></p></body></html>"))
        self.mask_groupBox.setTitle(_translate("DataPatternWidget", "Mask"))
        self.pb_maskpixel.setText(_translate("DataPatternWidget", "Mask Individual Pixels"))
        self.pb_maskrectangle.setText(_translate("DataPatternWidget", "Mask Rectangle"))
        self.pb_removecentral.setText(_translate("DataPatternWidget", "Mask Quad Pixels"))
        self.pb_maskedge.setText(_translate("DataPatternWidget", "Mask Edge Pixels"))
        self.pb_savemask.setText(_translate("DataPatternWidget", "Save Mask"))
        self.pb_loadmask.setText(_translate("DataPatternWidget", "Load Mask"))
        self.pb_maskbelow.setText(_translate("DataPatternWidget", "Mask Below"))
        self.pb_maskabove.setText(_translate("DataPatternWidget", "Mask Above"))
        self.pb_expandmask.setText(_translate("DataPatternWidget", "Expand Mask"))
        self.pb_clearmask.setText(_translate("DataPatternWidget", "Clear Mask"))
        self.groupBox_3.setTitle(_translate("DataPatternWidget", "Pattern Manipulation"))
        self.pb_buildmesh.setText(_translate("DataPatternWidget", "Build Angular Calibration Mesh"))
        self.pb_fitrange.setText(_translate("DataPatternWidget", "Set Fit Range"))
        self.pb_orientchanneling.setText(_translate("DataPatternWidget", "Orient Channeling Axis"))
        self.pb_editorientation.setText(_translate("DataPatternWidget", "Edit Orientation"))
        self.pb_compressmesh.setText(_translate("DataPatternWidget", "Compress Pixel Mesh"))
        self.pb_setticks.setTitle(_translate("DataPatternWidget", "Pattern Visualization"))
        self.pb_colorscale.setText(_translate("DataPatternWidget", "Edit Color Scale"))
        self.pb_setlabels.setText(_translate("DataPatternWidget", "Set Labels"))
