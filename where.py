import pandas as pd
import numpy as np

df = pd.DataFrame({
    'daftar': ['a', 'b', 'c', 'd', 'e', 'b', 'c', 'd', 'c', 'e'],
    'daftar2': ['makanan', 'minuman', 'minuman', 'makanan', 'makanan', 'minum', 'makan', 'maka', 'minu', 'makan']
})

df['penjelasan']= np.where(
    df['daftar'].isin(['a', 'b', 'c']),
    'good', 'bad'
)

print(df)