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

# df <- merge(df1, df2, by.x = "sku_id", by.y = "id")
df <- inner_join(df1, df2, by = c("sku_id" = "id"))
print(head(df))

df <- df[df$is_valid == 1, ]
df$order_date <- as.Date(df$order_date)
df <- filter(df, year(order_date) == 2022)

tabel1 <- df %>%
    group_by(sku_name, category) %>%
    summarise(after_discount = sum(after_discount), qty_ordered = sum(qty_ordered)) %>%
    arrange(desc(qty_ordered))
tabel1 <- head(tabel1, 10)
print(tabel1)


tabel2 <- df %>% distinct(customer_id, .keep_all = TRUE) %>% group_by(sku_name, category) %>% summarise(jumlah_pelanggan = n_distinct(customer_id))
print(head(tabel2))



tabel3 <- df %>% distinct(id, .keep_all = TRUE) %>% group_by(sku_name, category) %>% summarise(total_order = n_distinct(id))
print(head(tabel3))
cat('\n\n\n\n\n\n')


tabelawal <- merge(tabel1, tabel2, by = c('sku_name', 'category'))
tabelakhir <- merge(tabelawal, tabel3, by = c('sku_name', 'category'))
tabelakhir <- tabelakhir %>% arrange(desc(qty_ordered))
print(tabelakhir)
