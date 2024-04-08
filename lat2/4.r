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

df <- inner_join(df1, df2, by = c('sku_id' = 'id'))
print(head(df))

df <- filter(df, is_valid == 1, category == 'Women Fashion')
df$order_date <- ymd(df$order_date)
df$profit <- df$after_discount - (df$cogs * df$qty_ordered)

hasil <- filter(df, year(order_date) == 2022)
hasil <- hasil %>% group_by(sku_name, category) %>% summarise(`2022` = sum(profit))
hasil <- arrange(hasil, desc(`2022`))
print(head(hasil, 5))