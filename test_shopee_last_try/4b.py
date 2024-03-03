from attr import has
import pandas as pd

df1 = pd.read_csv('Orders.csv')
df1['Order Date'] = pd.to_datetime(df1['Order Date'])
df2 = pd.read_csv('Customer.csv')
df = pd.merge(df1, df2, on='Customer ID', how='inner')
print(df)
filter = df1.groupby('Customer ID')['Order Date'].min().reset_index(name='tanggal_beli_pertama')
hasil_filter = df[df['Order Date'].isin(filter['tanggal_beli_pertama'])]

hasil = hasil_filter.groupby(['City', 'Order Date'])['Customer ID'].count().reset_index(name='total_order').sort_values('Order Date').reset_index(drop=True)
print(hasil)