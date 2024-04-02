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


df <- inner_join(df_od, df_cd, by = c("customer_id" = "id"), relationship = "many-to-many")
df <- df[df$is_gross == 1, ]
df <- filter(df, is_valid==0)
df <- df %>% filter(is_net == 0)
df$order_date <- as.Date(df$order_date)
df <- df %>% filter(year(order_date) == 2022)
df <- df %>% distinct(customer_id, .keep_all = TRUE)
# df <- distinct(df, customer_id, .keep_all = TRUE)
print(head(df))

cat('\n\n')
print('Data Akhir')
hasil <- select(df, customer_id, registered_date)
print(head(hasil))
print(tail(hasil))