import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', user='root', password='', database='pembelian_shopee')
query1 = "SELECT*FROM order_detail"
query2 = "SELECT*FROM sku_detail"
df1 = pd.read_sql(query1, connection)
df2 = pd.read_sql(query2, connection)
connection.close()

df = pd.merge(df1, df2, left_on='sku_id', right_on='id', how='inner')
df = df[df['is_valid'] == 1]
df['order_date'] = pd.to_datetime(df['order_date'])
df = df[df['order_date'].dt.year == 2022]
print(df)
tabel1 = df.groupby(['sku_name', 'category'])[['after_discount', 'qty_ordered']].sum().reset_index()
print(tabel1)
tabel2 = df.groupby(['sku_name', 'category'])[['customer_id', 'id_x']].nunique().reset_index()
print(tabel2)

tabel_akhir = pd.merge(tabel1, tabel2, on=['sku_name', 'category'], how='inner')
tabel_akhir = tabel_akhir.sort_values('qty_ordered', ascending=False).reset_index(drop=True).head(10)
print(tabel_akhir)