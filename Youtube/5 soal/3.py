import pandas as pd


df = pd.read_csv('Analisis excel/Youtube/5 soal/Orders.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])
print(df)

hasil = df.groupby('Customer ID')['Order Date'].min().reset_index(name='pembelian pertama')
print(hasil)