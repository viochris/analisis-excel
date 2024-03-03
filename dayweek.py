from datetime import datetime
import pandas as pd
import locale
import sqlite3


ultah = datetime(2005, 4, 2)
day_week = ultah.weekday()
day_week_name = ultah.strftime('%A')
print(day_week)
print(day_week_name)

df = pd.DataFrame({
    'tanggal': ['2024-02-01', '2024-02-20', '2024-02-25', '2024-02-29', '2005-04-02', '2024-02-05'],
})
df['tanggal'] = pd.to_datetime(df['tanggal'])
df['day_week'] = df['tanggal'].dt.day_of_week
df['day_week_name'] = df['tanggal'].dt.day_name()
print(df)