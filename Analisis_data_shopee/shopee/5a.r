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
df <- filter(df, is_valid == 1)
df$produk <- case_when(
    grepl('samsung', tolower(df$sku_name)) ~ 'Samsung',
    grepl('apple|iphone|macbook', tolower(df$sku_name)) ~ 'Apple',
    grepl('sony', tolower(df$sku_name)) ~ 'Sony',
    grepl('huawei', tolower(df$sku_name)) ~ 'Huawei',
    grepl('lenovo', tolower(df$sku_name)) ~ 'Lenovo',
    TRUE ~ 'others'
)
df <- filter(df, produk != 'others')
print(head(df))

hasil <- df %>% group_by(produk) %>% summarise(total = round(sum(after_discount))) %>% arrange(desc(total))
print(hasil)