import pandas as pd

# Membuat DataFrame contoh
df = pd.DataFrame({'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})
print(df)
print()

# Menampilkan nama kolom dan nama baris
print(df.columns)
print(df.index)
print()

# Menghitung jumlah, rata-rata, nilai maksimum, nilai minimum, dan median pada setiap baris
row_sums = df.sum(axis=1)
print("Row Sums:")
print(row_sums)

row_means = df.mean(axis=1)
print("Row Means:")
print(row_means)

row_maxs = df.max(axis=1)
print("Row Maximums:")
print(row_maxs)

row_mins = df.min(axis=1)
print("Row Minimums:")
print(row_mins)

row_medians = df.median(axis=1)
print("Row Medians:")
print(row_medians)
print()

# Menghitung nilai maksimum, nilai minimum, dan median pada setiap kolom
col_maxs = df.max()
print("Column Maximums:")
print(col_maxs)

col_mins = df.min()
print("Column Minimums:")
print(col_mins)

col_medians = df.median()
print("Column Medians:")
print(col_medians)
print()

# Menampilkan jumlah baris, jumlah kolom, dan dimensi DataFrame
num_rows = len(df)
print("Number of Rows:", num_rows)

num_cols = len(df.columns)
print("Number of Columns:", num_cols)

dim_df = df.shape
print("Dimensions of DataFrame:", dim_df)
print()

# Menampilkan nama kolom dan nama baris menggunakan index
dim_df = df.index
print("Row Names:")
print(dim_df)

dim_df = df.columns
print("Column Names:")
print(dim_df)
print()

# Menampilkan tipe data setiap kolom
print("Data Types of Columns:")
print(df.dtypes)
