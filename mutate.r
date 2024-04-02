# Mengimpor library
library(dplyr)

# Membuat DataFrame contoh
df <- data.frame(
    Nama = c('John', 'Doe', 'Jane', 'Smith'),
    Usia = c(30, 25, 35, 40)
)

# Menambahkan kolom baru yang merupakan panjang nama
cat('mutate tidak langsung: \n')
df <- df %>%
    mutate(Panjang_Nama = nchar(Nama))

# Menampilkan DataFrame hasil
print(df)

cat('\n\nmutate langsung: \n')
df <- mutate(df, Panjang_Nama = nchar(Nama))
print(df)