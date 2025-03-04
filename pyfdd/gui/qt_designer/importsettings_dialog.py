# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'importsettings_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImportSettingsDialog(object):
    def setupUi(self, ImportSettingsDialog):
        ImportSettingsDialog.setObjectName("ImportSettingsDialog")
        ImportSettingsDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ImportSettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(ImportSettingsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setToolTip("")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.w_editables = QtWidgets.QWidget(self.widget)
        self.w_editables.setObjectName("w_editables")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.w_editables)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rb_timepix_quad = QtWidgets.QRadioButton(self.w_editables)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_timepix_quad.sizePolicy().hasHeightForWidth())
        self.rb_timepix_quad.setSizePolicy(sizePolicy)
        self.rb_timepix_quad.setObjectName("rb_timepix_quad")
        self.gridLayout_2.addWidget(self.rb_timepix_quad, 1, 1, 1, 1)
        self.rb_single_chip = QtWidgets.QRadioButton(self.w_editables)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_single_chip.sizePolicy().hasHeightForWidth())
        self.rb_single_chip.setSizePolicy(sizePolicy)
        self.rb_single_chip.setChecked(True)
        self.rb_single_chip.setObjectName("rb_single_chip")
        self.gridLayout_2.addWidget(self.rb_single_chip, 1, 0, 1, 1)
        self.rb_timepix3_quad = QtWidgets.QRadioButton(self.w_editables)
        self.rb_timepix3_quad.setObjectName("rb_timepix3_quad")
        self.gridLayout_2.addWidget(self.rb_timepix3_quad, 1, 2, 1, 1)
        self.le_config_label = QtWidgets.QLineEdit(self.w_editables)
        self.le_config_label.setObjectName("le_config_label")
        self.gridLayout_2.addWidget(self.le_config_label, 0, 2, 1, 1)
        self.le_orientation_commands = QtWidgets.QLineEdit(self.w_editables)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_orientation_commands.sizePolicy().hasHeightForWidth())
        self.le_orientation_commands.setSizePolicy(sizePolicy)
        self.le_orientation_commands.setObjectName("le_orientation_commands")
        self.gridLayout_2.addWidget(self.le_orientation_commands, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.w_editables)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.w_editables)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.w_editables, 1, 0, 1, 2)
        self.cb_import_config = QtWidgets.QComboBox(self.widget)
        self.cb_import_config.setObjectName("cb_import_config")
        self.cb_import_config.addItem("")
        self.cb_import_config.addItem("")
        self.gridLayout.addWidget(self.cb_import_config, 0, 0, 1, 2)
        self.pb_delete_configuration = QtWidgets.QPushButton(self.widget)
        self.pb_delete_configuration.setObjectName("pb_delete_configuration")
        self.gridLayout.addWidget(self.pb_delete_configuration, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.label_2 = QtWidgets.QLabel(ImportSettingsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(ImportSettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ImportSettingsDialog)
        self.buttonBox.accepted.connect(ImportSettingsDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(ImportSettingsDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ImportSettingsDialog)

    def retranslateUi(self, ImportSettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        ImportSettingsDialog.setWindowTitle(_translate("ImportSettingsDialog", "Import Settings"))
        self.rb_timepix_quad.setText(_translate("ImportSettingsDialog", "Timepix quad"))
        self.rb_single_chip.setText(_translate("ImportSettingsDialog", "Single chip"))
        self.rb_timepix3_quad.setText(_translate("ImportSettingsDialog", "Timepix3 quad"))
        self.label.setText(_translate("ImportSettingsDialog", "Orientation (cw, cc, mh, mv)"))
        self.label_4.setText(_translate("ImportSettingsDialog", "Configuration label"))
        self.cb_import_config.setItemText(0, _translate("ImportSettingsDialog", "Single chip"))
        self.cb_import_config.setItemText(1, _translate("ImportSettingsDialog", "New configuration"))
        self.pb_delete_configuration.setText(_translate("ImportSettingsDialog", "Delete configuration"))
        self.label_2.setText(_translate("ImportSettingsDialog", "<html><head/><body><p>Orientation commands:</p><p><span style=\" font-weight:600;\">cw</span> - Rotate Clockwise, <span style=\" font-weight:600;\">cc</span> - Rotate Counterclockwise,<br/><span style=\" font-weight:600;\">mh</span> - Mirror Horizontaly, <span style=\" font-weight:600;\">mv</span> - Mirror Verticaly.</p></body></html>"))
