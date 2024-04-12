import pandas as pd


nama = "John"
umur = 30
pesan = "Nama: {}, Umur: {}".format(nama, umur)
print(pesan)
print()

pesan = 'Nama: "{}", Umur: "{}"'.format(nama, umur)
print(pesan)
print()

pesan = f'Nama: "{nama}", Umur: "{umur}"'
print(pesan)
print()


df = pd.DataFrame({
    'Nama': ['"John"', '"Niko"', '"Vio"', '"Gayus"']
})
print(df)
print()

df['Nama tanpa "'] = df['Nama'].str.replace('"', '').str.strip()
print(df)