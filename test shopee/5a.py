from pickle import TRUE
import pandas as pd
df = pd.read_csv('order.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df = df.sort_values('Order ID')

pembelian1 = df.groupby('Customer ID')['Order Date'].min().reset_index(name='Tanggal').sort_values('Tanggal', ascending=True).reset_index(drop=True)
# CARA MEMFILTER YANG BENAR SEHINGGA TANGGAL PEMBELIAN PERTAMA YANG SAMA DENGAN TANGGAL PEMBELIAN BIASANYA DAPAT TERFILTER
hasil = pd.merge(df, pembelian1, on='Customer ID', how='inner')
hasil = hasil[hasil['Order Date'] == hasil['Tanggal']]
hasil = hasil[['Customer ID', 'Sales', 'Order ID', 'Order Date']].sort_values('Customer ID').reset_index(drop=True)
print(hasil)
# hasil = hasil.sort_values('Sales', ascending=False)
# hasil = hasil.groupby('Customer ID')['Sales'].first().reset_index(name='Total Sales').sort_values('Customer ID', ascending=True).reset_index(drop=True)
# print(hasil)

duplikat = hasil[hasil[['Customer ID', 'Sales']].duplicated() == True]
print(duplikat)
print()

print(hasil[(hasil['Customer ID'] == 'GM-14695') & (hasil['Sales'] == 22.960)])
print(hasil[(hasil['Customer ID'] == 'LB-16795') & (hasil['Sales'] == 281.372)])

