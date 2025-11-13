import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class Kurir(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load(QFile("kurir.ui"), self)
        self.aksi = crud()
        self.tampilData()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

    def bersih(self):
        self.ui.editID.clear()
        self.ui.editNama.clear()
        self.ui.editLayanan.clear()
        self.ui.editTarif.clear()
        self.ui.editEstimasi.clear()

    def simpan(self):
        if not self.ui.editID.text():
            QMessageBox.warning(self, "Eror", "ID Kurir Kosong")
            return
        self.aksi.simpanKurir(
            self.ui.editID.text(), self.ui.editNama.text(),
            self.ui.editLayanan.text(), self.ui.editTarif.text(), self.ui.editEstimasi.text()
        )
        self.tampilData()
        self.bersih()

    def ubah(self):
        self.aksi.ubahKurir(
            self.ui.editID.text(), self.ui.editNama.text(),
            self.ui.editLayanan.text(), self.ui.editTarif.text(), self.ui.editEstimasi.text()
        )
        self.tampilData()
        self.bersih()

    def hapus(self):
        self.aksi.hapusKurir(self.ui.editID.text())
        self.tampilData()
        self.bersih()

    def tampilData(self):
        data = self.aksi.dataKurir()
        self.ui.tabelKurir.setRowCount(0)
        for i, row in enumerate(data):
            self.ui.tabelKurir.insertRow(i)
            self.ui.tabelKurir.setItem(i, 0, QTableWidgetItem(str(row['id_kurir'])))
            self.ui.tabelKurir.setItem(i, 1, QTableWidgetItem(str(row['nama_kurir'])))
            self.ui.tabelKurir.setItem(i, 2, QTableWidgetItem(str(row['jenis_layanan'])))
            self.ui.tabelKurir.setItem(i, 3, QTableWidgetItem(str(row['tarif'])))
            self.ui.tabelKurir.setItem(i, 4, QTableWidgetItem(str(row['estimasi'])))
