class Pegawai():
    def nama_pegawai(self):
        nama = "Ardan"
        return nama
    def alamat_pegawai(self):
        alamat = "Yogyakarta"
        return alamat

    def cetak(self):
        print("Nama pegawai:", self.nama_pegawai())
        print("Alamat pegawai:", self.alamat_pegawai())

x = Pegawai()
x.cetak()