library(dplyr)
library(lubridate)

df <- read.csv('test_shopee_all/Orders.csv')
# df$Order.Date <- mdy(df$Order.Date)
df$Order.Date <- as.Date(df$Order.Date, format = '%m/%d/%Y')

filter <- df %>% group_by(Customer.ID) %>% summarise(pembelian_awal = min(Order.Date)) %>% arrange(Customer.ID)
print(head(df))
print(head(filter))

hasil <- merge(df, filter, by = 'Customer.ID')
# hasil <- hasil %>% filter(hasil$Order.Date == hasil$pembelian_awal)
hasil_df <- hasil[hasil$Order.Date == hasil$pembelian_awal, ]
print(head(hasil_df))

hasil <- subset(hasil_df, select = c(Customer.ID, Sales))
hasil <- arrange(hasil, Customer.ID)
# hasil <- hasil[order(hasil$Customer.ID), ]
print(head(hasil))
print(tail(hasil))
cat('\n\n\n\n')

hasil <- hasil_df %>% group_by(Customer.ID) %>% summarize(sales = unique(Sales)) %>% arrange(Customer.ID)
print(head(hasil))
print(tail(hasil))