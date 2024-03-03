import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', user='root', password='', database='pembelian_shopee')
query1 = "SELECT*FROM order_detail"
df = pd.read_sql(query1, connection)
connection.close()

df = df[df['is_valid'] == 1]
df['order_date'] = pd.to_datetime(df['order_date'])
df = df[df['order_date'].dt.year == 2021]
df['month'] = df['order_date'].dt.month 
print(df)

tabel1 = df.groupby('month')['qty_ordered'].sum().reset_index(name='kuantitas')
tabel2 = df.groupby('month')[['customer_id', 'id']].nunique().reset_index()
tabel = pd.merge(tabel1, tabel2, on='month', how='inner')
tabel = tabel.sort_values('kuantitas', ascending=False).reset_index(drop=True)
print(tabel)