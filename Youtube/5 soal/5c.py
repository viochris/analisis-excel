import pandas as pd

df1 = pd.read_csv('Customer.csv')
df2 = pd.read_csv('Orders.csv')
# df2 = df2.sort_values('Order ID')
df2['Order Date'] = pd.to_datetime(df2['Order Date'])

df = pd.merge(df1, df2, on='Customer ID', how='inner')
filter = df.groupby('Customer ID')['Order Date'].min().reset_index(name='pembelian pertama')

gabung = pd.merge(df, filter, on='Customer ID', how='inner')
gabung = gabung[gabung['Order Date'] == gabung['pembelian pertama']]
coba = gabung[gabung['Customer ID']== 'AA-10375']
# print(coba[['Customer ID', 'Sales']])

gabung = gabung.sort_values('Sales', ascending=False)
hasil = gabung.groupby('Customer ID')['Sales'].first().reset_index().sort_values('Customer ID', ascending=True).reset_index(drop=True)
print(hasil)