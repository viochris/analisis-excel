import pandas as pd

df1 = pd.read_csv('Customer.csv')
df2 = pd.read_csv('Orders.csv')
# df2 = df2.sort_values('Order ID')
df2['Order Date'] = pd.to_datetime(df2['Order Date'])

df = pd.merge(df1, df2, on='Customer ID', how='inner')
filter = df.groupby('Customer ID')['Order Date'].min().reset_index(name='pembelian pertama')

gabung = pd.merge(df, filter, on='Customer ID', how='inner')
gabung = gabung[gabung['Order Date'] == gabung['pembelian pertama']]
# coba = gabung[gabung['Customer ID']== 'ZD-21925']
# print(coba[['Customer ID', 'Sales']])


# bebas duplikat
hasil = gabung.groupby('Customer ID')['Sales'].unique().explode().reset_index().sort_values('Customer ID', ascending=True).reset_index(drop=True)
print(hasil)



# bukti
duplikat = hasil[hasil[['Customer ID', 'Sales']].duplicated() == True]
print(duplikat[['Customer ID', 'Sales']])
print()

print(hasil[(hasil['Customer ID'] == 'GM-14695') & (hasil['Sales'] == 22.960)])
print(hasil[(hasil['Customer ID'] == 'LB-16795') & (hasil['Sales'] == 281.372)])