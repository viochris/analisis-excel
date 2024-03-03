import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', user='root', password='', database='pembelian')
sql = "SELECT * FROM salesman"
df = pd.read_sql(sql, connection)
connection.close()

print(df)
df = df[['salesman_name', 'commision']]
df = df.sort_values('commision', ascending=False).reset_index(drop=True)
print(df.head(1))