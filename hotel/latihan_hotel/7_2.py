import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
df = df[df['is_canceled'] == 0]
df['arrival_date'] = pd.to_datetime(df['arrival_date_year'].astype(str) + '-' + df['arrival_date_month'].astype(str) + '-' + df['arrival_date_day_of_month'].astype(str))
df_reservasi_perhari = df.groupby('arrival_date')['is_canceled'].count().reset_index()
print(df_reservasi_perhari)
df_avg_reservasi_harian = df_reservasi_perhari.groupby(pd.Grouper(key='arrival_date', freq='W'))['is_canceled'].mean().reset_index()
print(df_avg_reservasi_harian)

plt.figure(figsize=(10, 4))
sns.lineplot(data=df_avg_reservasi_harian, x='arrival_date', y='is_canceled')
plt.title("Jumlah Reservasi per Hari")
plt.xlabel("Tanggal Tiba")
plt.ylabel("Jumlah Reservasi")
plt.show()