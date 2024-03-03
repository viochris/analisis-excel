import pandas as pd

df = pd.read_csv('customer.csv')
df = df.groupby('City')['Customer ID'].nunique().reset_index(name='jumlah').sort_values('jumlah', ascending=False).reset_index(drop=True)
print(df)
