library(dplyr)

# Contoh DataFrame
df <- data.frame(Nama = c('a', 'b', 'c'),
                    A = c(1, 2, 3),
                    B = c(4, 5, 6),
                    C = c(7, 8, 9))

# Fungsi yang diaplikasikan pada setiap kolom
double_column <- function(x, y, z) {
  return(x * y * z)
}

# Tampilkan DataFrame hasil
print("DataFrame setelah apply pada kolom:")
print(data)

df$total <- mapply(double_column,df$A, df$B, df$C)
df$total2 <- df$A * df$B
df$total3 <- sapply(df$A, function(x) x * 2)
print(df)

column <- function(x) {
  return(x * 2)
}
df$total4 <- sapply(df$A, column)
df$total5 <- sapply(df$A, function(x) column(x))
print(df)