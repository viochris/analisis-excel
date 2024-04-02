# # Mengimpor paket zoo
# library(zoo)

# Membuat DataFrame contoh dengan nilai NA
df <- data.frame(A = c(1, NA, 3),
                 B = c(NA, 5, 6),
                 C = c(7, 8, NA))
print(df)

# df[is.na(df)] <- as.numeric(names(which.max(table(df$A))))
# print(df)

# Mengisi nilai-nilai NA dengan median menggunakan na.aggregate()
# df_filled <- na.aggregate(df, FUN = median, na.rm = TRUE)
# print(df_filled)

hasil <- sum(df$A, na.rm=TRUE)
print(hasil)
hasil <- mean(df$A, na.rm=TRUE)
print(hasil)
hasil <- median(df$A, na.rm=TRUE)
print(hasil)
hasil <- min(df$A, na.rm=TRUE)
print(hasil)
hasil <- max(df$A, na.rm=TRUE)
print(hasil)