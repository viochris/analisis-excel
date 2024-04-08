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
df <- filter(df, is_valid == 1)
df$order_date <- as.Date(df$order_date)
df <- df[year(df$order_date) == 2022, ]
df <- df[month(df$order_date) %in% c(10:12),]
print(head(df))

weekdays <- df[weekdays(df$order_date) %in% c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"), ]
weekdays <- round(mean(weekdays$before_discount), 2)

weekends <- filter(df, weekdays(order_date) %in% c("Saturday", "Sunday"))
weekends <- round(mean(weekends$before_discount), 2)

hasil <- data.frame(
    Total =  'Total 3 Bulan',
    weekday = weekdays,
    weekend = weekends,
    keuntungan = weekends - weekdays,
    persentase =round((weekends - weekdays) / weekends * 100, 2)
)
print(hasil)