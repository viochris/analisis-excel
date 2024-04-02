import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

df_hotel = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
df_hotel = df_hotel.reset_index().rename(columns={'index': 'id'})


def check(df):
    data = {
        'Nama': df.columns.tolist(),
        'Dtype': df.dtypes.tolist(),
        'Null': df.isna().sum().tolist(),
        'nullpct': ((df.isnull().sum() / df.shape[0] * 100).round(2).astype(str) + '%').tolist(),
        'nullpct2': ((df.isnull().sum() / len(df) * 100).round(2).astype(str) + '%').tolist(),
        'nullpct3': ((df.isnull().mean() * 100).round(2).astype(str) + '%').tolist(),
        'Unique': df.nunique().tolist()
    }
    df = pd.DataFrame(data)
    return df
hasil = check(df_hotel)
print(hasil)