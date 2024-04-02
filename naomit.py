import pandas as pd

# Membuat DataFrame contoh
data = {'A': [1, 2, None, 4],
        'B': [None, 5, 6, 7],
        'C': [8, 9, 10, 11]}
df = pd.DataFrame(data)

# Menghapus baris dengan nilai NaN (axis=0)
df_dropna_axis0 = df.dropna(axis=0)
print("DataFrame setelah menghapus baris dengan nilai NaN (axis=0):\n", df_dropna_axis0)

# Menghapus kolom dengan nilai NaN (axis=1)
df_dropna_axis1 = df.dropna(axis=1)
print("\nDataFrame setelah menghapus kolom dengan nilai NaN (axis=1):\n", df_dropna_axis1)
