from operator import le
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

df_hotel = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
# df_hotel = df_hotel.reset_index().rename(columns={'index':'id'})
df_hotel = df_hotel.reset_index().rename({'index':'id'})
print(df_hotel)

def check(df):
    df_hasil = pd.DataFrame({
        'nama': df.columns.tolist(),
        'dtype': df.dtypes.tolist(),
        'null': df.isnull().sum().tolist(),
        'null%': (df.isna().mean()*100).tolist(),
        'unique': df.nunique().tolist()
    })
    return df_hasil
print("Data Hotel:")
print(check(df_hotel))