library(dplyr)

df <- read.csv('test_shopee_all/Customer.csv') #, col.names = c('customer_id', 'name', 'segment', 'city', 'state'))
print(head(df))
# colnames(df) <- c('customer_id', 'name', 'segment', 'city', 'state')
# print(head(df))

hasil <- df %>% group_by(City) %>% summarise(jumlah = n_distinct(Customer.ID)) %>% arrange(desc(jumlah))
print(head(hasil))
print(tail(hasil))