# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/process_info_widget.ui'
#
# Created: Mon May 26 03:07:25 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ProcessInfoWidget(object):
    def setupUi(self, ProcessInfoWidget):
        ProcessInfoWidget.setObjectName("ProcessInfoWidget")
        ProcessInfoWidget.resize(400, 106)
        self.gridLayout = QtGui.QGridLayout(ProcessInfoWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lblInfo = QtGui.QLabel(ProcessInfoWidget)
        self.lblInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInfo.setObjectName("lblInfo")
        self.gridLayout.addWidget(self.lblInfo, 0, 0, 1, 1)

        self.retranslateUi(ProcessInfoWidget)
        QtCore.QMetaObject.connectSlotsByName(ProcessInfoWidget)

    def retranslateUi(self, ProcessInfoWidget):
        ProcessInfoWidget.setWindowTitle(QtGui.QApplication.translate("ProcessInfoWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lblInfo.setText(QtGui.QApplication.translate("ProcessInfoWidget", "Loading ...", None, QtGui.QApplication.UnicodeUTF8))

