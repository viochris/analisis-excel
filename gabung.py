import pandas as pd

# Contoh DataFrame pertama
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

# Contoh DataFrame kedua
df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Age': [25, 30, 22]
})

# 1. concat (menggabungkan berdasarkan indeks)
concatenated_df = pd.concat([df1, df2], axis=1)
print("Concatenated DataFrame:")
print(concatenated_df)
print()

# 2. join (menggabungkan berdasarkan indeks)
joined_df = df1.set_index('ID').join(df2.set_index('ID'), how='inner')
print("Joined DataFrame:")
print(joined_df)
print()

# 3. merge (menggabungkan berdasarkan kolom ID)
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print("Merged DataFrame:")
print(merged_df)


# tabel_akhir = df.loc[:,'Minggu1':'Minggu4'].join(df.loc[:,'Jumlah':'Total'])