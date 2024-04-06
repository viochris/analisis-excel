library(dplyr)
library(lubridate)

df <- read.csv('test_shopee_all/Orders.csv')
# df$Order.Date <- mdy(df$Order.Date)
df$Order.Date <- as.Date(df$Order.Date, format = '%m/%d/%Y')
print(head(df))

hasil <- df %>% group_by(Customer.ID) %>% summarise(pembelian_awal = min(Order.Date)) %>% arrange(Customer.ID)
print(head(hasil))
print(tail(hasil))