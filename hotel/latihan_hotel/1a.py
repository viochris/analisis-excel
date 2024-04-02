import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

df_hotel = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
df_hotel = df_hotel.reset_index().rename(columns = {'index': 'id'})
df_hotel['ID1'] = df_hotel.index


def check(df):
    data = pd.DataFrame({
        'Nama': df.columns.tolist(),
        'Dtypes': df.dtypes.tolist(),
        'Null': df.isnull().sum().tolist(),
        'Nullpct': ((df.isnull().sum() / len(df) * 100).round(2).astype(str) + '%').tolist(),
        'Nullpct1': ((df.isnull().sum() / df.shape[0] * 100).round(2).astype(str) + '%').tolist(),
        'Nullpct2': ((df.isnull().mean() * 100).round(2).astype(str) + '%').tolist(),
        'Nunique': df.nunique().tolist(),
        
        #TIDAK BISA KARENA ISINYA ADA YANG STR DLL
        # 'min': df.min().tolist(),
        # 'max': df.max().tolist(),
        # 'median': df.median().tolist()
    })
    return data

hasil = check(df_hotel)
print(hasil)