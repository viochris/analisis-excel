import pandas as pd
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', user='root', password='', database='pembelian_shopee')
query = "SELECT*FROM order_detail"
df = pd.read_sql(query, connection)
connection.close()


df = df[df['is_valid'] == 1]
df['order_date'] = pd.to_datetime(df['order_date'])
df = df.query('order_date.dt.year == 2021')
df = df.assign(month = df['order_date'].dt.month)
print(df)

# This line of code is performing the following operations:
hasil = df.groupby('month')['after_discount'].sum().round().reset_index(name = 'total').sort_values('total', ascending=False).reset_index(drop=True)
print(hasil)