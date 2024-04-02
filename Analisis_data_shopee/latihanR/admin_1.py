import pandas as pd

df = pd.read_excel('Tes Excel Admin Klinik.xlsx', skiprows=3, nrows=5, usecols="C:G", names=['Nama Pasien', 'Kelas', 'Penanganan', 'Tanggal Masuk', 'Tanggal Keluar'])
# df = df.dropna()
print(df)

# df['Tanggal Masuk'] = pd.to_datetime(df['Tanggal Masuk'])
# df['Tanggal Keluar'] = pd.to_datetime(df['Tanggal Keluar'])
# df['Lama Tinggal'] = df['Tanggal Keluar'].dt.day - df['Tanggal Masuk'].dt.day
# def inap(x,y):
#     if x == 'A':
#         return 300000*y
#     if x == 'B':
#         return 200000*y
#     if x == 'C':
#         return 100000*y
# df['Inap'] = df.apply(lambda row: inap(row['Kelas'], row['Lama Tinggal']), axis=1)
# print(df)
# def layanan(x,y):
#     if x == 'A':
#         return 150000*y
#     if x == 'B':
#         return 100000*y
#     if x == 'C':
#         return 50000*y
# df['Layanan'] = df.apply(lambda row: layanan(row['Kelas'], row['Lama Tinggal']), axis=1)
# def persalinan(x):
#     if x == 'Dokter':
#         return 200000
#     if x == 'Bidan':
#         return 100000
# df['Persalinan'] = df['Penanganan'].apply(persalinan)
# df['Total Biaya'] = df[['Inap', 'Layanan', 'Persalinan']].sum(axis=1)
# print(df)


# total = sum(df['Total Biaya'])
# print(f'Total Bayar: {total}')
# total = max(df['Total Biaya'])
# print(f'Biaya Tertinggi: {total}')
# total = min(df['Total Biaya'])
# print(f'Biaya Terendah: {total}')
# tabel1 = df.groupby('Kelas')['Kelas'].count().reset_index(name='Jumlah Pasien')
# tabel2 = df.groupby('Kelas')['Total Biaya'].sum().reset_index(name='Jumlah Biaya')
# tabel_akhir = pd.merge(tabel1, tabel2, left_on='Kelas', right_on='Kelas', how='inner')
# print(tabel_akhir)
# tabel_akhir = tabel_akhir.set_index('Kelas')
# print(tabel_akhir)