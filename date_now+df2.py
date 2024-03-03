import pandas as pd
from datetime import datetime


# Contoh DataFrame dengan kolom 'tanggal_lahir'
data = {'nama': ['John', 'Alice', 'Bob'],
        'tanggal_lahir': ['1990-05-10', '1985-12-25', '1995-08-15']}
df = pd.DataFrame(data)

# Mengonversi kolom 'tanggal_lahir' ke tipe datetime
df['tanggal_lahir'] = pd.to_datetime(df['tanggal_lahir'])

# Menghitung usia berdasarkan tahun kelahiran
today = datetime(2024, 1, 1)  # Anggap saja kita sedang berada di tahun 2024
df['usia'] = today.year - df['tanggal_lahir'].dt.year
print(df)

hari_ini = datetime.now()
df['usia1'] = hari_ini.year - df['tanggal_lahir'].dt.year
print(df)


df['usia2'] = 2024 - df['tanggal_lahir'].dt.year
print(df)