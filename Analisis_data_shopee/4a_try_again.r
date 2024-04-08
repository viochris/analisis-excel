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

df <- df_od
df$order_date <- as.Date(df$order_date)
df <- filter(df, is_valid == 1, year(order_date) == 2022, month(order_date) %in% c(10:12))

tabel_days <- df[wday(df$order_date) %in% c(2:6),]
tabel_days <- round(mean(tabel_days$before_discount))
tabel_end <- filter(df, wday(order_date) %in% c(1, 7))
tabel_end <- round(mean(tabel_end$before_discount))

# 1 = minggu - 7 = sabtu

df <- data.frame(
    Total = 'Total 3 Bulan',
    weekdays = tabel_days,
    weekend = tabel_end,
    Keuntungan = tabel_end - tabel_days,
    persentase = (tabel_end - tabel_days) / tabel_end * 100
)
print(df)