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

# df <- inner_join(df1, df2, by = c("sku_id" = "id"))
df <- merge(df1, df2, by.x = "sku_id", by.y = "id")
print(head(df))

df <- df[df$is_valid == 1, ]
df$order_date <- as.Date(df$order_date)
df <- filter(df, year(order_date) == 2022)
tabel1 <- df %>%
    group_by(category) %>%
    summarise(after_discount = sum(after_discount), qty_ordered = sum(qty_ordered))
print(tabel1)


tabel2 <- df %>% distinct(customer_id, .keep_all = TRUE)
print('Hasil: ')
print(dim(tabel2))
tabel2 <- tabel2 %>% 
    group_by(category) %>%
    summarise(customer_id = n(), id = n_distinct(id))
print(tabel2)
print(sum(tabel2$customer_id))


tabel <- inner_join(tabel1, tabel2, by = c("category"))
# tabel = merge(tabel1, tabel2, by = c('sku_name', 'category'))
tabel <- tabel %>% arrange(desc(qty_ordered))
tabel <- head(tabel, 10)
print(tabel)
