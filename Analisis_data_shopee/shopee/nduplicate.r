library(RMySQL)
library(dplyr)
library(lubridate)

# Ganti 'dbname', 'username', 'password', dan 'host' sesuai dengan informasi database Anda
con <- dbConnect(MySQL(), dbname = "pembelian_shopee", user = "root", password = "", host = "localhost")

query <- "SELECT * FROM order_detail"
df <- dbGetQuery(con, query)
dbDisconnect(con)

print(head(df))

hasil <- df %>% group_by(customer_id) %>% summarise(jumlah = n()) %>% arrange(desc(jumlah))
print(head(hasil))
