import pandas as pd

df = pd.read_excel('Tes Excel Shopee Data Analyst.xlsx', sheet_name='Test')
df = df.drop(index=range(15,23))
df = df.dropna(axis=1)
print(df)
df2 = pd.read_excel('Tes Excel Shopee Data Analyst.xlsx', sheet_name='Database')

tabel = pd.merge(df['Customer Code'],df2[['CUSTOMER CODE', 'CUSTOMER NAME', 'Tax' ,  'BOX QTY', 'TOTAL WEIGHT']],left_on='Customer Code', right_on='CUSTOMER CODE', how='inner')
tabel = tabel.drop(columns='CUSTOMER CODE')
print(tabel)

tabel1 = tabel.drop_duplicates('Customer Code')
print(tabel1)
print()
tabel2 = tabel.groupby('Customer Code')['BOX QTY'].sum().reset_index(name='BOX QTY')
tabel3 = tabel.groupby('Customer Code')['TOTAL WEIGHT'].sum().reset_index(name='TOTAL WEIGHT')
print(tabel2)
print(tabel3)

tabel_12 = pd.merge(tabel1[['Customer Code', 'CUSTOMER NAME', 'Tax']], tabel2, left_on='Customer Code', right_on='Customer Code', how='inner')
tabel_123 = pd.merge(tabel_12, tabel3, left_on='Customer Code', right_on='Customer Code', how='inner')
print(tabel_12)
print(tabel_123)


def harga1(Box):
    return Box*100000
tabel_123['Price Total Qty Box'] = tabel_123['BOX QTY'].apply(harga1)
def harga2(W):
    return W*1000000
tabel_123['Price Total Weight'] = tabel_123['TOTAL WEIGHT'].apply(harga2)
def tax(pjk):
    if pjk == 'PKP':
        return 0.10
    if pjk == 'PKTP':
        return 0.0
    else:
        return 0.0
tabel_123['Pajak'] = tabel_123['Tax'].apply(tax)
print(tabel_123)
def total(x,y,z):
    # x = tabel_123['Price Total Qty Box']
    # y = tabel_123['Price Total Weight']
    # z = tabel_123['Pajak']
    return x+y+((x+y)*z)
tabel_123['Total'] = total(tabel_123['Price Total Qty Box'], tabel_123['Price Total Weight'], tabel_123['Pajak'])
# tabel_123['Total'] = tabel_123.apply(lambda row:total(row['Price Total Qty Box'], row['Price Total Weight'], row['Pajak']), axis=1)
print(tabel_123)
tabel_123.to_excel('Data Shopee.xlsx', index=False)