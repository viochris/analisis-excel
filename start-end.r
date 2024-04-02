# Mengimpor library
library(stringr)

# Membuat DataFrame contoh
data <- data.frame(
    Nama = c('John', 'Doe', 'Jane', 'Smith'),
    Usia = c(30, 25, 35, 40)
)

# Memeriksa apakah nilai di kolom 'Nama' dimulai dengan 'J'
starts_with_J <- str_detect(tolower(data$Nama), '^j')

# Memeriksa apakah nilai di kolom 'Nama' diakhiri dengan 'e'
ends_with_e <- str_detect(tolower(data$Nama), 'e$')

cat("Baris yang dimulai dengan 'J':\n")
print(data[starts_with_J, ])

cat("\nBaris yang diakhiri dengan 'e':\n")
print(data[ends_with_e, ])
cat('\n\n')

cat("Baris yang tidak dimulai dengan 'J':\n")
print(data[!starts_with_J, ])

cat("\nBaris yang tidak  diakhiri dengan 'e':\n")
print(data[!ends_with_e, ])
