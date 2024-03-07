import pandas as pd

df1 = pd.read_csv('Analisis excel/Youtube/5 soal/Orders.csv')
df1['Order Date'] = pd.to_datetime(df1['Order Date'])
df1 = df1.groupby('Customer ID')['Order Date'].min().reset_index(name='tanggal_beli_pertama')

df2 = pd.read_csv('Analisis excel/Youtube/5 soal/Customer.csv')
# df2 = df2.drop_duplicates()

hasil = pd.merge(df2, df1, on='Customer ID', how='inner').sort_values('tanggal_beli_pertama', ascending=False).reset_index(drop=True)
# print(hasil)
hasil1 = hasil.groupby(['City', 'tanggal_beli_pertama'])['Customer ID'].count().reset_index(name='jumlah').sort_values('jumlah', ascending=False).reset_index(drop=True)
print(hasil1)
hasil2 = hasil.groupby(['City', 'tanggal_beli_pertama'])['Customer ID'].nunique().reset_index(name='jumlah').sort_values('jumlah', ascending=False).reset_index(drop=True)
print(hasil2)