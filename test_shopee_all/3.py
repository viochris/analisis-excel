import pandas as pd

df = pd.read_csv('test_shopee_all/Orders.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])
print(df)

hasil = df.groupby('Customer ID')['Order Date'].min().reset_index(name = 'pembelian_pertama').sort_values('Customer ID', ascending=True).reset_index(drop=True)
print(hasil)