import pandas as pd
import datetime as dt
import streamlit as st
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_csv('bread basket.csv')
df['date_time'] = pd.to_datetime(df['date_time'])
df['month'] = df['date_time'].dt.month.replace((1,2,3,4,5,6,7,8,9,10,11,12), ('jan','feb','march','apr','may','june','july','august','sept','okt','nov','dec'))
print(df)

item = df['Item'].unique()
day = df['period_day'].unique()
week = df['weekday_weekend'].unique()
bulan = df['month'].unique()

st.title('Sistem Rekomendasi Produk')
st.sidebar.header('Combo Filter')
selected_item = st.sidebar.selectbox('Select an item:',item)
# selected_day = st.sidebar.selectbox('Select day',day)
# selected_week = st.sidebar.selectbox('Select weekend/weekday',week)
# selected_month = st.sidebar.selectbox('Select month',bulan)

awal = df.groupby(['Transaction', 'Item'])['Item'].count().reset_index(name='jumlah')
pivot = pd.pivot_table(awal,index='Transaction', columns='Item', values='jumlah', aggfunc=sum).fillna(0)
def hot_encode(x):
    if x == 0:
        return False
    if x > 0:
        return True
pivot_akhir = pivot.applymap(hot_encode)
tabel_apr = apriori(pivot_akhir, min_support=0.0015, use_colnames=True)
tabel_asscosiasi = association_rules(tabel_apr, metric="confidence", min_threshold=0.3).sort_values('confidence',ascending=False).reset_index(drop=True)
tabel_asscosiasi['antecedents'] = tabel_asscosiasi['antecedents'].apply(lambda x: list(x))
tabel_asscosiasi['consequents'] = tabel_asscosiasi['consequents'].apply(lambda x: list(x))

tabel_asscosiasi_perubahan = tabel_asscosiasi[
    (tabel_asscosiasi['antecedents'].apply(lambda x: selected_item in x)) | 
    (tabel_asscosiasi['consequents'].apply(lambda x: selected_item in x))
]
if not tabel_asscosiasi_perubahan.empty:
    tabel_asscosiasi_perubahan = tabel_asscosiasi_perubahan.iloc[0]
    st.success(f'Hasil Rekomendasi {selected_item}')
    st.write(tabel_asscosiasi_perubahan[['antecedents', 'consequents']])
else:
    st.subheader(f'{selected_item} Not Found')