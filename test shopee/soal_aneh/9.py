from operator import le
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re


df_hotel = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
df_hotel = df_hotel.reset_index().rename(columns={'index': 'id'})
df_hotel = df_hotel[df_hotel['is_canceled'] == 0]
df_hotel['arrival_date'] = pd.to_datetime(df_hotel['arrival_date_year'].astype(str) + '-' + df_hotel['arrival_date_month'].astype(str) + '-' + df_hotel['arrival_date_day_of_month'].astype(str))

df_country = pd.read_csv('https://gist.githubusercontent.com/tadast/8827699/raw/f5cac3d42d16b78348610fc4ec301e9234f82821/countries_codes_and_coordinates.csv')
df_country['country'] = df_country['Alpha-3 code'].str.replace('"', '').str.strip()
print(df_country)

df = pd.merge(df_hotel, df_country, on='country', how='inner')
print(df)

hasil = df.groupby('Country')['is_canceled'].count().reset_index(name='Total_reserved').sort_values('Total_reserved', ascending=False).reset_index(drop=True)
print(hasil)
hasil = hasil.head(10)
print(hasil)

hasil = df['Country'].value_counts().reset_index(name='total')
hasil = hasil.head(10)
print(hasil)

df.Country.value_counts().head(10).sort_values(ascending=True).plot.barh()
plt.show()