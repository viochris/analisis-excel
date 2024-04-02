import pandas as pd

# Membuat DataFrame contoh
data = {'Nama': ['John', 'Doe', 'Jane', 'Smith'],
        'Usia': [30, 25, 35, 40]}
df = pd.DataFrame(data)

# Memeriksa apakah nilai di kolom 'Nama' dimulai dengan 'J'
starts_with_J = df['Nama'].str.lower().str.startswith('j')

# Memeriksa apakah nilai di kolom 'Nama' diakhiri dengan 'e'
ends_with_e = df['Nama'].str.lower().str.endswith('e')

print("Baris yang dimulai dengan 'J':")
print(df[starts_with_J])

print("\nBaris yang diakhiri dengan 'e':")
print(df[ends_with_e])

print('\n\n')

print("Baris yang tidak dimulai dengan 'J':")
print(df[~starts_with_J])

print("\nBaris yang tidak diakhiri dengan 'e':")
print(df[~ends_with_e])
