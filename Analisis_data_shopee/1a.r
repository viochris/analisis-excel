library(RMySQL)
library(dplyr)
library(tidyr)
library(lubridate)

path_od <- "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/order_detail.csv"
path_pd <- "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/payment_detail.csv"
path_cd <- "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/customer_detail.csv"
path_sd <- "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/sku_detail.csv"
df_od <- read.csv(path_od)
df_pd <- read.csv(path_pd)
df_cd <- read.csv(path_cd)
df_sd <- read.csv(path_sd)

df <- merge(df_od, df_sd[c('id', 'sku_name', 'category')], by.x = 'sku_id', by.y = 'id')
df <- df[df$is_valid == 1,]
df <- filter(df, category == 'Mobiles & Tablets')
df$order_date <- ymd(df$order_date)
# df$order_date <- as.Date(df$order_date)
df <- filter(df, year(order_date) == 2022)
print(head(df))


hasil <- df %>% group_by(sku_name) %>% summarise(jumlah = sum(qty_ordered)) %>% arrange(desc(jumlah))
hasil <- head(hasil, 5)
print(hasil)

barplot(hasil$jumlah, horiz = TRUE, names.arg = hasil$sku_name, col = "skyblue",
        main = "2022 Top 5 Ordered On Mobiles and Tablets Category",
        xlab = "Total order", ylab = "SKU name"
)