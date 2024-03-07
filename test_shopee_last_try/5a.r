library(dplyr)
library(tidyr)

order <- read.csv("Analisis excel/Youtube/5 soal/Orders.csv")
order$Order.Date <- as.Date(order$Order.Date, "%m/%d/%Y")
tanggal <- order %>%
    group_by(Customer.ID) %>%
    summarise(first_order = min(Order.Date))

df <- inner_join(order, tanggal, by = "Customer.ID") %>% filter(Order.Date == first_order)
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
