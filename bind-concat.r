# Buat dua data frame contoh
df1 <- data.frame(A = 1:3, B = c('a', 'b', 'c'))
df2 <- data.frame(A = 4:6, B = c('d', 'e', 'f'))

# Gabungkan berdasarkan baris menggunakan rbind()
result <- rbind(df1, df2)
print(result)
cat('\n\n\n\n')



# Buat dua data frame contoh
df1 <- data.frame(A = 1:3, B = c('a', 'b', 'c'))
df2 <- data.frame(C = c('x', 'y', 'z'), D = 4:6)

# Gabungkan berdasarkan kolom menggunakan cbind()
result <- cbind(df1, df2)
print(result)
cat('\n\n\n\n')


