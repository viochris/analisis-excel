import pandas as pd

df = pd.read_csv('test_shopee_all/Orders.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])

filter = df.groupby('Customer ID')['Order Date'].min().reset_index(name = 'pembelian_pertama').sort_values('Customer ID', ascending=True).reset_index(drop=True)

print(df)
print(filter)

hasil = pd.merge(df, filter, on = 'Customer ID')
hasil = hasil[hasil['Order Date'] == hasil['pembelian_pertama']]
print(hasil)
print('\n\n\n')

hasil = hasil[['Customer ID', 'Sales']].sort_values('Customer ID', ascending=True).reset_index(drop=True)
print(hasil)