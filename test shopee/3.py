import pandas as pd
df = pd.read_csv('order.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])
print(df[['Customer ID', 'Order Date']])
df = df.groupby('Customer ID')['Order Date'].min().reset_index(name='Tanggal').sort_values('Tanggal', ascending=True).reset_index(drop=True)
print(df)