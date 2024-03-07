library(dplyr)

customer <- read.csv("Analisis excel/Youtube/5 soal/Customer.csv")


order <- read.csv("Analisis excel/Youtube/5 soal/Orders.csv")
order$Order.Date <- as.Date(order$Order.Date, "%m/%d/%Y")
order <- order %>% group_by(Customer.ID) %>% summarise(first_order = min(Order.Date))

# df <-  merge(customer, order, by = "Customer.ID", all = FALSE)
df <-  inner_join(customer, order, by = "Customer.ID", relationship ="many-to-many")


hasil <- df %>% group_by(City, first_order) %>% summarise(total_pembeli = n()) %>% arrange(desc(total_pembeli))
print(hasil)
hasil2 <- df %>% group_by(City, first_order) %>% summarise(total_pembeli = n_distinct(Customer.ID)) %>% arrange(desc(total_pembeli))
print(hasil2, n=20)