import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
df = df[df['is_canceled'] == 0]
hasil = df.groupby(['hotel', 'arrival_date_month'])['reservation_status'].count().reset_index(name='jumlah')
print(hasil)

df['arrival_date_month'] = df['arrival_date_month'].replace(('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'), (1,2,3,4,5,6,7,8,9,10,11,12))
hasil2 = df.groupby(['hotel', 'arrival_date_month'])['reservation_status'].count().reset_index(name='jumlah')
print(hasil2)

sns.countplot(data=df, x='arrival_date_month', hue='hotel')
plt.xlabel('Month')
plt.ylabel('Count')
plt.title('Arrival Plot')
plt.show()