import pandas as pd

df1 = pd.read_csv('Analisis excel/test_shopee_last_try/Orders.csv')
df1['Order Date'] = pd.to_datetime(df1['Order Date'])
df2 = pd.read_csv('Analisis excel/test_shopee_last_try/Customer.csv')
df = pd.merge(df1, df2, on='Customer ID', how='inner')
# print(df)
filter = df1.groupby('Customer ID')['Order Date'].min().reset_index(name='tanggal_beli_pertama')
hasil_filter = pd.merge(df, filter, on='Customer ID', how='inner')
hasil_filter = hasil_filter[hasil_filter['Order Date'] == hasil_filter['tanggal_beli_pertama']]
hasil_filter = hasil_filter.sort_values('Order Date', ascending=False).reset_index(drop=True)
# print(hasil_filter)

hasil = hasil_filter.groupby(['City', 'Order Date'])['Customer ID'].count().reset_index(name='jumlah').sort_values('jumlah', ascending=False).reset_index(drop=True)
print(hasil)
hasil = hasil_filter.groupby(['City', 'Order Date'])['Customer ID'].nunique().reset_index(name='jumlah').sort_values('jumlah', ascending=False).reset_index(drop=True)
print(hasil)
# lebih tepat digunakan untuk menghitung order id
# hasil = hasil_filter.groupby(['City', 'Order Date'])['Order ID'].count().reset_index(name='jumlah').sort_values('Order Date', ascending=True).reset_index(drop=True)
# print(hasil)



"""
code pertama = 4.py
code kedua = 4coba.py

baiklah, code kedua salah, karena semua data tidak masuk. 
Hal tersebut hanya dibandingkan dengan customer.csv saja. 
Padahal keduanya digabungkan dengan customer id, dan bisa saja jika di orders.csv 
ada 3 data sedangkan di customer.csv ada 2 data dengan customer id sama. 
Seharusnya dengan code 1, akan menyesuaikan dan hasil akhirnya adalah 3. 
data dengan customer id sama tapi isi pembelian berbeda. Tapi karena code 2 membandingkan 
langsung dengan customer.csv, hal ini menyebabkan kehilangan data.

tapi code kedua juga tidak salah, jika mencari pembelian pertama, 
code kedua tepat karena benar-benar murni pembelian pertama, tidak seperti 
code pertama yang memang data pembelian pertama tapi terdapat data pembelian 
barangnya pada hari itu juga, sehingga asalkan sesuai dengan filter pembelian pertama, 
entah barang yang dibeli beda atau sama, akan dijadikan satu. 

jadinya penggunaannya tergantung, jika ingin mencari data pembelian 
pertama dengan mempertimbangkan barang-barang yang dibeli lebih tepat code pertama, tapi jika mencari 
data pembelian pertama tanpa mempertimbangkan barang-barang yang dibeli, code kedua lebih tepat"""