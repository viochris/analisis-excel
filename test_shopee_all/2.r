library(dplyr)

customer <- read.csv('test_shopee_all/Customer.csv')
customer <- customer %>% group_by(City) %>% summarise(ID = unique(Customer.ID))

order <- read.csv('test_shopee_all/Orders.csv')

print(head(customer))
print(head(order))
cat('\n\n\n')

# hasil <- merge(customer, order, by.x = 'ID', by.y = 'Customer.ID')
hasil <- inner_join(customer, order, by = c('ID' = 'Customer.ID'))
hasil <- hasil %>% group_by(City) %>% summarise(jumlah = n()) %>% arrange(desc(jumlah))
print(head(hasil))