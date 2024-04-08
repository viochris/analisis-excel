# Membuat dataframe contoh
df <- data.frame(
    A = c(1, 2, 3),
    B = c(4, 5, 6)
)

# Menampilkan dataframe
print(df)
cat('\n\n')
print(colSums(df))
print(rowSums(df))

cat('\n\n')
print(sum(df))
print(sum(df$A))
print(sum(df[, 'A']))
print(sum(df[1,]))