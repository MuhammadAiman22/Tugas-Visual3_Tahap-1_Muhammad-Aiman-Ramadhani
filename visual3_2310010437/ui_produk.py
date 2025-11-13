# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'produk.ui'
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

class Ui_FormProduk(object):
    def setupUi(self, FormProduk):
        if not FormProduk.objectName():
            FormProduk.setObjectName(u"FormProduk")
        FormProduk.resize(600, 500)
        self.formLayoutWidget = QWidget(FormProduk)
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

        self.editIDToko = QLineEdit(self.formLayoutWidget)
        self.editIDToko.setObjectName(u"editIDToko")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editIDToko)

        self.l3 = QLabel(self.formLayoutWidget)
        self.l3.setObjectName(u"l3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l3)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.l4 = QLabel(self.formLayoutWidget)
        self.l4.setObjectName(u"l4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.l4)

        self.editHarga = QLineEdit(self.formLayoutWidget)
        self.editHarga.setObjectName(u"editHarga")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editHarga)

        self.l5 = QLabel(self.formLayoutWidget)
        self.l5.setObjectName(u"l5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.l5)

        self.editKategori = QLineEdit(self.formLayoutWidget)
        self.editKategori.setObjectName(u"editKategori")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editKategori)

        self.btnSimpan = QPushButton(FormProduk)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 190, 90, 29))
        self.btnHapus = QPushButton(FormProduk)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 190, 90, 29))
        self.btnUbah = QPushButton(FormProduk)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 190, 90, 29))
        self.btnBersih = QPushButton(FormProduk)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(390, 190, 90, 29))
        self.tabelProduk = QTableWidget(FormProduk)
        if (self.tabelProduk.columnCount() < 5):
            self.tabelProduk.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelProduk.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelProduk.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelProduk.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelProduk.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelProduk.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelProduk.setObjectName(u"tabelProduk")
        self.tabelProduk.setGeometry(QRect(50, 240, 500, 230))

        self.retranslateUi(FormProduk)

        QMetaObject.connectSlotsByName(FormProduk)
    # setupUi

    def retranslateUi(self, FormProduk):
        FormProduk.setWindowTitle(QCoreApplication.translate("FormProduk", u"Data Produk", None))
        self.l1.setText(QCoreApplication.translate("FormProduk", u"ID Produk", None))
        self.l2.setText(QCoreApplication.translate("FormProduk", u"ID Toko", None))
        self.l3.setText(QCoreApplication.translate("FormProduk", u"Nama Produk", None))
        self.l4.setText(QCoreApplication.translate("FormProduk", u"Harga", None))
        self.l5.setText(QCoreApplication.translate("FormProduk", u"Kategori", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormProduk", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("FormProduk", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("FormProduk", u"Ubah", None))
        self.btnBersih.setText(QCoreApplication.translate("FormProduk", u"Bersih", None))
        ___qtablewidgetitem = self.tabelProduk.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormProduk", u"ID", None));
        ___qtablewidgetitem1 = self.tabelProduk.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormProduk", u"Toko", None));
        ___qtablewidgetitem2 = self.tabelProduk.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormProduk", u"Nama Produk", None));
        ___qtablewidgetitem3 = self.tabelProduk.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormProduk", u"Harga", None));
        ___qtablewidgetitem4 = self.tabelProduk.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormProduk", u"Kategori", None));
    # retranslateUi

