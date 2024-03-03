class Mobil:
    def __init__(self, warna, merk, kecepatan):
        self.warna = warna
        self.merk = merk
        self.kecepatan = kecepatan
        
    def tambah(self):
        self.kecepatan += 10
mobil1 = Mobil('Hitam', 'BMW', 100)
print('kecepatan sebelumnya: ', mobil1.kecepatan)
mobil1.tambah()
print('kecepatan setelahya: ', mobil1.kecepatan)


mobil2 = Mobil('Hitam', 'BMW', 150)
print('kecepatan sebelumnya: ', mobil2.kecepatan)
mobil2.tambah()
print('kecepatan setelahya: ', mobil2.kecepatan)


print('kecepatan sebelumnya: ', mobil1.kecepatan)
mobil1.tambah()
print('kecepatan setelahya: ', mobil1.kecepatan)