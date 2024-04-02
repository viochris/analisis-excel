import pandas as pd

# Membuat DataFrame contoh
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Mengatur kolom 'A' sebagai indeks dan mengembalikan indeks menjadi kolom baru
df_reset = df.set_index('A').reset_index()
print(df_reset)
print()

# Membuat DataFrame dengan indeks multi-level
df_multi = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C' : [7,8,9]} )
df_multi.set_index(['A', 'B'], inplace=True)
print(df_multi)
print()
# Mengembalikan indeks multi-level menjadi kolom
df_reset_multi = df_multi.reset_index()
print(df_reset_multi)
print()

# Membuat DataFrame contoh
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

# Menggabungkan DataFrame dan mengatur indeks ulang
df_concat = pd.concat([df1, df2]).reset_index(drop=True)
print(df_concat)
print()

# Membuat DataFrame contoh
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# Mengatur indeks dan mengatur nama kolom setelah reset indeks
df_reset = df.set_index('A').reset_index().rename(columns={'A': 'New_A'})
print(df_reset)
