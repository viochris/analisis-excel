library(dplyr)

order <- read.csv("Analisis excel/Youtube/5 soal/Orders.csv")
order$Order.Date <- as.Date(order$Order.Date, "%m/%d/%Y")
order$Ship.Date <- as.Date(order$Ship.Date, "%m/%d/%Y")
print(head(order))

hasil <- order %>% group_by(Customer.ID) %>% summarise(first_order = min(Order.Date))
print(hasil)
