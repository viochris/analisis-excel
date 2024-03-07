library(dplyr)
library(tidyr)

customer <- read.csv("Analisis excel/Youtube/5 soal/Customer.csv")
print(head(customer))

order <- read.csv("Analisis excel/Youtube/5 soal/Orders.csv")
order$Order.Date <- as.Date(order$Order.Date, "%m/%d/%Y")
print(head(order))

# Inner join customer and order data frames
df <- inner_join(customer, order, by = "Customer.ID", relationship ="many-to-many")
filter <- order %>% group_by(Customer.ID) %>% summarise(first_order = min(Order.Date))

df <- df[df$Order.Date %in% filter$first_order,]
print(df)

hasil <- df %>% group_by(City, Order.Date) %>% summarise(total_pembeli = n()) %>% arrange(desc(total_pembeli))
print(hasil)
print(dim(hasil))
hasil2 <- df %>% group_by(City, Order.Date) %>% summarise(total_pembeli = n_distinct(Customer.ID)) %>% arrange(desc(total_pembeli))
print(hasil2, n=20)
print(dim(hasil2))