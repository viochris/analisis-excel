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

df <- merge(df_od, df_cd, by.x = 'customer_id', by.y = 'id')
df <- filter(df, is_valid == 0, is_gross == 1, is_net == 0)
df$order_date <- ymd(df$order_date)
df <- df[year(df$order_date) == 2022, ]
df <- distinct(df, customer_id, .keep_all = TRUE)
print(head(df))

hasil <- df[c('customer_id', 'registered_date')]
# hasil <- arrange(hasil, customer_id)
hasil <- hasil[order(hasil$customer_id),]
print(head(hasil))
print(tail(hasil))