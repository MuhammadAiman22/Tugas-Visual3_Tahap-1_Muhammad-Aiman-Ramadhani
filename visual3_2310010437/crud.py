import mysql.connector

class crud:
    def __init__(self):
        self.koneksiDB = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='visual3_2310010437'
        )


    def simpanToko(self, id_toko, id_user, nama_toko, alamat, status):
        kursor = self.koneksiDB.cursor()
        sql = "INSERT INTO toko (id_toko, id_user, nama_toko, alamat, status) VALUES (%s,%s,%s,%s,%s)"
        val = (id_toko, id_user, nama_toko, alamat, status)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahToko(self, id_toko, id_user, nama_toko, alamat, status):
        kursor = self.koneksiDB.cursor()
        sql = "UPDATE toko SET id_user=%s, nama_toko=%s, alamat=%s, status=%s WHERE id_toko=%s"
        val = (id_user, nama_toko, alamat, status, id_toko)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusToko(self, id_toko):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM toko WHERE id_toko=%s", (id_toko,))
        self.koneksiDB.commit()
        kursor.close()

    def dataToko(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM toko ORDER BY id_toko ASC")
        return kursor.fetchall()

    def simpanProduk(self, id_produk, id_toko, nama, harga, kategori):
        kursor = self.koneksiDB.cursor()
        sql = "INSERT INTO produk (id_produk, id_toko, nama_produk, harga, kategori) VALUES (%s,%s,%s,%s,%s)"
        val = (id_produk, id_toko, nama, harga, kategori)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahProduk(self, id_produk, id_toko, nama, harga, kategori):
        kursor = self.koneksiDB.cursor()
        sql = "UPDATE produk SET id_toko=%s, nama_produk=%s, harga=%s, kategori=%s WHERE id_produk=%s"
        val = (id_toko, nama, harga, kategori, id_produk)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusProduk(self, id_produk):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM produk WHERE id_produk=%s", (id_produk,))
        self.koneksiDB.commit()
        kursor.close()

    def dataProduk(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM produk ORDER BY id_produk ASC")
        return kursor.fetchall()

    def simpanTransaksi(self, id_transaksi, id_user, id_produk, jumlah, total):
        kursor = self.koneksiDB.cursor()
        sql = "INSERT INTO transaksi (id_transaksi, id_user, id_produk, jumlah, total_bayar) VALUES (%s,%s,%s,%s,%s)"
        val = (id_transaksi, id_user, id_produk, jumlah, total)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahTransaksi(self, id_transaksi, id_user, id_produk, jumlah, total):
        kursor = self.koneksiDB.cursor()
        sql = "UPDATE transaksi SET id_user=%s, id_produk=%s, jumlah=%s, total_bayar=%s WHERE id_transaksi=%s"
        val = (id_user, id_produk, jumlah, total, id_transaksi)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusTransaksi(self, id_transaksi):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM transaksi WHERE id_transaksi=%s", (id_transaksi,))
        self.koneksiDB.commit()
        kursor.close()

    def dataTransaksi(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM transaksi ORDER BY id_transaksi ASC")
        return kursor.fetchall()


    def simpanKurir(self, id_kurir, nama, layanan, tarif, estimasi):
        kursor = self.koneksiDB.cursor()
        sql = "INSERT INTO kurir (id_kurir, nama_kurir, jenis_layanan, tarif, estimasi) VALUES (%s,%s,%s,%s,%s)"
        val = (id_kurir, nama, layanan, tarif, estimasi)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahKurir(self, id_kurir, nama, layanan, tarif, estimasi):
        kursor = self.koneksiDB.cursor()
        sql = "UPDATE kurir SET nama_kurir=%s, jenis_layanan=%s, tarif=%s, estimasi=%s WHERE id_kurir=%s"
        val = (nama, layanan, tarif, estimasi, id_kurir)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusKurir(self, id_kurir):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM kurir WHERE id_kurir=%s", (id_kurir,))
        self.koneksiDB.commit()
        kursor.close()

    def dataKurir(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM kurir ORDER BY id_kurir ASC")
        return kursor.fetchall()
