import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
hasil = df['is_canceled'].value_counts()
print(hasil)
proporsi = df['is_canceled'].value_counts(normalize=True)
print(proporsi)

sns.countplot(data=df, x='is_canceled')
plt.title('Cancelled')
plt.show()