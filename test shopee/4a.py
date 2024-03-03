import pandas as pd

df1 = pd.read_csv('customer.csv')
df2 = pd.read_csv('order.csv')

df = pd.merge(df1, df2, on='Customer ID')
df['Order Date'] = pd.to_datetime(df['Order Date'])
tanggal_pertama = df.groupby('Customer ID')['Order Date'].min().reset_index(name='Tanggal').sort_values('Customer ID', ascending=True).reset_index(drop=True)
df= df[df['Order Date'].isin(tanggal_pertama['Tanggal'])]
print(df)
hasil = df.groupby(['City', 'Order Date'])['Customer ID'].count().reset_index(name='jumlah').sort_values('Order Date', ascending=True).reset_index(drop=True)
print(hasil)