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
merged_df <- merge(left_df, right_df, by = 'key', all.x = TRUE)
print(merged_df)

# Gabungkan DataFrame dengan metode 'right'
merged_df <- merge(left_df, right_df, by = 'key', all.y = TRUE)
print(merged_df)

# Gabungkan DataFrame dengan metode 'inner'
merged_df <- merge(left_df, right_df, by = 'key')
print(merged_df)

# Gabungkan DataFrame dengan metode 'outer'
merged_df <- merge(left_df, right_df, by = 'key', all = TRUE)
print(merged_df)
