import pandas as pd

def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))

# bisa
# tidak bisa pakai a=, b=
def penjumlahan(a, b, /):
    return a + b
print(penjumlahan(8, 50))

# tidak bisa:
# def penjumlahan(a, b,/):
#     return a + b
# print(penjumlahan(a=8, b=50))
# dan seharusnya:
# def penjumlahan(a, b, /):
#     return a + b
# print(penjumlahan(8, 50))

def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan
print(greeting(pesan="Selamat sore!",nama="Dicoding"))
# harus pakai a=, b=
# tidak bisa:
# def greeting(*, nama, pesan):
#     return "Halo, " + nama + "! " + pesan
# print(greeting("Selamat sore!","Dicoding"))
# dan seharusnya:
# def greeting(*, nama, pesan):
#     return "Halo, " + nama + "! " + pesan
# print(greeting(pesan="Selamat sore!",nama="Dicoding"))

def hitung_total(*a):
    print(type(a))
    total = sum(a)
    return total

print(hitung_total(1, 2, 3))

# df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
# def hitung_total(*args):
#     print(type(args))
#     total = sum(args)
#     return total

# print(hitung_total(df['a'], df['b']))
# lebih baik yang ini:
# hasil = df['a'] + df['b']
# print(hasil)

def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))


mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang(5,10))


# global
a = 10
def add(b):
    result = a+b
    return result

bilanganPertama = add(20)
print(bilanganPertama)


# lokal
def add(a, b):
    lokal_var = 5
    result = a+b-lokal_var
    return result

bilanganPertama = add(10,20)
print(bilanganPertama)

def minimal(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else: return a
print(minimal(10,10))


df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': ['A', 'B', 'C'],
})

def kali(a, c = 2):
    return a*c
df['d'] = df['a'].apply(kali)
print(df)