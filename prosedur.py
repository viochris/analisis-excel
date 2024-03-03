import pandas as pd

def greeting(name):
    print("Halo " + name + ", Selamat Datang!")
greeting("Dicoding Indonesia")

def greeting():
    print("Halo Selamat Datang!")
greeting()


# Hanya bisa mengembalikan 1 nilai
df = pd.DataFrame({
    'nilai': [100, 80, 90, 87, 76, 80]
})
def nilai(x):
    if x > 90 & x <=100:
        return "A"
        return 'Pintar'
    elif x > 80 & x <= 90:
        return "B"
    elif x > 70 & x <= 80:
        return "C"
    elif x > 60 & x <= 70:
        return "D"
    else:
        return "E"
df['huruf'] = df['nilai'].apply(nilai)
print(df)
print()

# bisa mengembalikan 2 nilai
def keterangan(x):
    return 'bagus'
df['ket'] = df['huruf'].apply(keterangan)
print(df)