import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class Toko(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load(QFile("toko.ui"), self)
        self.aksi = crud()
        self.tampilData()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

    def bersih(self):
        self.ui.editID.clear()
        self.ui.editIDUser.clear()
        self.ui.editNamaToko.clear()
        self.ui.editAlamat.clear()
        self.ui.editStatus.clear()

    def simpan(self):
        if not self.ui.editID.text():
            QMessageBox.warning(self, "Eror", "ID Toko Kosong")
            return
        self.aksi.simpanToko(
            self.ui.editID.text(), self.ui.editIDUser.text(),
            self.ui.editNamaToko.text(), self.ui.editAlamat.text(), self.ui.editStatus.text()
        )
        self.tampilData()
        self.bersih()

    def ubah(self):
        self.aksi.ubahToko(
            self.ui.editID.text(), self.ui.editIDUser.text(),
            self.ui.editNamaToko.text(), self.ui.editAlamat.text(), self.ui.editStatus.text()
        )
        self.tampilData()
        self.bersih()

    def hapus(self):
        self.aksi.hapusToko(self.ui.editID.text())
        self.tampilData()
        self.bersih()

    def tampilData(self):
        data = self.aksi.dataToko()
        self.ui.tabelToko.setRowCount(0)
        for i, row in enumerate(data):
            self.ui.tabelToko.insertRow(i)
            self.ui.tabelToko.setItem(i, 0, QTableWidgetItem(str(row['id_toko'])))
            self.ui.tabelToko.setItem(i, 1, QTableWidgetItem(str(row['id_user'])))
            self.ui.tabelToko.setItem(i, 2, QTableWidgetItem(str(row['nama_toko'])))
            self.ui.tabelToko.setItem(i, 3, QTableWidgetItem(str(row['alamat'])))
            self.ui.tabelToko.setItem(i, 4, QTableWidgetItem(str(row['status'])))
