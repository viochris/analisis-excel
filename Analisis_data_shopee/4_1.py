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
print(df)

tabel_days = df[df["order_date"].dt.day_of_week < 5]
tabel_days = tabel_days['before_discount'].mean().round(2)
tabel_end = df[df["order_date"].dt.day_of_week >= 5]
tabel_end = tabel_end['before_discount'].mean().round(2)


data = {
    'Total': ['Total 3 Bulan'],
    'weekdays': [tabel_days],
    'weekend': [tabel_end],
    'Keuntungan/kerugian': [tabel_end - tabel_days],
    'Persentase': [round((tabel_end - tabel_days) / tabel_end * 100, 2)]
}
df = pd.DataFrame(data)
print(df)

