import pandas as pd

# Buat DataFrame contoh
data = {'A': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Cek apakah nilai kolom 'A' tidak ada dalam daftar [2, 4, 6]
result = df[~df['A'].isin([2, 4, 6])]
# Tampilkan hasil
print(result)
