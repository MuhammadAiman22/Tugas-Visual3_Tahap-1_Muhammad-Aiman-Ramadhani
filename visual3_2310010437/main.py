import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from toko import Toko
from produk import Produk
from transaksi import Transaksi
from kurir import Kurir

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load(QFile("main.ui"), self)

        # Connect Actions
        self.ui.actionToko.triggered.connect(self.buka_toko)
        self.ui.actionProduk.triggered.connect(self.buka_produk)
        self.ui.actionTransaksi.triggered.connect(self.buka_transaksi)
        self.ui.actionKurir.triggered.connect(self.buka_kurir)

    def buka_toko(self):
        self.window_toko = Toko()
        self.window_toko.show()

    def buka_produk(self):
        self.window_produk = Produk()
        self.window_produk.show()

    def buka_transaksi(self):
        self.window_transaksi = Transaksi()
        self.window_transaksi.show()

    def buka_kurir(self):
        self.window_kurir = Kurir()
        self.window_kurir.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.ui.show()
    sys.exit(app.exec())
