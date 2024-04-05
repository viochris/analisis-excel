import pandas as pd

df = pd.read_excel('Tes Excel Admin Klinik 2.xlsx', usecols='C:G', skiprows=1, names=['Nama Pasien', 'Kelas', 'Persalinan', 'Tanggal Masuk', 'Tanggal Keluar'])
df = df.dropna()
df= df.drop(index=range(9,12))
df['Tanggal Masuk'] = pd.to_datetime(df['Tanggal Masuk'])
df['Tanggal Keluar'] = pd.to_datetime(df['Tanggal Keluar'])
df['Lama inap'] = df['Tanggal Keluar'].dt.day - df['Tanggal Masuk'].dt.day
def inap(x,y):
    if x == 'BPJS':
        return 300000*y
    if x == 'Umum':
        return 900000*y
df['Inap'] = df.apply(lambda row:inap(row['Kelas'], row['Lama inap']), axis=1)
def layanan(x,y):
    if x == 'BPJS':
        return 150000*y
    if x == 'Umum':
        return 300000*y
df['Layanan'] = df.apply(lambda row:layanan(row['Kelas'], row['Lama inap']), axis=1)
def persalinan(x,y):
    if x == 'BPJS':
        if y == 'Dokter':
            return 1000000
        if y == 'Bidan':
            return 500000
    if x == 'Umum':
        if y == 'Dokter':
            return 1500000
        if y == 'Bidan':
            return 700000
df['Biaya Persalinan'] = df.apply(lambda row:persalinan(row['Kelas'], row['Persalinan']), axis=1)
# def persalinan2(x,y):
#     if x == 'BPJS' and y == 'Dokter':
#         return 1000000
#     if x == 'BPJS'  and y == 'Bidan':
#         return 500000
#     if x == 'Umum' and y == 'Dokter':
#         return 1500000
#     if x == 'Umum' and  y == 'Bidan':
#         return 700000
# df['Biaya Persalinan2'] = df.apply(lambda row:persalinan2(row['Kelas'], row['Persalinan']), axis=1)
df['Total Biaya'] = df[['Inap', 'Layanan', 'Biaya Persalinan']].sum(axis=1)
print(df)

hasil = sum(df['Total Biaya'])
print(f'Total Bayar: {hasil}')
hasil = df['Total Biaya'].mean()
hasil = round(hasil, 2)
print(f'Total Bayar: {hasil}')
sisa = max(df['Total Biaya'])
print(f'Biaya Tertinggi: {sisa}')
sisa = min(df['Total Biaya'])
print(f'Biaya Terendah: {sisa}')

tabel_akhir1 = df.groupby('Kelas')['Kelas'].count().reset_index(name='Jumlah Pasien')
tabel_akhir2 = df.groupby('Kelas')['Total Biaya'].sum().reset_index(name='Jumlah Pasien')
tabel = pd.merge(tabel_akhir1, tabel_akhir2, left_on='Kelas', right_on='Kelas', how='inner')
tabel = tabel.set_index('Kelas')
print(tabel)