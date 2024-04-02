library(RMySQL)
library(dplyr)
library(lubridate)

# Ganti 'dbname', 'username', 'password', dan 'host' sesuai dengan informasi database Anda
con <- dbConnect(MySQL(), dbname = "pembelian_shopee", user = "root", password = "", host = "localhost")

query <- "SELECT * FROM order_detail"
df <- dbGetQuery(con, query)
dbDisconnect(con)

print(head(df))

# df <- df[df$is_valid == 1, ]
# df <- filter(df, is_valid == 1)
df <- df %>% filter(is_valid == 1)

df$order_date <- as.Date(df$order_date)
# df <- mutate(df, order_date = as.Date(order_date))

# df <- df[year(df$order_date) == 2021, ]
# df <- filter(df, year(order_date) == 2021)
df <- df %>% filter(year(order_date) == 2021) 

# df <- mutate(df, month = month(order_date))
df$month <- month(df$order_date)

print(head(df))


hasil <- df %>% group_by(month) %>% summarise(total = sum(after_discount)) %>% arrange(desc(total))
print(hasil)