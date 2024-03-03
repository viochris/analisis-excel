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
df = df[df['is_valid'] == 1]
df['order_date'] = pd.to_datetime(df['order_date'])

tabel2021 = df[df['order_date'].dt.year == 2021]
tabel2021 = tabel2021.groupby('category')['qty_ordered'].sum().reset_index(name='jumlah2021').sort_values('jumlah2021', ascending=False).reset_index(drop=True)
# print(tabel2021)
tabel2022 = df[df['order_date'].dt.year == 2022]
tabel2022 = tabel2022.groupby('category')['qty_ordered'].sum().reset_index(name='jumlah2022').sort_values('jumlah2022', ascending=False).reset_index(drop=True)
# print(tabel2022)
df1 = pd.merge(tabel2021, tabel2022, on='category', how='inner')
# print(df1)

def perubahan(x,y):
    return y-x
df1['Perubahan'] = df1.apply(lambda row: perubahan(row['jumlah2021'], row['jumlah2022']), axis=1)
df1 = df1.sort_values('Perubahan', ascending=False).reset_index(drop=True)
def keterangan(x):
    if x > 0:
        return 'Naik'
    elif x < 0:
        return 'Turun'
df1['Keterangan'] = df1['Perubahan'].apply(keterangan)
print(df1)


print('TOP 20 Produk Mengalami Penurunan')
df = df[df['category'].str.lower() == 'others']
tabel2021 = df[df['order_date'].dt.year == 2021]
tabel2021 = tabel2021.groupby('sku_name')['qty_ordered'].sum().reset_index(name='jumlah2021').sort_values('jumlah2021', ascending=False).reset_index(drop=True)
print(tabel2021)
tabel2022 = df[df['order_date'].dt.year == 2022]
tabel2022 = tabel2022.groupby('sku_name')['qty_ordered'].sum().reset_index(name='jumlah2022').sort_values('jumlah2022', ascending=False).reset_index(drop=True)
print(tabel2022)
tabel_akhir = pd.merge(tabel2021, tabel2022, on='sku_name', how='outer').fillna(0)
tabel_akhir['Perubahan'] = tabel_akhir.apply(lambda row: perubahan(row['jumlah2021'], row['jumlah2022']), axis=1)
tabel_akhir = tabel_akhir.sort_values('Perubahan', ascending=True).reset_index(drop=True)
tabel_akhir['Keterangan'] = tabel_akhir['Perubahan'].apply(keterangan)
print(tabel_akhir.head(20))