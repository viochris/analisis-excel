import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Baca data dari URL
df_hotel = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
df_country = pd.read_csv('https://gist.githubusercontent.com/tadast/8827699/raw/f5cac3d42d16b78348610fc4ec301e9234f82821/countries_codes_and_coordinates.csv')
print(df_country['Alpha-3 code'].value_counts())
df_country['code'] = df_country['Alpha-3 code'].str.replace('"', '').str.strip()
print(df_country[['Country', 'code']])
df_merged = pd.merge(df_hotel[['is_canceled', 'country']], df_country[['Country', 'code']], left_on='country', right_on='code', how='inner')
df_merged = df_merged[df_merged['is_canceled'] == 0]
print(df_merged)

hasil = df_merged['Country'].value_counts().reset_index(name='count')
hasil = hasil.head(10)
print(hasil)

hasil = df_merged['Country'].value_counts().reset_index(name='count').sort_values('count', ascending=False).reset_index(drop=True)
hasil = hasil.head(10)
print(hasil)

df_merged.Country.value_counts().head(10).sort_values(ascending=True).plot.barh()
plt.show()