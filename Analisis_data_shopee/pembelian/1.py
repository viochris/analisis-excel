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
# seleksi =  np.isnan(df['order_id'])
# print(df[seleksi])
print(df)


print(df.isna())
print(df.isna().sum())
print(df[df.notnull().all(axis=1)])
print(df[df.isna().any(axis=1)])
print(df[df.notnull().any(axis=1)])
print(df[df.isna().all(axis=1)])
print('\n\n\n')
print(df.loc[:,df.notnull().all(axis=0)])
print(df.loc[:,df.isna().any(axis=0)])
print(df.loc[:,df.notnull().any()])
print(df.loc[:, df.isna().all()])
print('\n\n\n')

print(df['order_id'].isna())
print(df[df['order_id'].isna()])
