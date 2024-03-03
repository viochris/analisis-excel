class Mobil:
    def __init__(self, warna, nama, tahun):
        self.warna = warna
        self.nama = nama
        self.tahun = tahun


mobil_1 = Mobil('Merah', 'BMW', 2020)
print(mobil_1.warna)
print(mobil_1.nama)
print(mobil_1.tahun)