import pandas as pd
from datetime import datetime

# Contoh DataFrame dengan kolom tanggal
data = {'tanggal': ['2024-01-15', '2024-02-20', '2024-03-25', '2024-01-30']}
df = pd.DataFrame(data)


# Mengonversi kolom 'tanggal' menjadi tipe data datetime
df['tanggal'] = pd.to_datetime(df['tanggal'])

df['format'] = df['tanggal'].dt.strftime('%y-%m')
print(df)

df['format1'] = df['tanggal'].dt.strftime('%Y-%m')
print(df)

df['format2'] = df['tanggal'].dt.to_period('M')
print(df)

df['year'] = df['tanggal'].dt.year
df['month'] = df['tanggal'].dt.month
df['day'] = df['tanggal'].dt.day

sekarang = datetime.now().date()
tanggal_sekarang = sekarang.strftime('%Y-%m-%d')
tanggal_sekarang = datetime.strptime(tanggal_sekarang, '%Y-%m-%d')
df['dif'] = tanggal_sekarang - df['tanggal']
print(df)


# ARGUMENT DARI STRPTIME HARUS STR
# sekarang = datetime.now()
# tanggal_sekarang = datetime.strptime(sekarang, '%Y-%m-%d')
# df['didf'] = tanggal_sekarang - df['tanggal']
# print(df)

hari = datetime(2024,2,20)
df['dif2'] = hari - df['tanggal']
print(df)

hari = pd.to_datetime('2024-02-20')
df['dif2'] = hari - df['tanggal']
print(df)

df['now'] = [datetime.now().date() for i in range(len(df))]
df['now'] = pd.to_datetime(df['now'])
df['dif3'] = df['now'] - df['tanggal']
print(df)

df['now'] = ['2024-02-20' for i in range(len(df))]
df['now'] = pd.to_datetime(df['now'])
df['dif4'] = df['now'] - df['tanggal']
print(df)

hasil = df[df['tanggal'].dt.strftime('%Y-%m') == '2024-01']
print(hasil)