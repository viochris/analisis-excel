import pandas as pd

df = pd.read_excel('Tes Excel Shopee Data Analyst.xlsx', sheet_name='Database')
tabel_group = df.groupby(['AREA','CUSTOMER NAME'])[['BOX QTY', 'TOTAL WEIGHT']].sum().reset_index().sort_values('AREA', ascending=True)
print(tabel_group)
tabel =  pd.pivot_table(df, index=['AREA', 'CUSTOMER NAME'], values=['BOX QTY', 'TOTAL WEIGHT'], aggfunc=sum).sort_values('AREA', ascending=True)
print(tabel)