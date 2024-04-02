import pandas as pd
import datetime as dt
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_csv('bread basket.csv')

print(df)
print()
print(df.info())
print()
print(df.describe())
print()
df['date_time'] = pd.to_datetime(df['date_time'])
print(df.info())
print()
df['Month'] = df['date_time'].dt.month
df['Month'] = df['Month'].replace((1,2,3,4,5,6,7,8,9,10,11,12), ('jan','feb','march','apr','may','june','july','august','sept','okt','nov','dec'))
print(df)
print()
print(df['Item'].unique())
print()
print(df['period_day'].unique())
print()
print(df['weekday_weekend'].unique())
print()
tabel_awal = df.groupby(['Transaction', 'Item'])['Item'].count().reset_index(name='Total')
print(tabel_awal)
print()
tabel_pivot = pd.pivot_table(tabel_awal, values='Total', index='Transaction', columns='Item', aggfunc=sum).fillna(0)
print(tabel_pivot)
print()
def kosong(x):
    if x == 0:
        return False
    if x>0:
        return True
tabel_akhir = tabel_pivot.applymap(kosong)
print(tabel_akhir)
print()
tabel_apriori = apriori(tabel_akhir, min_support=0.015, use_colnames=True).sort_values('support', ascending=False).reset_index(drop=True)
print(tabel_apriori)
print()
hasil_akhir = association_rules(tabel_apriori, metric='confidence', min_threshold=0.5).sort_values('confidence', ascending=False).reset_index(drop=True)
print(hasil_akhir)
print()

hasil_akhir.to_excel('hasil akhir.xlsx', index=True)