# Mengimpor library
library(stringr)

# Membuat DataFrame contoh
data <- data.frame(
    Nama = c('John', 'Doe', 'Jane', 'Smith'),
    Usia = c(30, 25, 35, 40)
)
print(df)

start_3 <- str_detect(data$Usia, '^3')
end_0 <- str_detect(data$Usia, '0$')

cat("Baris yang dimulai dengan 3:\n")
print(data[start_3, ])

cat("\nBaris yang diakhiri dengan 0:\n")
print(data[end_0, ])
