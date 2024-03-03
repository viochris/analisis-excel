import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re


df_hotel = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
df_hotel = df_hotel.reset_index().rename(columns={'index': 'id'})
city = df_hotel[df_hotel['hotel']=='City Hotel']
print(city['is_canceled'].value_counts(normalize=True))
resort = df_hotel[df_hotel['hotel']=='Resort Hotel']
print(resort['is_canceled'].value_counts(normalize=True))
sns.countplot(data=city, x='is_canceled')
plt.show()
