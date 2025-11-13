# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'toko.ui'
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

class Ui_FormToko(object):
    def setupUi(self, FormToko):
        if not FormToko.objectName():
            FormToko.setObjectName(u"FormToko")
        FormToko.resize(600, 500)
        self.formLayoutWidget = QWidget(FormToko)
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

        self.editNamaToko = QLineEdit(self.formLayoutWidget)
        self.editNamaToko.setObjectName(u"editNamaToko")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editNamaToko)

        self.l4 = QLabel(self.formLayoutWidget)
        self.l4.setObjectName(u"l4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.l4)

        self.editAlamat = QLineEdit(self.formLayoutWidget)
        self.editAlamat.setObjectName(u"editAlamat")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editAlamat)

        self.l5 = QLabel(self.formLayoutWidget)
        self.l5.setObjectName(u"l5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.l5)

        self.editStatus = QLineEdit(self.formLayoutWidget)
        self.editStatus.setObjectName(u"editStatus")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editStatus)

        self.btnSimpan = QPushButton(FormToko)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 190, 90, 29))
        self.btnHapus = QPushButton(FormToko)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 190, 90, 29))
        self.btnUbah = QPushButton(FormToko)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 190, 90, 29))
        self.btnBersih = QPushButton(FormToko)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(390, 190, 90, 29))
        self.tabelToko = QTableWidget(FormToko)
        if (self.tabelToko.columnCount() < 5):
            self.tabelToko.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelToko.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelToko.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelToko.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelToko.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelToko.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelToko.setObjectName(u"tabelToko")
        self.tabelToko.setGeometry(QRect(50, 240, 500, 230))

        self.retranslateUi(FormToko)

        QMetaObject.connectSlotsByName(FormToko)
    # setupUi

    def retranslateUi(self, FormToko):
        FormToko.setWindowTitle(QCoreApplication.translate("FormToko", u"Data Toko", None))
        self.l1.setText(QCoreApplication.translate("FormToko", u"ID Toko", None))
        self.l2.setText(QCoreApplication.translate("FormToko", u"ID User", None))
        self.l3.setText(QCoreApplication.translate("FormToko", u"Nama Toko", None))
        self.l4.setText(QCoreApplication.translate("FormToko", u"Alamat", None))
        self.l5.setText(QCoreApplication.translate("FormToko", u"Status", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormToko", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("FormToko", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("FormToko", u"Ubah", None))
        self.btnBersih.setText(QCoreApplication.translate("FormToko", u"Bersih", None))
        ___qtablewidgetitem = self.tabelToko.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormToko", u"ID Toko", None));
        ___qtablewidgetitem1 = self.tabelToko.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormToko", u"ID User", None));
        ___qtablewidgetitem2 = self.tabelToko.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormToko", u"Nama Toko", None));
        ___qtablewidgetitem3 = self.tabelToko.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormToko", u"Alamat", None));
        ___qtablewidgetitem4 = self.tabelToko.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormToko", u"Status", None));
    # retranslateUi

