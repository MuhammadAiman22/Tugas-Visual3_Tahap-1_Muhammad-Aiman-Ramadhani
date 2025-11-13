# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transaksi.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_FormTransaksi(object):
    def setupUi(self, FormTransaksi):
        if not FormTransaksi.objectName():
            FormTransaksi.setObjectName(u"FormTransaksi")
        FormTransaksi.resize(600, 500)
        self.formLayoutWidget = QWidget(FormTransaksi)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 20, 450, 150))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.l1 = QLabel(self.formLayoutWidget)
        self.l1.setObjectName(u"l1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l1)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.l2 = QLabel(self.formLayoutWidget)
        self.l2.setObjectName(u"l2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l2)

        self.editIDUser = QLineEdit(self.formLayoutWidget)
        self.editIDUser.setObjectName(u"editIDUser")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editIDUser)

        self.l3 = QLabel(self.formLayoutWidget)
        self.l3.setObjectName(u"l3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l3)

        self.editIDProduk = QLineEdit(self.formLayoutWidget)
        self.editIDProduk.setObjectName(u"editIDProduk")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editIDProduk)

        self.l4 = QLabel(self.formLayoutWidget)
        self.l4.setObjectName(u"l4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.l4)

        self.editJumlah = QLineEdit(self.formLayoutWidget)
        self.editJumlah.setObjectName(u"editJumlah")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editJumlah)

        self.l5 = QLabel(self.formLayoutWidget)
        self.l5.setObjectName(u"l5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.l5)

        self.editTotal = QLineEdit(self.formLayoutWidget)
        self.editTotal.setObjectName(u"editTotal")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editTotal)

        self.btnSimpan = QPushButton(FormTransaksi)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 190, 90, 29))
        self.btnHapus = QPushButton(FormTransaksi)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 190, 90, 29))
        self.btnUbah = QPushButton(FormTransaksi)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 190, 90, 29))
        self.btnBersih = QPushButton(FormTransaksi)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(390, 190, 90, 29))
        self.tabelTransaksi = QTableWidget(FormTransaksi)
        if (self.tabelTransaksi.columnCount() < 5):
            self.tabelTransaksi.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelTransaksi.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelTransaksi.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelTransaksi.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelTransaksi.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelTransaksi.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelTransaksi.setObjectName(u"tabelTransaksi")
        self.tabelTransaksi.setGeometry(QRect(50, 240, 500, 230))

        self.retranslateUi(FormTransaksi)

        QMetaObject.connectSlotsByName(FormTransaksi)
    # setupUi

    def retranslateUi(self, FormTransaksi):
        FormTransaksi.setWindowTitle(QCoreApplication.translate("FormTransaksi", u"Data Transaksi", None))
        self.l1.setText(QCoreApplication.translate("FormTransaksi", u"ID Transaksi", None))
        self.l2.setText(QCoreApplication.translate("FormTransaksi", u"ID User", None))
        self.l3.setText(QCoreApplication.translate("FormTransaksi", u"ID Produk", None))
        self.l4.setText(QCoreApplication.translate("FormTransaksi", u"Jumlah", None))
        self.l5.setText(QCoreApplication.translate("FormTransaksi", u"Total Bayar", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormTransaksi", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("FormTransaksi", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("FormTransaksi", u"Ubah", None))
        self.btnBersih.setText(QCoreApplication.translate("FormTransaksi", u"Bersih", None))
        ___qtablewidgetitem = self.tabelTransaksi.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormTransaksi", u"ID", None));
        ___qtablewidgetitem1 = self.tabelTransaksi.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormTransaksi", u"User", None));
        ___qtablewidgetitem2 = self.tabelTransaksi.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormTransaksi", u"Produk", None));
        ___qtablewidgetitem3 = self.tabelTransaksi.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormTransaksi", u"Jumlah", None));
        ___qtablewidgetitem4 = self.tabelTransaksi.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormTransaksi", u"Total", None));
    # retranslateUi

