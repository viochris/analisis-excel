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
df['profit'] = df['after_discount'] - (df['cogs']*df['qty_ordered'])
print(df)

tabel2021 = df[df['order_date'].dt.year == 2021]
tabel2021 = tabel2021.groupby('category')['profit'].sum().round().reset_index(name='2021')
print(tabel2021)
tabel2022 = df[df['order_date'].dt.year == 2022]
tabel2022 = tabel2022.groupby('category')['profit'].sum().round().reset_index(name='2022')
print(tabel2022)
tabelakhir = pd.merge(tabel2021, tabel2022, on='category', how='inner')
tabelakhir['%'] = ((tabelakhir['2022'] - tabelakhir['2021'])/tabelakhir['2021'])*100
tabelakhir = tabelakhir.sort_values("%", ascending=False).reset_index(drop=True)
print(tabelakhir)
