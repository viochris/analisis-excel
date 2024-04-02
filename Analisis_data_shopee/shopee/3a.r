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
df$order_date <- ymd(df$order_date)
print(head(df))


tabel21 <- df[year(df$order_date) == 2021, ]
tabel21 <- tabel21 %>% group_by(category) %>% summarise(tahun2021 = sum(after_discount))

tabel22 <- filter(df, year(order_date) == 2022)
tabel22 <- tabel22 %>% group_by(category) %>% summarise(tahun2022 = sum(after_discount))

hasil <- merge(tabel21, tabel22, by='category')
hasil$perbedaan <- hasil$tahun2022 - hasil$tahun2021

penjelasan <- function(x){
    if (x > 0){
        return('Naik')
    }else if(x < 0){
        return('Turun')
    }else{
        return(NULL)
    }}
hasil$penjelasan <- sapply(hasil$perbedaan, penjelasan)
hasil <- hasil %>% arrange(desc(hasil$perbedaan))
print(hasil)