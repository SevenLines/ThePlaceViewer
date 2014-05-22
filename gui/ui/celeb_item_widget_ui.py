# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/celeb_item_widget.ui'
#
# Created: Fri May 23 02:43:48 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CelebItemWidget(object):
    def setupUi(self, CelebItemWidget):
        CelebItemWidget.setObjectName("CelebItemWidget")
        CelebItemWidget.resize(219, 33)
        self.gridLayout = QtGui.QGridLayout(CelebItemWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lblInfo = QtGui.QLabel(CelebItemWidget)
        self.lblInfo.setObjectName("lblInfo")
        self.gridLayout.addWidget(self.lblInfo, 0, 0, 1, 1)

        self.retranslateUi(CelebItemWidget)
        QtCore.QMetaObject.connectSlotsByName(CelebItemWidget)

    def retranslateUi(self, CelebItemWidget):
        CelebItemWidget.setWindowTitle(QtGui.QApplication.translate("CelebItemWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lblInfo.setText(QtGui.QApplication.translate("CelebItemWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

