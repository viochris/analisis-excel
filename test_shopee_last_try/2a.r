library(dplyr)

customer <- read.csv("Youtube/5 soal/Customer.csv")
customer <- customer %>% distinct(City, Customer.ID, .keep_all = TRUE)


print(head(customer))

order <- read.csv("Youtube/5 soal/Orders.csv")
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