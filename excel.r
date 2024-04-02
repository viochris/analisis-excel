library(RMySQL)
library(dplyr)
library(tidyr)
library(lubridate)

df <- read.csv('Data Shopee.csv')
df$order_date <- as.Date(df$order_date)
print(head(df))

df$net_profit <- df$before_discount - df$cogs * df$qty_ordered

hasil <- df %>% group_by(year(order_date),month(order_date)) %>% summarise(net_profit = sum(net_profit),
            before_discount = sum(before_discount),
            id = n_distinct(id),
            after_discount = sum(after_discount))
hasil$aov <- hasil$before_discount / hasil$id
print(hasil)

write.csv(hasil, 'aov.xlsx')