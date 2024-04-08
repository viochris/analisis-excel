library(dplyr)

# Membuat dataframe
df <- data.frame(
    Nama = c('Andi', 'Budi', 'Cindy', 'Deni', 'Andi'),
    Kelas = c('A', 'B', 'A', 'C', 'C'),
    Umur = c(20, 22, 21, 23, 21)
)

# Menampilkan dataframe
print(df)

# Mengurutkan dataframe berdasarkan dua kolom secara berurutan
df_sorted <- df %>% arrange(Kelas, Umur)

# Menampilkan hasil
print(df_sorted)
