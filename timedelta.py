import pandas as pd
from datetime import date

# Membuat DataFrame contoh
data = {
    'date_column': ['2023-01-01', '2022-03-15', '2022-06-10', '2021-12-25', '2020-10-05']
}
df = pd.DataFrame(data)

# Konversi kolom 'date_column' ke datetime
df['date_column'] = pd.to_datetime(df['date_column'])

# Tanggal hari ini
today_date = pd.to_datetime(date.today().strftime('%Y-%m-%d'))

# Menghitung jumlah bulan sejak tanggal dalam kolom hingga hari ini
df['mths_since_date_column'] = round(pd.to_numeric((today_date - df['date_column']).dt.days / 30))

print((today_date - df['date_column']).dt.days)
# Menghapus kolom 'date_column'
# df.drop(columns=['date_column'], inplace=True)
df = df.drop('date_column', axis=1)

print(df)
