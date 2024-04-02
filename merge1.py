import pandas as pd

# Buat DataFrame kiri
left_df = pd.DataFrame({'key': ['K0', 'K1', 'K3'],
                        'value_left': ['A', 'B', 'D']})

# Buat DataFrame kanan
right_df = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K5'],
                        'value_right': ['X', 'Y', 'Z', 'W']})

# Gabungkan DataFrame dengan metode 'left'
merged_df = pd.merge(left_df, right_df, on='key', how='left')
print(merged_df)
merged_df = pd.merge(left_df, right_df, on='key', how='right')
print(merged_df)
merged_df = pd.merge(left_df, right_df, on='key', how='inner')
print(merged_df)
merged_df = pd.merge(left_df, right_df, on='key', how='outer')
print(merged_df)
