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

df = pd.merge(df_od, df_cd, left_on='customer_id', right_on='id', how="inner")
df = df[df['is_gross'] == 1]
df = df[df['is_valid'] == 0]
df = df[df['is_net'] == 0]
df['order_date'] = pd.to_datetime(df['order_date'])
df = df[df['order_date'].dt.year == 2022]
df = df.drop_duplicates('customer_id')
df = df[['customer_id', 'registered_date']].reset_index(drop=True)
print(df)