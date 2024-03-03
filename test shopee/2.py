import pandas as pd

df1 = pd.read_csv('customer.csv')
df2 = pd.read_csv('order.csv')

df = pd.merge(df1, df2, on='Customer ID')
df = df.groupby('City')['Order ID'].count().reset_index(name='jumlah').sort_values('jumlah', ascending=False).reset_index(drop=True)
print(df)