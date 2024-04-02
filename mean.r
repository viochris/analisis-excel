# Buat data frame contoh
df <- data.frame(
  A = c(1, 2, 3, 4, 5),
  B = c(6, 7, 8, 9, 10),
  C = c(11, 12, 13, 14, 15)
)

# Tampilkan data frame
print(df)
cat('\n\n')
print(mean(df$A))
cat('\n\n')
hasil <- sapply(df, mean)
print(hasil)
cat('\n\n')
hasil <- colMeans(df)
print(hasil)
cat('\n\n')
hasil <- rowMeans(df)
print(hasil)