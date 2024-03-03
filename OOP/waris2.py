class Mobil:
    def __init__(self, warna, merek, kecepatan, harga):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
        self.harga = harga
    
    def tambah_kecepatan(self):
        self.kecepatan += 10
        self.harga += 1000000


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    # def tambah_kecepatan(self):
    #     self.kecepatan +=10
    #     print("Kecepatan Anda meningkat! Hati-Hati!")
    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan Anda meningkat! Hati-Hati!")

# Kelas Mobil Dasar
mobil_1 = Mobil("Merah", "DicodingCar", 160, 1000000)
print(mobil_1.kecepatan)
print(mobil_1.harga)
mobil_1.tambah_kecepatan()
print(mobil_1.kecepatan)
print(mobil_1.harga)
print()

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160, 1000000)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()
print(mobil_sport_1.kecepatan)
print(mobil_sport_1.harga)