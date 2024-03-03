import pandas as pd

# Buat DataFrame dengan indeks multi-level
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
}
index = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)], names=['first', 'second'])
df = pd.DataFrame(data, index=index)

# Tampilkan DataFrame awal
print("DataFrame awal:")
print(df)

# Gunakan unstack untuk mengubah indeks multi-level menjadi kolom
unstacked_df = df.unstack()

# Tampilkan DataFrame setelah menggunakan unstack
print("\nDataFrame setelah unstack:")
print(unstacked_df)
