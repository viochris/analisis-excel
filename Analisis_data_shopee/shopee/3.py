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
df['order_date'] = pd.to_datetime(df['order_date'])
tabel2021 = df[df['order_date'].dt.year == 2021]
tabel2021 = tabel2021.groupby('category')['after_discount'].sum().round().reset_index(name='2021')
print(tabel2021)
tabel2022 = df[df['order_date'].dt.year == 2022]
tabel2022 = tabel2022.groupby('category')['after_discount'].sum().round().reset_index(name='2022')
print(tabel2022)
hasil = pd.merge(tabel2021, tabel2022, on='category', how='inner')
def pengurangan(x,y):
    return y -x
hasil['perbedaan'] = hasil.apply(lambda row: pengurangan(row['2021'], row['2022']), axis=1)
def Penjelasan(x):
    if x>0:
        return 'Naik'
    elif x<0:
        return 'Turun'
hasil['penjelasan'] = hasil['perbedaan'].apply(Penjelasan)
hasil = hasil.sort_values('perbedaan', ascending=False).reset_index(drop=True)
print(hasil)