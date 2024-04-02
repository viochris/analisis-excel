import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
city = df[df['hotel'] == 'City Hotel']
hasil = city['is_canceled'].value_counts(normalize=True)
print('City Hotel')
print(hasil)
print()
resort = df[df['hotel'] == 'Resort Hotel']
hasil = resort['is_canceled'].value_counts(normalize=True)
print('Resort Hotel')
print(hasil)
