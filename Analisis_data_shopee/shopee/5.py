import pandas as pd
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', user='root', password='', database='pembelian_shopee')
query1 = "SELECT*FROM order_detail"
query2 = "SELECT*FROM sku_detail"
df1 = pd.read_sql(query1, connection)
df2 = pd.read_sql(query2, connection)
connection.close()

df = pd.merge(df1, df2, left_on='sku_id', right_on='id', how='inner')
df = df[df['is_valid'] == 1]
# df['order_date'] = pd.to_datetime(df['order_date'])
# df = df[df['order_date'].dt.year == 2022]
print(df)

df['produk'] = np.select(
    [df['sku_name'].str.lower().str.contains('samsung'),
    df['sku_name'].str.lower().str.contains('apple')|df['sku_name'].str.lower().str.contains('iphone')|df['sku_name'].str.lower().str.contains('macbook'),
    df['sku_name'].str.lower().str.contains('sony'),
    df['sku_name'].str.lower().str.contains('huawei'),
    df['sku_name'].str.lower().str.contains('lenovo')
    ],
    ['Samsung', 'Apple', 'Sony', 'Huawei', 'Lenovo'],
    default='others'
)
df = df[df['produk'] != 'others']
print(df)
hasil = df.groupby('produk')['after_discount'].sum().round().reset_index(name='total').sort_values('total', ascending=False).reset_index(drop=True)
print(hasil)