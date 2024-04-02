import pandas as pd
import numpy as np


# Membuat DataFrame contoh
df = pd.DataFrame({
    'Nama': ["John", "Doe", "Jane", "Smith", "John", np.nan, "Bari", "Jan"],
    'Usia': [30, 25, 35, 40, 30, 34, np.nan, 35]
})
print(df)
print('\n\n')

print('nama-nama')
print(df.index)
print(df.columns)
print(df.values)


# print('Data tambahan')
# tabel = df['Nama'].value_counts()
# print(tabel)

# hasil = df['Nama'].value_counts(normalize=True)
# print(hasil)

# print(tabel.index)
# print()
# print(tabel.values)
# print()
# print(hasil.index)
# print()
# print(hasil.values)
# print()
# print(hasil.values.sum().round())


# print('\n\n\n\n\n')

# print(df.value_counts())
# print(df[['Nama', 'Usia']].value_counts())


# tabel = df.value_counts(normalize=True)
# print(tabel)

# hasil = df[['Nama', 'Usia']].value_counts(normalize=True)
# print(hasil)



# print(tabel.index)
# print()
# print(tabel.values)
# print()
# print(hasil.index)
# print()
# print(hasil.values)
# print()
# print(hasil.values.sum().round())