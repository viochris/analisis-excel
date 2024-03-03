import pandas as pd

df = pd.read_csv('Customer.csv')
print(df)

hasil = df.groupby('City')['Customer ID'].nunique().reset_index(name='Jumlah Customer per City')
print(hasil)