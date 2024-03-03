import pandas as pd
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', user='root', password='', database='pembelian_shopee')
query = "SELECT*FROM order_detail"
df = pd.read_sql(query, connection)
connection.close()

print(df)
df = df[df['is_valid'] == 1]
df['order_date'] = pd.to_datetime(df['order_date'])
df = df[df['order_date'].dt.year == 10-2021]
df['month'] = df['order_date'].dt.month
hasil = df.groupby('order_date')['after_discount'].sum().round()
hasil2 = df.groupby('order_date')['customer_id'].count().round()
hasil_akhir = pd.merge(hasil, hasil2, on='order_date', how='inner')
hasil_akhir['ARPU'] = hasil_akhir['after_discount']/hasil_akhir['customer_id']
print(hasil_akhir)