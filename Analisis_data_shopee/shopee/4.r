library(RMySQL)
library(dplyr)
library(tidyr)
library(lubridate)

# Ganti 'dbname', 'username', 'password', dan 'host' sesuai dengan informasi database Anda
con <- dbConnect(MySQL(), dbname = "pembelian_shopee", user = "root", password = "", host = "localhost")

query1 <- "SELECT * FROM order_detail"
query2 <- "SELECT * FROM payment_detail"

df1 <- dbGetQuery(con, query1)
df2 <- dbGetQuery(con, query2)
dbDisconnect(con)

print(head(df1))
cat("\n")
print(head(df2))
cat("\n\n")


df <- merge(df1, df2, by.x = "payment_id", by.y = "id", all = FALSE)
print(head(df))

df <- filter(df, is_valid == 1)
df$order_date <- as.Date(df$order_date)
df <- filter(df, year(order_date) == 2022)
print(head(df))

hasil <- df %>% group_by(payment_method) %>% summarise(total = n_distinct(id)) %>% arrange(desc(total))
print(hasil)
print(head(hasil, 5))