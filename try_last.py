import pandas as pd
import datetime as dt
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('bread basket.csv')

print(df)
print()
print(df.info())
print()
print(df.describe())
print()
df['date_time'] = pd.to_datetime(df['date_time'])
df['Month'] = df['date_time'].dt.month
df['Month'] = df['Month'].replace((1,2,3,4,5,6,7,8,9,10,11,12), ('jan','feb','march','apr','may','june','july','august','sept','okt','nov','dec'))
print(df)
print(df['Item'].unique())
print(df['period_day'].unique())
print(df['weekday_weekend'].unique())
tabel_baru = df.groupby(['Transaction', 'Item'])['Item'].count().reset_index(name='Jumlah')
print(tabel_baru)
tabel_pivot = pd.pivot_table(tabel_baru, values='Jumlah', index='Transaction', columns='Item', aggfunc='sum').fillna(0)
print(tabel_pivot)
def kosong(x):
    if x == 0:
        return False
    if x > 0:
        return True
tabel_pivot = tabel_pivot.applymap(kosong)
print(tabel_pivot)
tabel_apriori = apriori(tabel_pivot, min_support=0.015, use_colnames=True)
print(tabel_apriori)
tabel_akhir = association_rules(tabel_apriori, metric='confidence', min_threshold=0.5).sort_values('confidence', ascending=False).reset_index(drop=True)
print(tabel_akhir)

