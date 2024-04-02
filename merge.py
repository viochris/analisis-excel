import pandas as pd

# Buat DataFrame kiri
left_df = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                        'value_left': ['A', 'B', 'C']})

# Buat DataFrame kanan
right_df = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K5', 'K0'],
                        'value_right': ['X', 'Y', 'Z', 'W', 'AAA']})

# Gabungkan DataFrame dengan metode 'left'
merged_df = pd.merge(left_df, right_df, on='key', how='left')

print(merged_df)
