# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/mainForm.ui'
#
# Created: Fri May 23 02:43:48 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 378)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.edtFilter = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtFilter.sizePolicy().hasHeightForWidth())
        self.edtFilter.setSizePolicy(sizePolicy)
        self.edtFilter.setObjectName("edtFilter")
        self.verticalLayout.addWidget(self.edtFilter)
        self.lstCelebs = QtGui.QTableView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstCelebs.sizePolicy().hasHeightForWidth())
        self.lstCelebs.setSizePolicy(sizePolicy)
        self.lstCelebs.setShowGrid(True)
        self.lstCelebs.setGridStyle(QtCore.Qt.SolidLine)
        self.lstCelebs.setObjectName("lstCelebs")
        self.lstCelebs.horizontalHeader().setVisible(False)
        self.lstCelebs.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.lstCelebs)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.lstImages = QtGui.QTableWidget(self.centralwidget)
        self.lstImages.setStyleSheet("QLabel {\n"
"    padding:10px;\n"
"    margin:2px;\n"
"    border: 1px solid gray;\n"
"    border-radius: 16px;\n"
"}")
        self.lstImages.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lstImages.setGridStyle(QtCore.Qt.NoPen)
        self.lstImages.setColumnCount(3)
        self.lstImages.setObjectName("lstImages")
        self.lstImages.setColumnCount(3)
        self.lstImages.setRowCount(0)
        self.lstImages.horizontalHeader().setVisible(False)
        self.lstImages.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.lstImages, 0, 1, 1, 1)
        self.lblCeleb = QtGui.QLabel(self.centralwidget)
        self.lblCeleb.setGeometry(QtCore.QRect(249, 9, 16, 16))
        self.lblCeleb.setText("")
        self.lblCeleb.setObjectName("lblCeleb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 25))
        self.menubar.setObjectName("menubar")
        self.menuThePlace_ru = QtGui.QMenu(self.menubar)
        self.menuThePlace_ru.setObjectName("menuThePlace_ru")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUpdate = QtGui.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuThePlace_ru.addAction(self.actionUpdate)
        self.menuThePlace_ru.addSeparator()
        self.menuThePlace_ru.addAction(self.actionExit)
        self.menubar.addAction(self.menuThePlace_ru.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuThePlace_ru.setTitle(QtGui.QApplication.translate("MainWindow", "ThePlace.ru", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))

