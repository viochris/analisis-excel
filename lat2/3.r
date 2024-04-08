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

df <- filter(df, is_valid == 1)
df$order_date <- as.Date(df$order_date)
df$profit <- df$after_discount - (df$cogs * df$qty_ordered)

tabel2021 <- filter(df, year(order_date) == 2021)
tabel2021 <- tabel2021 %>% group_by(category) %>% summarize(`2021` = sum(profit))

tabel2022 <- filter(df, year(order_date) == 2022)
tabel2022 <- tabel2022 %>% group_by(category) %>% summarize(`2022` = sum(profit))

tabel <- merge(tabel2021, tabel2022, by = 'category')
tabel$persentase <- (tabel$`2022` - tabel$`2021`) / tabel$`2021` *100
tabel <- arrange(tabel, desc(persentase))
print(tabel)