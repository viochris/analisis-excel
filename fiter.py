from email.policy import default
import pandas as pd
from sqlite3 import connect
import matplotlib.pyplot as plt
import streamlit as st

path_od = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/order_detail.csv"
path_pd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/payment_detail.csv"
path_cd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/customer_detail.csv"
path_sd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/sku_detail.csv"
df_od = pd.read_csv(path_od)
df_pd = pd.read_csv(path_pd)
df_cd = pd.read_csv(path_cd)
df_sd = pd.read_csv(path_sd)

df = pd.merge(df_od, df_sd[['id', 'sku_name', 'category']], left_on='sku_id', right_on='id', how="inner")
df['order_date'] = pd.to_datetime(df['order_date'])
df['tahun'] = df['order_date'].dt.year
df['bulan'] = df['order_date'].dt.month
valid_or_Not = df['is_valid'].unique()
category = df['category'].unique()
tahun = df['tahun'].unique()
bulan = df['bulan'].unique()

st.title('Filter Kategori')
st.sidebar.header('Filter')
valid = st.sidebar.multiselect('Valid/ Tidak', valid_or_Not, default=valid_or_Not)
kategori = st.sidebar.multiselect('Kategori', category, default=category)
tahun = st.sidebar.multiselect('Tahun', tahun, default=tahun)
bulan = st.sidebar.multiselect('Bulan', bulan, default=bulan)

# apply dan in tidak bisa digunakan untuk int. Dan apply in ini lebih baik digunakan untuk list dimana ada dua data dalam satu kolom
# filtered_data = df[(df['is_valid'] == valid) & (df['category'].apply(lambda x: kategori in x)) & (df['order_date'].dt.year == tahun)]
# filtered_data = df[(df['is_valid'] == valid) & (df['category'].apply(lambda x: any(item in x for item in kategori))) & (df['order_date'].dt.year == tahun)]
# filtered_data = df[(df['is_valid'] == valid) & (df['category'].isin(kategori)) & (df['tahun'] == tahun)]
filtered_data = df[(df['is_valid'].isin(valid)) & (df['category'].isin(kategori)) & (df['tahun'].isin(tahun)) & (df['bulan'].isin(bulan))]

tabel_akhir = filtered_data.groupby('sku_name')['qty_ordered'].sum().reset_index(name='jumlah').sort_values('jumlah', ascending=False).reset_index(drop=True)
tabel_5 = tabel_akhir.head(5)
print(tabel_5)

tabel_akhir2 = filtered_data.groupby('tahun')['qty_ordered'].sum().reset_index(name='jumlah').sort_values('jumlah', ascending=True).reset_index(drop=True)
print(tabel_akhir2)


tabel_akhir3 = filtered_data.groupby('bulan')['qty_ordered'].sum().reset_index(name='jumlah').sort_values('bulan', ascending=True).reset_index(drop=True)
print(tabel_akhir3)

# if st.dataframe(tabel_5):
if st.dataframe(tabel_5):
    fig, ax = plt.subplots()
    ax.barh(tabel_5['sku_name'], tabel_5['jumlah'], label=f'total_qty_ordered_in_{tahun}')
    ax.set_xlabel('Total Order')
    ax.set_ylabel('SKU Name')
    ax.set_title(f'{tahun} Top 5 Ordered')
    ax.legend(loc='lower right')
    ax.grid(axis='x')
    ax.invert_yaxis()  # Invert y-axis to have the highest quantity at the top

        # Menampilkan plot pertama menggunakan Streamlit
    st.pyplot(fig)
    
    
    # Plot untuk tabel_akhir2
    fig2, ax2 = plt.subplots()
    ax2.bar(tabel_akhir2.index, tabel_akhir2['jumlah'], label='Total Qty Ordered')
    ax2.set_xticks(range(len(tabel_akhir2)))
    ax2.set_xticklabels(tabel_akhir2['tahun'])
    ax2.set_xlabel('Tahun')
    ax2.set_ylabel('Total Order')
    ax2.set_title('Total Qty Ordered Over Time')
    ax2.legend(loc='upper left')
    ax2.grid(True)

    # Menampilkan plot menggunakan Streamlit
    st.write("Plot untuk Tabel Akhir 2:")
    st.pyplot(fig2)


    # Plot untuk tabel_akhir3
    fig3, ax3 = plt.subplots()
    ax3.bar(range(len(tabel_akhir3)), tabel_akhir3['jumlah'], label='Total Qty Ordered')
    ax3.set_xlabel('Bulan')
    ax3.set_ylabel('Total Order')
    ax3.set_title('Total Qty Ordered Over Time')
    ax3.legend(loc='upper left')
    ax3.grid(True)

    # Mengatur nilai xticks agar sesuai dengan bulan-bulan yang tersedia
    ax3.set_xticks(range(len(tabel_akhir3)))
    ax3.set_xticklabels(tabel_akhir3['bulan'], rotation=45)

    # Menampilkan plot menggunakan Streamlit
    st.write("Plot untuk Tabel Akhir 3:")
    st.pyplot(fig3)

