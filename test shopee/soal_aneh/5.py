import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re


df_hotel = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
df_hotel = df_hotel.reset_index().rename(columns={'index': 'id'})
df = df_hotel[df_hotel['is_canceled'] == 0]
hasil = df.groupby(['hotel', 'arrival_date_month'])['is_canceled'].count().reset_index(name='jumlah').sort_values('hotel', ascending=False).reset_index(drop=True)
print(hasil)

df['arrival_date_month'] = df['arrival_date_month'].replace(('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'), (1,2,3,4,5,6,7,8,9,10,11,12))
hasil = df.groupby(['hotel', 'arrival_date_month'])['is_canceled'].count().reset_index(name='jumlah').sort_values('hotel', ascending=False).reset_index(drop=True)
print(hasil)

sns.countplot(data=df, x='arrival_date_month', hue='hotel')
plt.title('Jumlah Check-in per Bulan di Hotel A dan B')
plt.show()