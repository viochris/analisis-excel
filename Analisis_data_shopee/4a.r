library(RMySQL)
library(dplyr)
library(tidyr)
library(lubridate)
# library(stringr)
library(tidyverse)

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
df <- df[df$is_valid == 1, ]
df <- filter(df, year(order_date) == 2022, month(order_date) %in% c(10, 11, 12))
df <- df %>% mutate(
    month = case_when(
        month(order_date) == 10 ~ "Oktober",
        month(order_date) == 11 ~ "November",
        month(order_date) == 12 ~ "Desember",
        TRUE ~ as.character(month(order_date, label=TRUE))
    )
)
df$month1 <- str_replace_all(month(df$order_date), c("10" = "Oktober", "11" = "November", "12" = "Desember"))
print(head(df))


weekday <- df[weekdays(df$order_date) %in% c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"), ]
weekday <- round(mean(weekday$before_discount), 2)


weekend <- filter(df, weekdays(df$order_date) %in% c("Saturday", "Sunday"))
weekend <- round(mean(weekend$before_discount), 2)
# weekend <- weekend %>% summarize(weekend = round(mean(before_discount), 2))

data  <- data.frame(
    total = 'total 3 bulan',
    weekdays = weekday,
    weekend = weekend,
    untung = weekend - weekday,
    persentase = round((weekend - weekday) / weekend * 100, 2)
)
print(data)