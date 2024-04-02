from pickle import TRUE
import pandas as pd
import numpy as np
from sympy import true

# Membuat DataFrame contoh
df = pd.DataFrame({
    'Nama': ["John", "Doe", "Jane", "Smith", "John", np.nan, "Bari", "Jan"],
    'Usia': [30, 25, 35, 40, 30, 34, np.nan, 35]
})

print(len(df))
print(df.shape)
print(df.shape[0])
print(df.shape[1])

print('\n\n\n')

print(df.count())
print(df.value_counts())
print(df[['Nama', 'Usia']].value_counts())
print(df.value_counts(normalize=True))


hasil = df[['Nama', 'Usia']].value_counts(normalize=True)
print(hasil)


print(hasil.values.sum().round())