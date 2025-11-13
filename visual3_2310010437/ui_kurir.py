# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kurir.ui'
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

class Ui_FormKurir(object):
    def setupUi(self, FormKurir):
        if not FormKurir.objectName():
            FormKurir.setObjectName(u"FormKurir")
        FormKurir.resize(500, 450)
        self.formLayoutWidget = QWidget(FormKurir)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 20, 400, 150))
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

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.l3 = QLabel(self.formLayoutWidget)
        self.l3.setObjectName(u"l3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l3)

        self.editLayanan = QLineEdit(self.formLayoutWidget)
        self.editLayanan.setObjectName(u"editLayanan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editLayanan)

        self.l4 = QLabel(self.formLayoutWidget)
        self.l4.setObjectName(u"l4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.l4)

        self.editTarif = QLineEdit(self.formLayoutWidget)
        self.editTarif.setObjectName(u"editTarif")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTarif)

        self.l5 = QLabel(self.formLayoutWidget)
        self.l5.setObjectName(u"l5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.l5)

        self.editEstimasi = QLineEdit(self.formLayoutWidget)
        self.editEstimasi.setObjectName(u"editEstimasi")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editEstimasi)

        self.btnSimpan = QPushButton(FormKurir)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 190, 90, 29))
        self.btnHapus = QPushButton(FormKurir)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 190, 90, 29))
        self.btnUbah = QPushButton(FormKurir)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 190, 90, 29))
        self.btnBersih = QPushButton(FormKurir)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(390, 190, 90, 29))
        self.tabelKurir = QTableWidget(FormKurir)
        if (self.tabelKurir.columnCount() < 5):
            self.tabelKurir.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelKurir.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelKurir.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelKurir.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelKurir.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelKurir.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelKurir.setObjectName(u"tabelKurir")
        self.tabelKurir.setGeometry(QRect(50, 240, 400, 200))

        self.retranslateUi(FormKurir)

        QMetaObject.connectSlotsByName(FormKurir)
    # setupUi

    def retranslateUi(self, FormKurir):
        FormKurir.setWindowTitle(QCoreApplication.translate("FormKurir", u"Data Kurir", None))
        self.l1.setText(QCoreApplication.translate("FormKurir", u"ID Kurir", None))
        self.l2.setText(QCoreApplication.translate("FormKurir", u"Nama Kurir", None))
        self.l3.setText(QCoreApplication.translate("FormKurir", u"Jenis Layanan", None))
        self.l4.setText(QCoreApplication.translate("FormKurir", u"Tarif", None))
        self.l5.setText(QCoreApplication.translate("FormKurir", u"Estimasi", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormKurir", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("FormKurir", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("FormKurir", u"Ubah", None))
        self.btnBersih.setText(QCoreApplication.translate("FormKurir", u"Bersih", None))
        ___qtablewidgetitem = self.tabelKurir.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormKurir", u"ID", None));
        ___qtablewidgetitem1 = self.tabelKurir.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormKurir", u"Nama", None));
        ___qtablewidgetitem2 = self.tabelKurir.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormKurir", u"Layanan", None));
        ___qtablewidgetitem3 = self.tabelKurir.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormKurir", u"Tarif", None));
        ___qtablewidgetitem4 = self.tabelKurir.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormKurir", u"Estimasi", None));
    # retranslateUi

