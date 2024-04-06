library(dplyr)
library(lubridate)

customer <- read.csv("test_shopee_all/Customer.csv")


order <- read.csv("test_shopee_all/Orders.csv")
# order$Order.Date <- as.Date(order$Order.Date, format = '%m/%d/%Y')
order$Order.Date <- mdy(order$Order.Date)
order <- order %>%
    group_by(Customer.ID) %>%
    summarise(pembelian_awal = min(Order.Date)) %>%
    arrange(Customer.ID)


print(head(customer))
print(head(order))
cat("\n\n\n")

hasil <- merge(customer, order, by = "Customer.ID")
print(head(hasil))

hasil_akhir <- hasil %>%
    group_by(City, pembelian_awal) %>%
    summarize(jumlah = n()) %>%
    arrange(desc(jumlah))
print(head(hasil_akhir))
print(tail(hasil_akhir))
