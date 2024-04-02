# Mengimpor library
library(dplyr)


# Membuat DataFrame contoh
df <- data.frame(
    Nama = c("John", "Doe", "Jane", "Smith", "John", NULL, "Bari", "Jan"),
    Usia = c(30, 25, 35, 40, 30, 34, NULL, 35)
)


hasil <- sapply(df, function(x) length(unique(x)))
print(hasil)
cat("\n\n")
hasil <- sapply(df, function(x) length(unique(na.omit(x))))
print(hasil)
cat("\n\n")
hasil <- sapply(df, function(x) length(unique(x[!is.na(x)])))
print(hasil)
cat("\n\n")



hasil <- sapply(df, function(x) sum(!duplicated(x)))
print(hasil)
cat("\n\n")
hasil <- sapply(df, function(x) sum(!duplicated(x)))
print(hasil)
cat("\n\n")

# Error in UseMethod("distinct") : 
#   no applicable method for 'distinct' applied to an object of class "character"
# hasil <- sapply(df, function(x) length(distinct(x, .keep_all = TRUE)))
# print(hasil)
# cat("\n\n")
# hasil <- sapply(df, function(x) length(distinct()))
# print(hasil)
# cat("\n\n")


# Menghitung jumlah nilai unik dalam kolom 'Nama'
jumlah_nama_unik <- df %>%
    summarise(Jumlah_Nama_Unik = n_distinct(Nama))

# Menghitung jumlah nilai unik dalam kolom 'Usia'
# jumlah_usia_unik <- df %>%
#     summarize(Jumlah_Usia_Unik = n_distinct(Usia))
jumlah_usia_unik <- summarize(df, Jumlah_Usia_Unik = n_distinct(Usia))

total <- n_distinct(df$Nama)
# Menampilkan hasil
print(jumlah_nama_unik)
print(jumlah_usia_unik)
print(total)
cat("\n\n\n")

unique <- df %>% summarise(across(everything(), n_distinct))
print(unique)

cat("\n\n")
unique <- df %>% summarize(across(everything(), ~ n_distinct(.[!is.na(.)])))
print(unique)

cat("\n\n")
unique <- df %>% summarize(across(everything(), ~ n_distinct(na.omit(.))))
print(unique)
