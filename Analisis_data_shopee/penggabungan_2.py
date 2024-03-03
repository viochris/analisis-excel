import pandas as pd
from sqlite3 import connect

path_od = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/order_detail.csv"
path_pd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/payment_detail.csv"
path_cd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/customer_detail.csv"
path_sd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/sku_detail.csv"
df_od = pd.read_csv(path_od)
df_pd = pd.read_csv(path_pd)
df_cd = pd.read_csv(path_cd)
df_sd = pd.read_csv(path_sd)


df = pd.merge(df_od, df_pd, left_on='payment_id', right_on='id', how="inner")
print(df)
df = pd.merge(df, df_cd, left_on='customer_id', right_on='id', how="inner")
print(df)
df = pd.merge(df, df_sd, left_on='sku_id', right_on='id', how="inner")
print(df)
