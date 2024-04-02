import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
df = df[df['is_canceled'] == 0]
df['arrival_date'] = pd.to_datetime(df['arrival_date_year'].astype(str) + '-' + df['arrival_date_month'].astype(str) + '-' + df['arrival_date_day_of_month'].astype(str))
df_checkout = df.groupby(['hotel','customer_type'])['adr'].mean().reset_index()
print(df_checkout)
# print(hasil1.loc[0:3, 'adr'].max())
# print(hasil1.loc[4:7, 'adr'].max())

plt.figure(figsize=(8,6))
sns.boxplot(data=df_checkout, x='adr', y='hotel', hue='customer_type')
sns.stripplot(data=df_checkout, x='adr', y='hotel', hue='customer_type', dodge=True, size=8, alpha=0.5)
plt.title('Boxplot ADR berdasarkan Jenis Hotel dan Tipe Pelanggan')
plt.xlabel('ADR')
plt.ylabel('Jenis Hotel')
plt.show()