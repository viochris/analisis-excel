class Mobil:
    warna = "Merah"

mobil1 = Mobil()
print(mobil1.warna)

mobil2 = Mobil()
mobil2.warna = 'hitam'
print(mobil2.warna)



print(mobil1.warna)
print(mobil2.warna)

Mobil.warna = 'biru'
print(mobil1.warna)
print(mobil2.warna)