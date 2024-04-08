import pandas as pd
import numpy as np

# Membuat dataframe
data = {
    'Nama': ['Andi', 'Budi', 'Cindy', 'Deni', 'Andi'],
    'Kelas': ['A', 'B', 'A', 'C', 'C'],
    'Umur': [20, 22, 21, 23, 21]
}

df = pd.DataFrame(data)
print(df)

# Mengurutkan dataframe berdasarkan dua kolom secara berurutan
df_sorted = df.sort_values(by=['Kelas', 'Umur'])

# Menampilkan hasil
print(df_sorted)