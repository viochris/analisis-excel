import pandas as pd
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', user='root', password='', database='pembelian')
sql1 = "SELECT * FROM orders"
sql2 = "SELECT * FROM customers"
df1 = pd.read_sql(sql1, connection)
df2 = pd.read_sql(sql2, connection)

df = pd.merge(df1, df2, on='customer_id', how='outer')
print(df)
hasil = df.groupby('customer_name')['order_id'].count().reset_index(name='jumlah').sort_values('jumlah', ascending=False).reset_index(drop=True)
print(hasil)