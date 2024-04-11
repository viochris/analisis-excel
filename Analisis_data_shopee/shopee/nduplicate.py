import pandas as pd
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', user='root', password='', database='pembelian_shopee')
query = "SELECT*FROM order_detail"
df = pd.read_sql(query, connection)
connection.close()

print(df)

hasil = df.groupby('customer_id')['customer_id'].count().reset_index(name = 'jumlah').sort_values('jumlah', ascending = False).reset_index(drop=True)
print(hasil.head(6))