library(dplyr)

# Membuat data frame contoh dengan beberapa kolom tahun
data <- data.frame(
    tahun_2012 = c(1, 2, 3),
    tahun_2020 = c(4, 5, 6),
    tahun_1962 = c(7, 8, 9),
    tahun_2013 = c(10, 11, 12),
    tahun_2022 = c(10, 11, 12)
)

# Memilih kolom-kolom yang merupakan tahun di tahun 20-an
hasil <- data %>%
    summarise(across(starts_with("tahun"), mean))

# Menampilkan hasil
print(hasil)
cat("\n\n")
# Memilih kolom-kolom yang merupakan tahun di tahun 20-an
hasil <- data %>%
    summarise(across(ends_with("2"), mean))

# Menampilkan hasil
print(hasil)
cat("\n\n")
# Memilih kolom-kolom yang merupakan tahun di tahun 20-an
hasil <- data %>%
    summarise(across(contains("20"), mean))

# Menampilkan hasil
print(hasil)


cat("\n\n\n\n")

# Membuat data frame contoh dengan beberapa kolom yang mengandung kata "bunga"
data <- data.frame(
    bunga_mawar = c(1, 2, 3),
    nama_bunga = c(4, 5, 6),
    jumlah_bunga = c(7, 8, 9),
    bukan_buunga = c(10, 11, 12)
)

# Memilih kolom-kolom yang mengandung kata "bunga"
hasil <- data %>%
    summarise(across(contains("bunga"), mean))

# Menampilkan hasil
print(hasil)
