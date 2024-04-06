import pandas as pd

df = pd.read_csv('test_shopee_all/Customer.csv') #, names = ['customer_id', 'name', 'segment', 'city', 'state'], header = 1)
print(df.head(5))
# df.columns = ['customer_id', 'name', 'segment', 'city', 'state']
# print(df.head())

hasil = df.groupby('City')['Customer ID'].nunique().reset_index(name='jumlah').sort_values('jumlah', ascending=False).reset_index(drop=True)
print(hasil)