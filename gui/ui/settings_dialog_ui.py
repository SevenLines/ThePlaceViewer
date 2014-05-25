# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/settings_dialog.ui'
#
# Created: Mon May 26 03:07:26 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(400, 313)
        self.gridLayout = QtGui.QGridLayout(SettingsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtGui.QStackedWidget(SettingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pgEnvironment = QtGui.QWidget()
        self.pgEnvironment.setObjectName("pgEnvironment")
        self.gridLayout_2 = QtGui.QGridLayout(self.pgEnvironment)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(self.pgEnvironment)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.edtSaveDirectory = QtGui.QLineEdit(self.pgEnvironment)
        self.edtSaveDirectory.setObjectName("edtSaveDirectory")
        self.gridLayout_2.addWidget(self.edtSaveDirectory, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 3)
        self.btnSaveDirectory = QtGui.QPushButton(self.pgEnvironment)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSaveDirectory.sizePolicy().hasHeightForWidth())
        self.btnSaveDirectory.setSizePolicy(sizePolicy)
        self.btnSaveDirectory.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btnSaveDirectory.setObjectName("btnSaveDirectory")
        self.gridLayout_2.addWidget(self.btnSaveDirectory, 0, 2, 1, 1)
        self.stackedWidget.addWidget(self.pgEnvironment)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        self.selector = QtGui.QFrame(SettingsDialog)
        self.selector.setFrameShape(QtGui.QFrame.NoFrame)
        self.selector.setFrameShadow(QtGui.QFrame.Raised)
        self.selector.setLineWidth(0)
        self.selector.setObjectName("selector")
        self.gridLayout_3 = QtGui.QGridLayout(self.selector)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnEnvironment = QtGui.QPushButton(self.selector)
        self.btnEnvironment.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/folder_big.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEnvironment.setIcon(icon)
        self.btnEnvironment.setIconSize(QtCore.QSize(64, 64))
        self.btnEnvironment.setCheckable(True)
        self.btnEnvironment.setChecked(True)
        self.btnEnvironment.setAutoExclusive(True)
        self.btnEnvironment.setFlat(True)
        self.btnEnvironment.setObjectName("btnEnvironment")
        self.gridLayout_3.addWidget(self.btnEnvironment, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.selector)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.selector, 0, 0, 2, 1)

        self.retranslateUi(SettingsDialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtGui.QApplication.translate("SettingsDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingsDialog", "Save directory", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSaveDirectory.setText(QtGui.QApplication.translate("SettingsDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SettingsDialog", "Environment", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
