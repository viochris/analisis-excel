import pandas as pd

df1 = pd.read_csv('Analisis excel/Youtube/5 soal/Customer.csv')
print(df1)
df1 = df1.groupby('City')['Customer ID'].unique().explode().reset_index()

df2 = pd.read_csv('Analisis excel/Youtube/5 soal/Orders.csv')
print(df2)
df = pd.merge(df1, df2, on='Customer ID', how='inner')
print(df.head())

hasil = df.groupby('City')['Order ID'].count().reset_index()
print(hasil)