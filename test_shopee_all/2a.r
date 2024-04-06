library(dplyr)

customer <- read.csv('test_shopee_all/Customer.csv')
customer <- distinct(customer, City, Customer.ID)

order <- read.csv('test_shopee_all/Orders.csv')

print(head(customer))
print(head(order))
cat('\n\n\n')

hasil <- inner_join(customer, order, by = 'Customer.ID')
hasil <- hasil %>% group_by(City) %>% summarise(jumlah = n()) %>% arrange(desc(jumlah))
print(head(hasil))