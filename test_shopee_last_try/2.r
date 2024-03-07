library(dplyr)
library(tidyr)

customer <- read.csv("Analisis excel/Youtube/5 soal/Customer.csv")
customer <- customer %>% group_by(City) %>% reframe(Customer.ID = unique(Customer.ID))
# customer <- customer %>% group_by(City) %>% summarise(Customer_ID = list(unique(Customer.ID))) %>% unnest(cols = Customer_ID)
print(head(customer))

order <- read.csv("Analisis excel/Youtube/5 soal/Orders.csv")
print(head(order))
cat('\n')


# Inner join customer and order data frames
hasil1 <- inner_join(customer, order, by = "Customer.ID", relationship ="many-to-many")
print(head(hasil1))

cat("\n\n")

# Alternative approach using merge
hasil2 <- merge(customer, order, by = "Customer.ID", all = FALSE)
print(head(hasil2))

hasil_akhir <- hasil1 %>% group_by(City) %>% summarise(jumlah = n()) 
print(hasil_akhir)

hasil_akhir <- hasil2 %>% group_by(City) %>% summarise(jumlah = n()) 
print(hasil_akhir)