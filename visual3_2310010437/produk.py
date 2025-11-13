import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class Produk(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load(QFile("produk.ui"), self)
        self.aksi = crud()
        self.tampilData()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

    def bersih(self):
        self.ui.editID.clear()
        self.ui.editIDToko.clear()
        self.ui.editNama.clear()
        self.ui.editHarga.clear()
        self.ui.editKategori.clear()

    def simpan(self):
        if not self.ui.editID.text():
            QMessageBox.warning(self, "Eror", "ID Produk Kosong")
            return
        self.aksi.simpanProduk(
            self.ui.editID.text(), self.ui.editIDToko.text(),
            self.ui.editNama.text(), self.ui.editHarga.text(), self.ui.editKategori.text()
        )
        self.tampilData()
        self.bersih()

    def ubah(self):
        self.aksi.ubahProduk(
            self.ui.editID.text(), self.ui.editIDToko.text(),
            self.ui.editNama.text(), self.ui.editHarga.text(), self.ui.editKategori.text()
        )
        self.tampilData()
        self.bersih()

    def hapus(self):
        self.aksi.hapusProduk(self.ui.editID.text())
        self.tampilData()
        self.bersih()

    def tampilData(self):
        data = self.aksi.dataProduk()
        self.ui.tabelProduk.setRowCount(0)
        for i, row in enumerate(data):
            self.ui.tabelProduk.insertRow(i)
            self.ui.tabelProduk.setItem(i, 0, QTableWidgetItem(str(row['id_produk'])))
            self.ui.tabelProduk.setItem(i, 1, QTableWidgetItem(str(row['id_toko'])))
            self.ui.tabelProduk.setItem(i, 2, QTableWidgetItem(str(row['nama_produk'])))
            self.ui.tabelProduk.setItem(i, 3, QTableWidgetItem(str(row['harga'])))
            self.ui.tabelProduk.setItem(i, 4, QTableWidgetItem(str(row['kategori'])))
