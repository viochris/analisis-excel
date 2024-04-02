# Load library
library(dplyr)

# Buat DataFrame
df <- data.frame(
    Nama = c(NA, "Niko", "Gaby", "Vio", "Maria"),
    Umur = c(12, 13, NA, 18, 34),
    Kelas = c(12, 13, 12, 16, NA)
)

print(df)
cat("\n")
print(df[is.na(df$Umur), ])
cat("\n")
print(df[!is.na(df$Umur), ])
cat("\n")
print(rowSums(is.na(df)))
cat("\n")
print(colSums(is.na(df)))
cat("\n")
print(df[rowSums(is.na(df[, c("Nama", "Kelas")])) > 0, ])
cat("\n")
print(df[rowSums(is.na(df)) > 0, ])
cat("\n")
print(df[, colSums(is.na(df)) > 0])
