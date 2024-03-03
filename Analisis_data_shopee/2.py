import pandas as pd
from sqlite3 import connect
import matplotlib.pyplot as plt

path_od = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/order_detail.csv"
path_pd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/payment_detail.csv"
path_cd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/customer_detail.csv"
path_sd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/sku_detail.csv"
df_od = pd.read_csv(path_od)
df_pd = pd.read_csv(path_pd)
df_cd = pd.read_csv(path_cd)
df_sd = pd.read_csv(path_sd)

df = pd.merge(df_od, df_sd, left_on='sku_id', right_on='id', how="inner")
print('Data ke-15 Kategor1')
df['order_date'] = pd.to_datetime(df['order_date'])
df['after_discount'] = df['after_discount'].round()
df = df[df['is_valid']==1]
tabel21 = df[df['order_date'].dt.year == 2021]
tabel21 = tabel21.groupby('category')['qty_ordered'].sum().reset_index(name='jumlah2021')
tabel22 = df[df['order_date'].dt.year == 2022]
tabel22 = tabel22.groupby('category')['qty_ordered'].sum().reset_index(name='jumlah2022')
tabel_akhir = pd.merge(tabel21, tabel22, left_on='category', right_on='category', how='inner')
def pengurangan(x,y):
    return y -x
tabel_akhir['Perbedaan'] = tabel_akhir.apply(lambda row: pengurangan(row['jumlah2021'], row['jumlah2022']), axis=1)
def Penjelasan(x):
    if x>0:
        return 'Naik'
    elif x<0:
        return 'Turun'
tabel_akhir['Penjelasan'] = tabel_akhir['Perbedaan'].apply(Penjelasan)
tabel_akhir = tabel_akhir.sort_values('Perbedaan', ascending=True).reset_index(drop=True)
print(tabel_akhir)
print()
print()
print('Data kategori others')
df = df[df['category']=='Others']
tabel_2021 = df[df['order_date'].dt.year == 2021]
tabel_2021 = tabel_2021.groupby('sku_name')['qty_ordered'].sum().reset_index(name='Jumlah 2021')
# print(tabel_2021)
tabel_2022 = df[df['order_date'].dt.year == 2022]
tabel_2022 = tabel_2022.groupby('sku_name')['qty_ordered'].sum().reset_index(name='Jumlah 2022')
# print(tabel_2022)
tabel_akhir = pd.merge(tabel_2021, tabel_2022, left_on='sku_name', right_on='sku_name', how='outer').fillna(0)
# print(tabel_akhir)
tabel_akhir['Perbedaan'] = tabel_akhir.apply(lambda row: pengurangan(row['Jumlah 2021'], row['Jumlah 2022']), axis=1)
tabel_akhir['Penjelasan'] = tabel_akhir['Perbedaan'].apply(Penjelasan)
tabel_akhir = tabel_akhir.sort_values('Perbedaan', ascending=True).reset_index(drop=True)
print(tabel_akhir.head(20))