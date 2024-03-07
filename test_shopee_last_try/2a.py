import pandas as pd

df1 = pd.read_csv('Analisis excel/Youtube/5 soal/Customer.csv')
df1 = df1.drop_duplicates(('City','Customer ID'))
df1 = df1.drop_duplicates(['City','Customer ID'])
df1 = df1.drop_duplicates(subset =['City','Customer ID'])

df2 = pd.read_csv('Analisis excel/Youtube/5 soal/Orders.csv')



df = pd.merge(df1, df2, on='Customer ID', how='inner')
print(df.head())


hasil = df.groupby('City')['Order ID'].count().reset_index(name='jumlah pembelian')
print(hasil)
