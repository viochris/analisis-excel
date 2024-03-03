import pandas as pd
import datetime


# Contoh DataFrame dengan kolom 'tanggal_lahir'
data = {'nama': ['John', 'Alice', 'Bob'],
        'tanggal_lahir': ['1990-05-10', '1985-12-25', '1995-08-15']}
df = pd.DataFrame(data)
print(df)

df['tanggal_lahir'] = pd.to_datetime(df['tanggal_lahir'])
df['tahun-bulan'] = df['tanggal_lahir'].dt.to_period('M')
print(df)
df = df[df['tahun-bulan'].between('1990-05', '1995-08', inclusive='both')]
# df = df[(df['tahun-bulan'] > '1990-05') & (df['tahun-bulan'] <= '1995-08')]
print(df)

