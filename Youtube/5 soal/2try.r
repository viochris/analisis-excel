library(dplyr)
library(tidyr)

customer <- read.csv("Youtube/5 soal/Customer.csv")
customer <- customer %>% distinct(City, Customer.ID) %>% arrange(desc(City))
print(head(customer))

# order <- read.csv("Youtube/5 soal/Orders.csv")
# print(head(order))
# cat('\n')

# hasil1 <- inner_join(customer, order, by = "Customer.ID", relationship ="many-to-many")
# print(head(hasil1))
# hasil_akhir <- hasil1 %>% group_by(City) %>% summarise(jumlah = n()) 
# print(hasil_akhir)