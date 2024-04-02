library(RMySQL)
library(dplyr)
library(tidyr)
library(lubridate)

# Ganti 'dbname', 'username', 'password', dan 'host' sesuai dengan informasi database Anda
con <- dbConnect(MySQL(), dbname = "pembelian_shopee", user = "root", password = "", host = "localhost")

query1 <- "SELECT * FROM order_detail"
query2 <- "SELECT * FROM sku_detail"

df1 <- dbGetQuery(con, query1)
df2 <- dbGetQuery(con, query2)
dbDisconnect(con)

print(head(df1))
cat("\n")
print(head(df2))
cat("\n\n")

# df <- merge(df1, df2, by.x = "sku_id", by.y = "id", all=FALSE)
df <- inner_join(df1, df2, by = c("sku_id" = "id"), relationship = "many-to-many")
print(head(df))
cat("\n\n")

df <- filter(df, is_valid ==1)
df <- df %>% mutate(
    produk = case_when(
        grepl('samsung', tolower(sku_name)) ~ 'samsung',
        grepl('apple|iphone|macbook', tolower(sku_name)) ~ 'apple',
        grepl('sony', tolower(sku_name)) ~ 'sony',
        grepl('huawei', tolower(sku_name)) ~ 'huawei',
        grepl('lenovo', tolower(sku_name)) ~ 'lenovo',
        TRUE ~ 'others'
    )
)

df <- filter(df, produk != 'others')
print(head(df))

hasil <- df %>% group_by(produk) %>% summarise(total = sum(after_discount)) %>% arrange(desc(total))
print(hasil)