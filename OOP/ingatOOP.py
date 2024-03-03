import pandas as pd

class Makanan:
    rasa = "Manis"
    warna = 'Merah'
print(Makanan.rasa)
print()


class Manusia:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia
        
    def ultah(self):
        self.usia += 1
        return self.usia
        
    def sapa(self):
        print(f"Halo, nama saya {self.nama} dan saya berusia {self.usia} tahun.")

saya = Manusia('John', 30)
saya.sapa()
saya.ultah() #jika hanya ingin menjalankan fungsi penambahan umur
saya.usia = 30
print(saya.ultah()) #jika ingin menunjukkan hasil returnnya
saya.sapa()
print()




# Inheritance (Pewarisan)
class Mahasiswa(Manusia):
    def __init__(self, nama, usia, jurusan):
        super().__init__(nama, usia)
        self.jurusan = jurusan
    
    def belajar(self):
        print(f"{self.nama} sedang belajar di jurusan {self.jurusan}.")

mahasiswa1 = Mahasiswa("Alice", 20, "Informatika")
mahasiswa1.sapa()
mahasiswa1.belajar()
mahasiswa1.ultah()
mahasiswa1.usia = 20
print(mahasiswa1.ultah())
mahasiswa1.sapa()
mahasiswa1.belajar()
print()


class Mahasiswa(Manusia):
    def belajar(self):
        print(f"{self.nama} sedang belajar di usia {self.usia}.")

mahasiswa1 = Mahasiswa("Alice", 24)
mahasiswa1.sapa()
mahasiswa1.belajar()
mahasiswa1.ultah()
mahasiswa1.usia = 24
print(mahasiswa1.ultah())
mahasiswa1.sapa()
mahasiswa1.belajar()
print()



# Encapsulation (Enkapsulasi)
# class Karyawan:
#     def __init__(self, gaji):
#         self.__gaji = gaji
    
#     def get_gaji(self):
#         return self.__gaji
    
#     def tunjukkan_gaji(self):
#         print(f'gajiku {self.__gaji}')
    
#     def set_gaji(self, gaji_baru):
#         if gaji_baru > 0:
#             self.__gaji = gaji_baru

# karyawan1 = Karyawan(3000)
# karyawan1.tunjukkan_gaji()
# print(karyawan1.get_gaji())

# karyawan1.set_gaji(6000)
# karyawan1.tunjukkan_gaji()
# print(karyawan1.get_gaji())

# karyawan1.set_gaji(1000)
# karyawan1.tunjukkan_gaji()
# print(karyawan1.get_gaji())

class Karyawan:
    def __init__(self):
        self.__gaji = 5000
    
    def get_gaji(self):
        return self.__gaji
    
    def tunjukkan_gaji(self):
        print(f'gajiku {self.__gaji}')
    
    def set_gaji(self, gaji_baru):
        if gaji_baru > 0:
            self.__gaji = gaji_baru

karyawan1 = Karyawan()
karyawan1.__gaji= 200 #tidak bisa dilakukan karena __ artinya private
print(vars(karyawan1))
karyawan1.tunjukkan_gaji()
print(karyawan1.get_gaji())

karyawan1.set_gaji(6000)
karyawan1.tunjukkan_gaji()
print(karyawan1.get_gaji())

karyawan1.set_gaji(1000)
karyawan1.tunjukkan_gaji()
print(karyawan1.get_gaji())



# class Hewan:
#     def kucing(self):
#         print("Meow!")
        
#     def anjing(self):
#         print("Woof! Woof!")

# kewan = Hewan()
# kewan.kucing()
# kewan.anjing()
# print()


# class Harimau():
#     def bersuara(self):
#         print("Meow!")
# harimau = Harimau()
# harimau.bersuara()

# class Asu():
#     def bersuara(self):
#         print("woof!")
# asu = Asu()
# asu.bersuara()

print()

# Polymorphism (Polimorfisme)
class Binatang:
    def bersuara(self):
        pass

class Kucing(Binatang):
    def bersuara(self):
        print("Meow!")
        
class Anjing(Binatang):
    def bersuara(self):
        print('Woof! Woof!')


print('cara 1')       
kucing = Kucing()
anjing = Anjing()
kucing.bersuara()
anjing.bersuara()

print('cara 2')
def main():
    binatang = [Kucing(), Anjing()]
    for hewan in binatang:
        hewan.bersuara()
main()
print()


# penggunaan OOP untuk df
class Proses:
    def __init__(self, df):
        self.df = df
    def tambah(self):
        self.df['new_column'] = self.df['old_column'] * 2
        return self.df


data = {'old_column': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
print(df)

proses = Proses(df)
proses.tambah()
print(df)

df['neest olumn'] = df['old_column'] * 2
print(df)