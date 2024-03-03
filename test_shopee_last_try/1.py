import pandas as pd

df = pd.read_csv('Customer.csv')


hasil1 = df.groupby('City')['Customer Name'].nunique().reset_index()
hasil2 = df.groupby('City')['Customer ID'].nunique().reset_index()
print(hasil1)
print(hasil2)