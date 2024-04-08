library(dplyr)

set.seed(123)
n_rows <- 1000
df <- data.frame(
  sku_name = sample(LETTERS[1:5], n_rows, replace = TRUE),
  category = sample(c("X", "Y", "Z"), n_rows, replace = TRUE),
  customer_id = sample(1:200, n_rows, replace = TRUE)
)
print(dim(df))

# Menggunakan distinct bersama dengan group_by
tabel2 <- df %>% distinct(customer_id, .keep_all = TRUE)
print(dim(tabel2))

tabel2 <- tabel2 %>% group_by(sku_name, category) %>% summarise(jumlah_pelanggan = n_distinct(customer_id))

# Menampilkan hasil
print(tabel2)
