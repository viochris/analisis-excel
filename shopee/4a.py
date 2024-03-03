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
weekday = weekday['before_discount'].mean()
weekend = df[df['order_date'].dt.day_of_week >= 5]
weekend = weekend['before_discount'].mean()
data = {
    'Total' : ['Total 3 bulan'],
    'weekday':[round(weekday, 2)],
    'weekend':[round(weekend, 2)],
    'perubahan': [round(weekend - weekday, 2)],
    'persentase': [round((weekend - weekday)/weekend*100, 2)]
}
df = pd.DataFrame(data)
print(df)