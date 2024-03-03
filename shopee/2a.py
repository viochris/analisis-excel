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
df['year'] = df['order_date'].dt.year

tabel = df.groupby(['category', 'year'])['qty_ordered'].sum().unstack()


def perubahan(x,y):
    return y-x
tabel['Perubahan'] = tabel.apply(lambda row: perubahan(row[2021], row[2022]), axis=1)

def keterangan(x):
    if x > 0:
        return 'Naik'
    elif x < 0:
        return 'Turun'
tabel['Keterangan'] = tabel['Perubahan'].apply(keterangan)
tabel = tabel.sort_values('Perubahan', ascending=False)
print(tabel)
print()


print('TOP 20 Produk Mengalami Penurunan')
df = df[df['category'].str.lower() == 'others']
tabel_akhir = df.groupby(['sku_name', 'year'])['qty_ordered'].sum().unstack().fillna(0)
tabel_akhir['Perubahan'] = tabel_akhir.apply(lambda row: perubahan(row[2021], row[2022]), axis=1)
tabel_akhir['Keterangan'] = tabel_akhir['Perubahan'].apply(keterangan)
tabel_akhir = tabel_akhir.sort_values('Perubahan', ascending=True)
print(tabel_akhir.head(20))

tabel_akhir.to_excel('Top 20.xlsx', index=True)