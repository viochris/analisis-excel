import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv')
df_1 = df[df['is_canceled'] == 0]
print(df_1)
df_checkout = df[df['reservation_status'] == 'Check-Out']
print(df_checkout)