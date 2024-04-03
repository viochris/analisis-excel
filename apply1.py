import pandas as pd

# Contoh DataFrame
data = {'Nama':['a','b','c'],'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Fungsi yang diaplikasikan pada setiap kolom
def double_column(x,y,z):
    return x * y*z

# Tampilkan DataFrame hasil
print("DataFrame setelah apply pada kolom:")
print(df)

df['total'] = df.apply(lambda col: double_column(col['A'], col['B'], col['C']), axis=1)
print(df)
df['total2'] = df.apply(lambda col: col['A'] * col['B'], axis=1)
df['total2a'] = df['A'] * df['B']
print(df)
df['total3'] = df.apply(lambda col: col['A'] *2, axis=1)
df['total3a'] = df['A'] *2
print(df)
def column(x):
    return x * 2
df['total4'] = df['A'].apply(column)
print(df)
df['total5'] = df.apply(lambda col: column(col['A']), axis = 1)
print(df)