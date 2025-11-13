# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionUser = QAction(MainWindow)
        self.actionUser.setObjectName(u"actionUser")
        self.actionToko = QAction(MainWindow)
        self.actionToko.setObjectName(u"actionToko")
        self.actionProduk = QAction(MainWindow)
        self.actionProduk.setObjectName(u"actionProduk")
        self.actionTransaksi = QAction(MainWindow)
        self.actionTransaksi.setObjectName(u"actionTransaksi")
        self.actionKurir = QAction(MainWindow)
        self.actionKurir.setObjectName(u"actionKurir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitle = QLabel(self.centralwidget)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitle)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 17))
        self.menuData = QMenu(self.menubar)
        self.menuData.setObjectName(u"menuData")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuData.menuAction())
        self.menuData.addAction(self.actionToko)
        self.menuData.addAction(self.actionProduk)
        self.menuData.addAction(self.actionTransaksi)
        self.menuData.addAction(self.actionKurir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistem Informasi Penjualan", None))
        self.actionUser.setText(QCoreApplication.translate("MainWindow", u"Data User", None))
        self.actionToko.setText(QCoreApplication.translate("MainWindow", u"Data Toko", None))
        self.actionProduk.setText(QCoreApplication.translate("MainWindow", u"Data Produk", None))
        self.actionTransaksi.setText(QCoreApplication.translate("MainWindow", u"Data Transaksi", None))
        self.actionKurir.setText(QCoreApplication.translate("MainWindow", u"Data Kurir", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u" APLIKASI E-COMMERCE PERIKANAN ", None))
        self.menuData.setTitle(QCoreApplication.translate("MainWindow", u"Menu Data", None))
    # retranslateUi

