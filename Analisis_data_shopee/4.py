import pandas as pd
from sqlite3 import connect
import numpy as np
import matplotlib.pyplot as plt

path_od = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/order_detail.csv"
path_pd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/payment_detail.csv"
path_cd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/customer_detail.csv"
path_sd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/sku_detail.csv"
df_od = pd.read_csv(path_od)
df_pd = pd.read_csv(path_pd)
df_cd = pd.read_csv(path_cd)
df_sd = pd.read_csv(path_sd)

df = df_od
df = df[df['is_valid'] == 1]
df['order_date'] = pd.to_datetime(df["order_date"])
df = df[df["order_date"].dt.year == 2022]
df = df[df["order_date"].dt.month.between(10,12)]
df['month'] = df["order_date"].dt.month.replace((10,11,12), ('oktober', 'november', 'desember'))
print(df)

tabel_days = df[df["order_date"].dt.day_of_week < 5]
tabel_days = tabel_days.groupby('month')['before_discount'].mean().round(2).reset_index(name='weekdays')
tabel_end = df[df["order_date"].dt.day_of_week >= 5]
tabel_end = tabel_end.groupby('month')['before_discount'].mean().round(2).reset_index(name='weekend')
tabel_mix = pd.merge(tabel_days, tabel_end, left_on='month', right_on='month', how='inner').sort_values('month', ascending=True).reset_index(drop=True)
def beda(x,y):
    return y-x
tabel_mix['Keuntungan/Kerugian'] = round(tabel_mix.apply(lambda x: beda(x['weekdays'], x['weekend']), axis=1), 2)
tabel_mix['Persentase'] = round(tabel_mix['Keuntungan/Kerugian'] / tabel_mix['weekend'] * 100, 2)
tabel_mix = tabel_mix.sort_values('month', ascending=False).reset_index(drop=True)
print(tabel_mix)

x = np.arange(len(tabel_mix['month']))
width = 0.25

plt.bar(x - width/2, tabel_mix['weekend'], width, label='weekend')
plt.bar(x + width/2, tabel_mix['weekdays'], width, label='weekdays')
plt.xticks(x, tabel_mix['month'])
plt.xlabel('Bulan')
plt.ylabel('Penjualan')
plt.title('Diagram Penjualan Weekdays vs Weekend In 2022')
plt.legend()
plt.grid()
plt.show()