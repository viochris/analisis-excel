library(RMySQL)
library(dplyr)
library(lubridate)

# Ganti 'dbname', 'username', 'password', dan 'host' sesuai dengan informasi database Anda
con <- dbConnect(MySQL(), dbname = "pembelian_shopee", user = "root", password = "", host = "localhost")

query1 <- "SELECT * FROM order_detail"
df1 <- dbGetQuery(con, query1)
query2 <- "SELECT * FROM payment_detail"
df2 <- dbGetQuery(con, query2)
query3 <- "SELECT * FROM sku_detail"
df3 <- dbGetQuery(con, query3)
dbDisconnect(con)

df <- inner_join(df1, df2, by = c('payment_id' = 'id'))
df$order_date <- ymd(df$order_date) 
df <- filter(df, is_valid == 1, year(order_date) == 2022)
print(head(df))
hasil <- df %>% group_by(payment_method) %>% summarise(total = n_distinct(id)) %>% arrange(desc(total))
top5 <- head(hasil, 5)
print(top5)



df_lain <- merge(df, df3, by.x = 'sku_id', by.y = 'id')
df_lain <- df_lain[df_lain$payment_method %in% top5$payment_method, ]
print(df_lain)
hasil <- df_lain %>% group_by(category, payment_method) %>% summarise(total = n_distinct(id)) %>% arrange(category)
print(head(hasil))
print(tail(hasil))