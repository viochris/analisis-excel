# Membuat data
data <- data.frame(
  Kolom1 = c(10, 15),
  Kolom2 = c(20, 25)
)

# Menggambar plot
barplot(as.matrix(data), beside = TRUE, col = c("blue", "green"),
        names.arg = c("Baris1", "Baris2"),
        xlab = "Baris", ylab = "Nilai",
        main = "Contoh Grafik 2 Batang dengan 2 Kolom")