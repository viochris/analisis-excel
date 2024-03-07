from attr import has
import pandas as pd

df1 = pd.read_csv('Analisis excel/test_shopee_last_try/Orders.csv')
df1['Order Date'] = pd.to_datetime(df1['Order Date'])
df2 = pd.read_csv('Analisis excel/test_shopee_last_try/Customer.csv')
df = pd.merge(df1, df2, on='Customer ID', how='inner')
print(df)
filter = df1.groupby('Customer ID')['Order Date'].min().reset_index(name='tanggal_beli_pertama')
hasil_filter = df[df['Order Date'].isin(filter['tanggal_beli_pertama'])]

print()
hasil = hasil_filter.groupby(['City', 'Order Date'])['Customer ID'].count().reset_index(name='total_order').sort_values('total_order', ascending=False).reset_index(drop=True)
print(hasil)
hasil = hasil_filter.groupby(['City', 'Order Date'])['Customer ID'].nunique().reset_index(name='jumlah').sort_values('jumlah', ascending=False).reset_index(drop=True)
print(hasil)