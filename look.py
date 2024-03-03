import pandas as pd
from sqlite3 import connect
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

path_od = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/order_detail.csv"
path_pd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/payment_detail.csv"
path_cd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/customer_detail.csv"
path_sd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/sku_detail.csv"
df_od = pd.read_csv(path_od)
df_pd = pd.read_csv(path_pd)
df_cd = pd.read_csv(path_cd)
df_sd = pd.read_csv(path_sd)

connection = connect(":memory:")
df_od.to_sql('order_detail', connection, index=False, if_exists='replace')
df_pd.to_sql('payment_detail', connection, index=False, if_exists='replace')
df_cd.to_sql('customer_detail', connection, index=False, if_exists='replace')
df_sd.to_sql('sku_detail', connection, index=False, if_exists='replace')

query = """
SELECT 
    order_detail.*,
    payment_detail.payment_method,
    customer_detail.registered_date,
    sku_detail.sku_name,
    sku_detail.base_price,
    sku_detail.cogs,
    sku_detail.category
FROM 
    order_detail
LEFT JOIN payment_detail
    ON payment_detail.id = order_detail.payment_id
LEFT JOIN customer_detail
    ON customer_detail.id = order_detail.customer_id
LEFT JOIN sku_detail
    ON sku_detail.id = order_detail.sku_id
"""
df = pd.read_sql(query, connection)
connection.close()



df['order_date'] = pd.to_datetime(df['order_date'])
df['Tahun'] = df['order_date'].dt.year
df['Tahun_bulan'] = df['order_date'].dt.strftime('%Y-%m')
df['net_profit'] = df['before_discount'] - df['cogs'] * df['qty_ordered']



tahun_bulan_values = df['Tahun_bulan'].unique()
category_values = df['category'].unique()
payment_values = df['payment_method'].unique()
valid_values = df['is_valid'].unique()
tahun_values = df['Tahun'].unique()


st.title('Dashboard')
st.sidebar.header('Filters')
tahun_bulan_selected=st.sidebar.multiselect('Select an rentang waktu :',tahun_bulan_values, default=tahun_bulan_values)
category_selected=st.sidebar.multiselect('Select an kategory :',category_values, default=category_values)
payment_selected=st.sidebar.multiselect('Select an payment_method :',payment_values, default=payment_values)
valid_selected=st.sidebar.multiselect('Select an valid/not valid :',valid_values, default=valid_values)
tahun_selected=st.sidebar.multiselect('Select an valid/not valid :',tahun_values, default=tahun_values)




filtered_data = df[(df['is_valid'].isin(valid_selected)) & (df['category'].isin(category_selected)) & (df['Tahun_bulan'].isin(tahun_bulan_selected)) & (df['payment_method'].isin(payment_selected)) & (df['Tahun'].isin(tahun_selected))]


hasil = filtered_data.groupby('Tahun_bulan').agg({'after_discount': 'sum', 'net_profit': 'sum', 'before_discount': 'sum', 'id': 'nunique'}).reset_index()
hasil['AOV'] = hasil['before_discount']/hasil['id']
print(hasil)




if st.dataframe(hasil):
    # Data
    tahun_bulan = hasil['Tahun_bulan']
    mean_after_discount = hasil['after_discount']
    mean_net_profit = hasil['net_profit']
    mean_aov = hasil['AOV']

    # Menentukan lebar setiap batang
    bar_width = 0.35

    # Indeks untuk sumbu x
    x_index = np.arange(len(tahun_bulan))

    # Plot
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot bar untuk mean_after_discount
    rects1 = ax1.bar(x_index - bar_width/2, mean_after_discount, bar_width, label='Mean After Discount', color='skyblue')

    # Plot bar untuk mean_net_profit
    rects2 = ax1.bar(x_index + bar_width/2, mean_net_profit, bar_width, label='Mean Net Profit', color='lightgreen')

    # Atur label sumbu x
    ax1.set_xlabel('Tahun Bulan')
    ax1.set_ylabel('Nilai')
    ax1.set_title('Rata-rata After Discount dan Net Profit Berdasarkan Tahun Bulan')
    ax1.set_xticks(x_index)
    ax1.set_xticklabels(tahun_bulan, rotation=45)
    ax1.legend(loc='upper left')

    # Tambahkan sumbu kedua untuk AOV
    ax2 = ax1.twinx()
    ax2.plot(x_index, mean_aov, color='orange', marker='o', linestyle='-', linewidth=2, label='Mean AOV')
    ax2.set_ylabel('AOV')
    ax2.legend(loc='upper right')

    # plt.tight_layout()
    # plt.show()
    st.pyplot(fig)