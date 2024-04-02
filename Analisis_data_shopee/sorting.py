import pandas as pd

x_umur = [12, 3, 6, 9, 10]
hasil = sorted(x_umur)
print(hasil)

x_nama= ["Doni", "Joni", "Kiki", "Sita", "Lala"]
hasil = sorted(x_nama)
print(hasil)

df = pd.DataFrame({
    'nama': x_nama,
    'umur': x_umur
})
print(df)

hasil = df.sort_values('nama', ascending=True)
print(hasil)