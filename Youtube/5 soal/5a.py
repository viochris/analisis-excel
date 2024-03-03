import pandas as pd

df = pd.read_csv('Orders.csv')
# df = df.sort_values('Order ID')
df['Order Date'] = pd.to_datetime(df['Order Date'])
filter = df.groupby('Customer ID')['Order Date'].min().reset_index(name='pembelian pertama')


gabung = pd.merge(df, filter, on='Customer ID', how='inner')
gabung = gabung[gabung['Order Date'] == gabung['pembelian pertama']]

# ada duplikat 2 disini
hasil = gabung[['Customer ID', 'Sales']].sort_values('Customer ID', ascending=True).reset_index(drop=True)
print(hasil)
print()





# bukti
duplikat = gabung[gabung[['Customer ID', 'Sales']].duplicated() == True]
print(duplikat[['Customer ID', 'Sales']])
print()

print(hasil[(hasil['Customer ID'] == 'GM-14695') & (hasil['Sales'] == 22.960)])
print(hasil[(hasil['Customer ID'] == 'LB-16795') & (hasil['Sales'] == 281.372)])