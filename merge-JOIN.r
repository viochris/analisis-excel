# Load library
library(dplyr)

# Buat DataFrame kiri
left_df <- data.frame(
  key = c('K0', 'K1', 'K3'),
  value_left = c('A', 'B', 'D')
)

# Buat DataFrame kanan
right_df <- data.frame(
  key = c('K0', 'K1', 'K4', 'K5'),
  value_right = c('X', 'Y', 'Z', 'W')
)

# Gabungkan DataFrame dengan metode 'left'
merged_df <- left_join(left_df, right_df, by = 'key')
print(merged_df)

# Gabungkan DataFrame dengan metode 'right'
merged_df <- right_join(left_df, right_df, by = 'key')
print(merged_df)

# Gabungkan DataFrame dengan metode 'inner'
merged_df <- inner_join(left_df, right_df, by = 'key')
print(merged_df)

# Gabungkan DataFrame dengan metode 'outer'
merged_df <- full_join(left_df, right_df, by = 'key')
print(merged_df)
