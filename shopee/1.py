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
df = df[df['order_date'].dt.year == 2022]
df = df[df['category'] == 'Mobiles & Tablets']
print(df)

hasil = df.groupby('sku_name')['qty_ordered'].sum().reset_index(name='jumlah').sort_values('jumlah', ascending=False).reset_index(drop=True)
hasil = hasil.head(5)
print(hasil)

x = hasil['sku_name']
y = hasil['jumlah']

plt.barh(x,y, label='total_qty_ordered_in_2022')
plt.gca().invert_yaxis()
plt.xlabel('Jumlah')
plt.ylabel('Nama Barang')
plt.title('Top 5 Paling Dibeli')
plt.grid()
plt.legend()
plt.show()