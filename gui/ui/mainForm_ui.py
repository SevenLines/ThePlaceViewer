# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/mainForm.ui'
#
# Created: Sun May 25 14:56:04 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 397)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.edtFilter = LabelFilterEdit(self.centralwidget)
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
        self.lstCelebs.setMaximumSize(QtCore.QSize(165, 16777215))
        self.lstCelebs.setShowGrid(True)
        self.lstCelebs.setGridStyle(QtCore.Qt.SolidLine)
        self.lstCelebs.setObjectName("lstCelebs")
        self.lstCelebs.horizontalHeader().setVisible(False)
        self.lstCelebs.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.lstCelebs)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.splitImages = QtGui.QSplitter(self.centralwidget)
        self.splitImages.setOrientation(QtCore.Qt.Horizontal)
        self.splitImages.setObjectName("splitImages")
        self.layoutWidget = QtGui.QWidget(self.splitImages)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblCeleb = QtGui.QLabel(self.layoutWidget)
        self.lblCeleb.setText("")
        self.lblCeleb.setScaledContents(False)
        self.lblCeleb.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCeleb.setObjectName("lblCeleb")
        self.verticalLayout_2.addWidget(self.lblCeleb)
        self.lstImages = QtGui.QTableWidget(self.layoutWidget)
        self.lstImages.setStyleSheet("LabelImage {\n"
"    padding:10px;\n"
"    border: 1px solid black;\n"
"}")
        self.lstImages.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lstImages.setGridStyle(QtCore.Qt.NoPen)
        self.lstImages.setColumnCount(3)
        self.lstImages.setObjectName("lstImages")
        self.lstImages.setColumnCount(3)
        self.lstImages.setRowCount(0)
        self.lstImages.horizontalHeader().setVisible(False)
        self.lstImages.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.lstImages)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnPrevious = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPrevious.sizePolicy().hasHeightForWidth())
        self.btnPrevious.setSizePolicy(sizePolicy)
        self.btnPrevious.setMaximumSize(QtCore.QSize(24, 16777215))
        self.btnPrevious.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/arrow-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPrevious.setIcon(icon)
        self.btnPrevious.setIconSize(QtCore.QSize(24, 24))
        self.btnPrevious.setFlat(True)
        self.btnPrevious.setObjectName("btnPrevious")
        self.horizontalLayout.addWidget(self.btnPrevious)
        self.spnPage = QtGui.QSpinBox(self.layoutWidget)
        self.spnPage.setSuffix("")
        self.spnPage.setMinimum(1)
        self.spnPage.setObjectName("spnPage")
        self.horizontalLayout.addWidget(self.spnPage)
        self.btnNext = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNext.sizePolicy().hasHeightForWidth())
        self.btnNext.setSizePolicy(sizePolicy)
        self.btnNext.setMaximumSize(QtCore.QSize(24, 16777215))
        self.btnNext.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/arrow-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNext.setIcon(icon1)
        self.btnNext.setIconSize(QtCore.QSize(24, 24))
        self.btnNext.setFlat(True)
        self.btnNext.setObjectName("btnNext")
        self.horizontalLayout.addWidget(self.btnNext)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.lblPreview = LabelImage(self.splitImages)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPreview.sizePolicy().hasHeightForWidth())
        self.lblPreview.setSizePolicy(sizePolicy)
        self.lblPreview.setMinimumSize(QtCore.QSize(0, 0))
        self.lblPreview.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lblPreview.setText("")
        self.lblPreview.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPreview.setObjectName("lblPreview")
        self.gridLayout.addWidget(self.splitImages, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 25))
        self.menubar.setObjectName("menubar")
        self.menuThePlace_ru = QtGui.QMenu(self.menubar)
        self.menuThePlace_ru.setObjectName("menuThePlace_ru")
        self.menuIvalidateCache = QtGui.QMenu(self.menuThePlace_ru)
        self.menuIvalidateCache.setObjectName("menuIvalidateCache")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionUpdate = QtGui.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionExit = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/power.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName("actionExit")
        self.actionInvalideateCacheAll = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/rainbow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInvalideateCacheAll.setIcon(icon3)
        self.actionInvalideateCacheAll.setObjectName("actionInvalideateCacheAll")
        self.actionInvalideateCachePage = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/refresh-01-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInvalideateCachePage.setIcon(icon4)
        self.actionInvalideateCachePage.setObjectName("actionInvalideateCachePage")
        self.actionInvalideateCacheCeleb = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/loading.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInvalideateCacheCeleb.setIcon(icon5)
        self.actionInvalideateCacheCeleb.setObjectName("actionInvalideateCacheCeleb")
        self.actionUpdate_database = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpdate_database.setIcon(icon6)
        self.actionUpdate_database.setObjectName("actionUpdate_database")
        self.menuIvalidateCache.addAction(self.actionInvalideateCachePage)
        self.menuIvalidateCache.addAction(self.actionInvalideateCacheCeleb)
        self.menuIvalidateCache.addSeparator()
        self.menuIvalidateCache.addAction(self.actionInvalideateCacheAll)
        self.menuThePlace_ru.addAction(self.actionUpdate_database)
        self.menuThePlace_ru.addAction(self.menuIvalidateCache.menuAction())
        self.menuThePlace_ru.addSeparator()
        self.menuThePlace_ru.addAction(self.actionExit)
        self.menubar.addAction(self.menuThePlace_ru.menuAction())
        self.toolBar.addAction(self.actionUpdate_database)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionInvalideateCacheAll)
        self.toolBar.addAction(self.actionInvalideateCacheCeleb)
        self.toolBar.addAction(self.actionInvalideateCachePage)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.btnNext, QtCore.SIGNAL("clicked()"), self.spnPage.stepUp)
        QtCore.QObject.connect(self.btnPrevious, QtCore.SIGNAL("clicked()"), self.spnPage.stepDown)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuThePlace_ru.setTitle(QtGui.QApplication.translate("MainWindow", "ThePlace.ru", None, QtGui.QApplication.UnicodeUTF8))
        self.menuIvalidateCache.setTitle(QtGui.QApplication.translate("MainWindow", "Invalidate Cache", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInvalideateCacheAll.setText(QtGui.QApplication.translate("MainWindow", "Refresh all", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInvalideateCacheAll.setToolTip(QtGui.QApplication.translate("MainWindow", "Refresh all", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInvalideateCachePage.setText(QtGui.QApplication.translate("MainWindow", "Refresh page", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInvalideateCachePage.setToolTip(QtGui.QApplication.translate("MainWindow", "Refresh page", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInvalideateCacheCeleb.setText(QtGui.QApplication.translate("MainWindow", "Refresh celeb", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInvalideateCacheCeleb.setToolTip(QtGui.QApplication.translate("MainWindow", "Refresh celeb", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_database.setText(QtGui.QApplication.translate("MainWindow", "Update database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_database.setToolTip(QtGui.QApplication.translate("MainWindow", "Update database", None, QtGui.QApplication.UnicodeUTF8))

from gui.LabelImage import LabelImage
from gui.label_filter_edit import LabelFilterEdit
import icons_rc
