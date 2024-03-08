import pandas as pd
import numpy as np

# Membuat DataFrame contoh
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, np.nan, 3, np.nan, 5]
}
df = pd.DataFrame(data)

# Mengisi nilai yang hilang dengan median
df_filled = df.fillna(df.median())
# df_filled = df.fillna(df.mean())
# df_filled = df.fillna(df.mode().iloc[0])

print("DataFrame awal:")
print(df)
print("\nDataFrame setelah pengisian nilai yang hilang dengan median:")
print(df_filled)
