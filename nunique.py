import pandas as pd
import numpy as np

# Membuat DataFrame contoh
df = pd.DataFrame({
    'Nama': ["John", "Doe", "Jane", "Smith", "John", np.nan, "Bari", "Jan"],
    'Usia': [30, 25, 35, 40, 30, 34, np.nan, 35]
})

# Menghitung jumlah nilai duplikat di setiap kolom
hasil = df.apply(lambda x: x.duplicated().sum())
print(hasil)
print('\n\n')

# Menghitung jumlah nilai bukan duplikat di setiap kolom
print(df.nunique())
print('\n\n')

print(len(df['Nama'].dropna().unique()))
