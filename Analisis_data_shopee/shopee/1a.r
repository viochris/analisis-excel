library(RMySQL)
library(dplyr)
library(lubridate)

# Ganti 'dbname', 'username', 'password', dan 'host' sesuai dengan informasi database Anda
con <- dbConnect(MySQL(), dbname = "pembelian_shopee", user = "root", password = "", host = "localhost")

query <- "SELECT * FROM order_detail"
df <- dbGetQuery(con, query)
dbDisconnect(con)

print(head(df))
df <- filter(df, is_valid==1)
df$order_date <- as.Date(df$order_date)
df <- df[year(df$order_date) ==2021,]
df$month <- month(df$order_date)
print(head(df))


hasil <- df %>% group_by(month) %>% summarise(total = sum(after_discount)) %>% arrange(desc(total))
print(hasil)