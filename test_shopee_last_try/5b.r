library(dplyr)
library(tidyr)

customer <- read.csv("Analisis excel/Youtube/5 soal/Customer.csv")
print(head(customer))

order <- read.csv("Analisis excel/Youtube/5 soal/Orders.csv")
order$Order.Date <- as.Date(order$Order.Date, "%m/%d/%Y")
print(head(order))


# Inner join customer and order data frames
hasil1 <- inner_join(customer, order, by = "Customer.ID", relationship ="many-to-many")

filter <- order %>% group_by(Customer.ID) %>% summarise(first_order = min(Order.Date))
df <- inner_join(hasil1, filter, by = "Customer.ID", relationship ="many-to-many") %>% filter(first_order == Order.Date)
print(head(df))

hasil <- subset(df, select = c(Customer.ID, Sales)) %>% arrange(Customer.ID)
print(head(hasil))
print(dim(hasil))

cat("\n")
hasil2 <- df %>%
    group_by(Customer.ID) %>%
    summarise(total = list(unique(Sales))) %>%
    unnest(total) %>%
    arrange(Customer.ID)
print(head(hasil2))
print(dim(hasil2))