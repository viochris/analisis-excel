import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re


df_hotel = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
df_hotel = df_hotel.reset_index().rename(columns={'index': 'id'})

df_hotel['arrival_date'] = pd.to_datetime(df_hotel['arrival_date_year'].astype(str) + '-' + df_hotel['arrival_date_month'].astype(str) + '-' + df_hotel['arrival_date_day_of_month'].astype(str))
print(df_hotel)