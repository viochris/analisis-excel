library(dplyr)
library(tidyverse)
library(ggplot2)

df_hotel <- read.csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv', na.strings = c("", "NA", " ", "N/A", "NULL"))
df <- df_hotel %>% mutate(ID = row_number()) %>% select(ID, everything())
df$arrival_date <- ymd(paste(df$arrival_date_year, df$arrival_date_month, df$arrival_date_day_of_month ,sep='-'))

df <- filter(df, is_canceled == 0)

df_reservasi_perhari_awal <- df %>% group_by(arrival_date) %>% summarise(total = sum(!is.na(is_canceled)))
print(head(df_reservasi_perhari_awal))

df_reservasi_perhari <- df_reservasi_perhari_awal %>% group_by(week = floor_date(arrival_date, "week")) %>% summarise(total = mean(total))
print(head(df_reservasi_perhari))

df_reservasi_perhari <- df_reservasi_perhari_awal %>% group_by(week = floor_date(arrival_date-1, "week")) %>% summarise(total = mean(total))
print(head(df_reservasi_perhari))
print(tail(df_reservasi_perhari))


plot(df_reservasi_perhari_awal$arrival_date, df_reservasi_perhari_awal$total,
        type = "l",
        xlab = "Tanggal Tiba",
        ylab = "Jumlah Reservasi",
        main = "Jumlah Reservasi per Hari")