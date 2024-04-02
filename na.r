# Contoh data frame
df <- data.frame(
    A = c(1, 2, NA, 4),
    B = c(NA, 2, 3, NA),
    C = c(NA, NA, NA, NA)
)

# Menghitung jumlah baris yang tidak memiliki nilai NA dalam kolom 'A'
print(sum(!is.na(df$A)))  # Output: 3
print(sapply(df, function(x) sum(is.na(x))))  # Output: 3
print(sapply(df, function(x) sum(!is.na(x))))  # Output: 3
print(sum(df$A))
#ketika ada NA, jika na.rm tidak sama dengan true, hasilnya akan NA juga
#hal ini berlaku untuk fungsi agregasi pada normalnya, seperti sum, mean, dll.
#tapi tidak untuk seperti sum(is.na(df))