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

df <- merge(df1, df2, by.x = 'sku_id', by.y = 'id')
df <- df[df$is_valid == 1,]
df$order_date <- ymd(df$order_date)
df <- filter(df, year(order_date) == 2022)
print(head(df))

hasil <- df %>% group_by(category) %>% summarise(jumlah = round(sum(after_discount))) %>% arrange(desc(jumlah))
print(hasil)