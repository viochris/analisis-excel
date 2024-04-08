library(RMySQL)
library(dplyr)
library(lubridate)

# Ganti 'dbname', 'username', 'password', dan 'host' sesuai dengan informasi database Anda
con <- dbConnect(MySQL(), dbname = "pembelian_shopee", user = "root", password = "", host = "localhost")

query1 <- "SELECT * FROM order_detail"
df1 <- dbGetQuery(con, query1)
query2 <- "SELECT * FROM sku_detail"
df2 <- dbGetQuery(con, query2)
dbDisconnect(con)

df <- inner_join(df1, df2, by = c("sku_id" = "id"))
# df <- merge(df1, df2, by.x = 'sku_id', by.y = 'id')
df$order_date <- ymd(df$order_date)
df <- filter(df, is_valid == 1, year(order_date) == 2022)
df <- arrange(df, sku_id)
# print(head(df))

# Penggunaan metode `sort` di Python dan `arrange` di R sebelum operasi 
# penghapusan duplikat dapat membantu mengurangi perbedaan hasil antara kedua bahasa. 
# Namun, dalam kasus di mana ada nilai yang sama dalam kolom pengurutan, perbedaan masih 
# mungkin terjadi karena urutan yang tidak terjamin sama di antara nilai-nilai yang sama.
# Penggunaan sort dan arrange disarankan karena adanya kerandoman yang membuat urutan tidak terjamin 
# saat menjalankan merge atau join.

tabel1 <- df %>%
    group_by(sku_name, category) %>%
    summarise(after_discount = sum(after_discount), qty_ordered = sum(qty_ordered)) %>%
    arrange(desc(qty_ordered))
tabel1 <- head(tabel1, 10)

tabel2 <- distinct(df, customer_id, .keep_all = TRUE)
tabel2 <- tabel2 %>%
    group_by(sku_name, category) %>%
    summarise(jumlah_pelanggan = n_distinct(customer_id))

tabel3 <- df[!duplicated(df$id), ]
tabel3 <- tabel3 %>%
    group_by(sku_name, category) %>%
    summarise(total_order = n_distinct(id))


tabelawal <- merge(tabel1, tabel2, by = c("sku_name", "category"))
tabelakhir <- merge(tabelawal, tabel3, by = c("sku_name", "category"))
tabelakhir <- arrange(tabelakhir, desc(qty_ordered))
print(tabelakhir)
