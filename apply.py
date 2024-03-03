import pandas as pd

# # Contoh DataFrame
# data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
# df = pd.DataFrame(data)

# # Fungsi yang diaplikasikan pada setiap baris
# def sum_row(row):
#     return row.sum()

# # Menggunakan apply pada setiap baris (axis=1)
# df['Sum_Row'] = df.apply(sum_row, axis=1)

# # Tampilkan DataFrame hasil
# print("DataFrame setelah apply pada baris:")
# print(df)



# Contoh DataFrame
data = {'Nama':['a','b','c'],'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Fungsi yang diaplikasikan pada setiap kolom
def double_column(x,y,z):
    return x * y*z

# Menggunakan apply pada setiap kolom (axis=0)
# df['baru'] = df['A'].apply(double_column)

# Tampilkan DataFrame hasil
print("DataFrame setelah apply pada kolom:")
print(df)

df.loc[3] = df.apply(lambda col: double_column(col[0], col[1], col[2]), axis=0)
print(df)
# def column(x):
#     return x * 2
# df.loc[3] = df.loc[0].apply(column)
# print(df)