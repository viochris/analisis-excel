import pandas as pd
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', user='root', password='', database='pembelian_shopee')
query1 = "SELECT*FROM order_detail"
query2 = "SELECT*FROM payment_detail"
query3 = "SELECT*FROM sku_detail"
df1 = pd.read_sql(query1, connection)
df2 = pd.read_sql(query2, connection)
df3 = pd.read_sql(query3, connection)
connection.close()

df = pd.merge(df1, df2, left_on='payment_id', right_on='id', how='inner')
df = df[df['is_valid'] == 1]
df['order_date'] = pd.to_datetime(df['order_date'])
df = df[df['order_date'].dt.year == 2022]
print(df)
hasil = df.groupby('payment_method')['id_x'].nunique().reset_index(name='total').sort_values('total', ascending=False).reset_index(drop=True)
top5_payment  = hasil.head(5)
print(top5_payment)
print('\n\n\n\n')

df2 = pd.merge(df, df3, left_on='sku_id', right_on='id', how='inner')
df2 = df2[df2['payment_method'].isin(top5_payment['payment_method'])]
print(df2)
hasil_akhir = df2.groupby(['category','payment_method'])['id_x'].nunique().reset_index(name='total').sort_values('category', ascending=True).reset_index(drop=True)
print(hasil_akhir)