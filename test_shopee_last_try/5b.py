import pandas as pd

df1 = pd.read_csv('Analisis excel/test_shopee_last_try/Orders.csv')
df1['Order Date'] = pd.to_datetime(df1['Order Date'])
df2 = pd.read_csv('Analisis excel/test_shopee_last_try/Customer.csv')
df = pd.merge(df1, df2, on='Customer ID', how='inner')
# print(df)
filter = df1.groupby('Customer ID')['Order Date'].min().reset_index(name='tanggal_beli_pertama')
hasil_filter = pd.merge(df, filter, on='Customer ID', how='inner')
hasil_filter = hasil_filter[hasil_filter['Order Date'] == hasil_filter['tanggal_beli_pertama']].sort_values('Order Date', ascending=False).reset_index(drop=True)
# print(hasil_filter)

hasil = hasil_filter[['Customer ID', 'Sales']].sort_values('Customer ID', ascending=True).reset_index(drop=True)
print(hasil)

hasil = hasil_filter.groupby('Customer ID')['Sales'].unique().explode().reset_index().sort_values('Customer ID', ascending=True).reset_index(drop=True)
print(hasil)
# hasil2 = hasil_filter['Order ID'].value_counts()
# print(hasil2)