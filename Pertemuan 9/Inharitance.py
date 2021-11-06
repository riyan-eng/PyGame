class Pegawai():
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
    def cetak(self):
        print("Nama pegawai:", self.nama)
        print("Alamat pegawai:", self.alamat)

class Manager(Pegawai):
    def __init__(self, nama, alamat):
        super().__init__(nama, alamat)
        self.manager = "manajer"
    
    def cetak(self):
        super().cetak()
        print("Status pegawai:", self.manager)

x = Pegawai("ardan", "yogyakarta")
x.cetak()
print()
y = Manager("ilmi", "malang")
y.cetak()