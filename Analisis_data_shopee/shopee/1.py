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
# df = df[df['order_date'].dt.year == 2021]
# df['month'] = df['order_date'].dt.month
df = df.query('order_date.dt.year == 2021')
df = df.assign(month = df['order_date'].dt.month)
hasil = df.groupby('month')['after_discount'].sum().round().reset_index(name='jumlah').sort_values('jumlah', ascending=False).reset_index(drop=True)
print(hasil)