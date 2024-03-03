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

class Mahasiswi(Manusia):
    def tua(self):
        self.usia += 2
        return self.usia

mahasiswi1 = Mahasiswi("Julia", 18)
mahasiswi1.sapa()
mahasiswi1.tua()
mahasiswi1.usia = 18
print(mahasiswi1.tua())
mahasiswi1.sapa()
print()