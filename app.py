import pandas as pd
import datetime as dt
import streamlit as st
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df=pd.read_csv('bread basket.csv')
df['date_time'] = pd.to_datetime(df['date_time'])
df['month'] = df['date_time'].dt.month.replace((1,2,3,4,5,6,7,8,9,10,11,12),('jan','feb','march','apr','may','june','july','august','sept','okt','nov','dec'))

item_unik = df['Item'].unique()
month = df['month'].unique()
day = df['period_day'].unique()
week = df['weekday_weekend'].unique()

st.title('Sistem Rekomendasi Produk')
st.sidebar.header('Filters')
selected_item=st.sidebar.selectbox('Select an item :',item_unik)
selected_period=st.sidebar.selectbox('Select an month :',month)
selected_day=st.sidebar.selectbox('Select an day :',day)
selected_week=st.sidebar.selectbox('Select an weekend/weekday :',week)

transactions=df.groupby(['Transaction','Item'])['Item'].count().reset_index(name='Total')
table=pd.pivot_table(transactions,index='Transaction',columns='Item',values='Total',aggfunc='sum').fillna(0)

def hot_encode(x):
    if x==0:
        return False
    if x>0:
        return True

final_table=table.applymap(hot_encode)
frequence=apriori(final_table,min_support=0.0015,use_colnames=True)

product_association = association_rules(frequence,metric='confidence',min_threshold=0.3).sort_values('confidence',ascending=False).reset_index(drop=True)
product_association['antecedents'] = product_association['antecedents'].apply(lambda x: list(x))
product_association['consequents'] = product_association['consequents'].apply(list)
print(product_association)

selected_item_rules = product_association[
    (product_association['antecedents'].apply(lambda x: selected_item in x)) |
    # (product_association['consequents'].isin([selected_item]))
    # (product_association['consequents'] == selected_item)
    (product_association['consequents'].apply(lambda x: selected_item in x))
    ]

print(selected_item_rules)

if not selected_item_rules.empty:
    selected_item_rules=selected_item_rules.iloc[0]
    st.success(f'Hasil Rekomendasi {selected_item}')
    st.write(selected_item_rules[['antecedents', 'consequents']])
else:
    st.subheader(f'No rules found with the selected criteria for {selected_item}.')