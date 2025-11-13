import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class Transaksi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load(QFile("transaksi.ui"), self)
        self.aksi = crud()
        self.tampilData()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

    def bersih(self):
        self.ui.editID.clear()
        self.ui.editIDUser.clear()
        self.ui.editIDProduk.clear()
        self.ui.editJumlah.clear()
        self.ui.editTotal.clear()

    def simpan(self):
        if not self.ui.editID.text():
            QMessageBox.warning(self, "Eror", "ID Transaksi Kosong")
            return
        self.aksi.simpanTransaksi(
            self.ui.editID.text(), self.ui.editIDUser.text(),
            self.ui.editIDProduk.text(), self.ui.editJumlah.text(), self.ui.editTotal.text()
        )
        self.tampilData()
        self.bersih()

    def ubah(self):
        self.aksi.ubahTransaksi(
            self.ui.editID.text(), self.ui.editIDUser.text(),
            self.ui.editIDProduk.text(), self.ui.editJumlah.text(), self.ui.editTotal.text()
        )
        self.tampilData()
        self.bersih()

    def hapus(self):
        self.aksi.hapusTransaksi(self.ui.editID.text())
        self.tampilData()
        self.bersih()

    def tampilData(self):
        data = self.aksi.dataTransaksi()
        self.ui.tabelTransaksi.setRowCount(0)
        for i, row in enumerate(data):
            self.ui.tabelTransaksi.insertRow(i)
            self.ui.tabelTransaksi.setItem(i, 0, QTableWidgetItem(str(row['id_transaksi'])))
            self.ui.tabelTransaksi.setItem(i, 1, QTableWidgetItem(str(row['id_user'])))
            self.ui.tabelTransaksi.setItem(i, 2, QTableWidgetItem(str(row['id_produk'])))
            self.ui.tabelTransaksi.setItem(i, 3, QTableWidgetItem(str(row['jumlah'])))
            self.ui.tabelTransaksi.setItem(i, 4, QTableWidgetItem(str(row['total_bayar'])))
