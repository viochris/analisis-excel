import pandas as pd

df1 = pd.read_csv('Customer.csv')
df2 = pd.read_csv('Orders.csv')
df2['Order Date'] = pd.to_datetime(df2['Order Date'])

df = pd.merge(df1, df2, on='Customer ID', how='inner')
filter = df.groupby('Customer ID')['Order Date'].min().reset_index(name='pembelian pertama')

hasil_filter = df[df['Order Date'].isin(filter['pembelian pertama'])]
print(hasil_filter)

hasil = hasil_filter.groupby(['City', 'Order Date'])['Customer ID'].count().reset_index(name='Jumlah').sort_values('Order Date', ascending=True).reset_index(drop=True)
print(hasil)


