class Pegawai():
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
    def cetak(self):
        print("Nama pegawai:", self.nama)
        print("Alamat pegawai:", self.alamat)

x = Pegawai("ardan", "yogyakarta")
x.cetak()