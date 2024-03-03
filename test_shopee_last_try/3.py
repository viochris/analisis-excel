import pandas as pd
df1 = pd.read_csv('Orders.csv')
df1['Order Date'] = pd.to_datetime(df1['Order Date'])
df2 = pd.read_csv('Customer.csv')
df = pd.merge(df1, df2, on='Customer ID', how='inner')
print(df)

hasil = df.groupby('Customer ID')['Order Date'].min().reset_index()
print(hasil)




df = pd.read_csv('Orders.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])
hasil = df.groupby('Customer ID')['Order Date'].min().reset_index()
print(hasil)