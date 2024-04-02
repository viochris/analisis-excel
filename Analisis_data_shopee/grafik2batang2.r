# Membuat data
set_a <- c(10, 15, 20)  # Contoh data untuk set batang A
set_b <- c(25, 30, 35)  # Contoh data untuk set batang B

# Membuat barplot tanpa jarak antara setiap pasangan AB
barplot(
  rbind(set_a, set_b),
  beside = TRUE,
  col = c("blue", "red"),
  names.arg = c("Bar 1", "Bar 2", "Bar 3"),
  ylim = c(0, max(set_a, set_b) + 5),  # Menyesuaikan batas atas sumbu y
  xlab = "Bats",
  ylab = "Values",
  main = "Barplot without Gap"
)

# Membuat barplot dengan jarak antara setiap pasangan AB
barplot(
  rbind(set_a, set_b),
  beside = TRUE,
  col = c("blue", "red"),
  names.arg = c("Bar 1", "Bar 2", "Bar 3"),
  space = c(0.5, 2),  # Menambahkan jarak antara setiap pasangan AB
  ylim = c(0, max(set_a, set_b) + 5),  # Menyesuaikan batas atas sumbu y
  xlab = "Bats",
  ylab = "Values",
  main = "Barplot with Gap"
)
