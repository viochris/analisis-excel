import pandas as pd
from sqlite3 import connect
import matplotlib.pyplot as plt
import numpy as np

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
df['order_date'] = pd.to_datetime(df['order_date'])
df = df[df['order_date'].dt.year == 2022]
df = df[df['order_date'].dt.month.between(10,12)]
df['month'] = df['order_date'].dt.month.replace((10,11,12), ('oktober', 'november', 'desember'))
print(df)

weekday = df[df['order_date'].dt.day_of_week < 5]
weekday = weekday.groupby('month')['before_discount'].mean().round(2).reset_index(name='weekday')
weekend = df[df['order_date'].dt.day_of_week >= 5]
weekend = weekend.groupby('month')['before_discount'].mean().round(2).reset_index(name='weekend')
df1 = pd.merge(weekday, weekend, on='month', how='inner')
def perubahan(x,y):
    return y-x
df1['perubahan'] = df1.apply(lambda x:perubahan(x['weekday'], x['weekend']), axis=1)
def persentase(x,y):
    return ((y-x)/y)*100
df1['persentase'] = df1.apply(lambda x:persentase(x['weekday'], x['weekend']), axis=1)
print(df1)

x = np.arange(len(df1['month']))
width = 0.25

plt.bar(x - width/2, df1['weekend'], width, label='weekend')
plt.bar(x + width/2, df1['weekday'], width, label='weekdays')
plt.xticks(x, df1['month'])
plt.xlabel('Bulan')
plt.ylabel('Penjualan')
plt.title('Diagram Penjualan Weekdays vs Weekend In 2022')
plt.legend()
plt.grid()
plt.show()