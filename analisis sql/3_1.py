import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', user='root', password='', database='pembelian')
sql1 = """
SELECT 
    c.*,
    s.*,
    o.*
FROM
    customers c
LEFT JOIN orders o ON
    c.customer_id = o.customer_id
LEFT JOIN salesman s ON 
    o.salesman_id = s.salesman_id;

"""
df = pd.read_sql(sql1, connection)
connection.close()
print(df)
df = df.groupby('customer_name')['salesman_name'].count().reset_index(name='jumlah').sort_values('jumlah', ascending=False).reset_index(drop=True)
print(df)
