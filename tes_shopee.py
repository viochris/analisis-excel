import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

df = pd.read_excel('Tes Excel Shopee Data Analyst.xlsx', sheet_name='Test', usecols='B')
df_asal = pd.read_excel('Tes Excel Shopee Data Analyst.xlsx', sheet_name='Database', usecols='B:I')
df = df.dropna()
df = df.drop(range(16,23))
print(df)
tabel1 = pd.merge(df,df_asal[['CUSTOMER CODE', 'CUSTOMER NAME', 'Tax']], left_on='Customer Code', right_on='CUSTOMER CODE', how='inner')
tabel1 = tabel1.drop_duplicates('Customer Code')
tabel1 = tabel1.drop('CUSTOMER CODE', axis=1)
print(tabel1)

tabel2 = pd.merge(df['Customer Code'],df_asal[['CUSTOMER CODE', 'BOX QTY', 'TOTAL WEIGHT']], left_on='Customer Code', right_on='CUSTOMER CODE', how='inner')
tabel2 = tabel2.groupby('Customer Code')[['BOX QTY', 'TOTAL WEIGHT']].sum().reset_index()
print(tabel2)
df = pd.merge(tabel1, tabel2, on='Customer Code', how='inner')
print(df)

def totalQTY(x):
    return x*100000
df['Price QTY'] = df['BOX QTY'].apply(totalQTY)
def totalW(x):
    return x*1000000
df['Price Weight'] = df['TOTAL WEIGHT'].apply(totalW)
def tax(x):
    if x == 'PKP':
        return 0.1
    elif x == 'PTKP':
        return 0 
    else: return  0
df['Pajak'] = df['Tax'].apply(tax) 
def total(x,y,z):
    hasil = x+y+((x+y)*z)
    return hasil
df['Hasil Akhir'] = df.apply(lambda row:total(row['Price QTY'], row['Price Weight'], row['Pajak']), axis=1 )
print(df)


pivot = pd.pivot_table(df_asal, index=['AREA', 'CUSTOMER NAME'], values=['BOX QTY', 'TOTAL WEIGHT'], aggfunc=sum, margins=True, margins_name='total').sort_values('AREA')
print(pivot)