library(dplyr)

df <- read.csv("Analisis excel/Youtube/5 soal/Customer.csv")
print(head(df))

hasil <- df %>% group_by(City) %>% summarise(jumlah_customer = n_distinct(Customer.ID))
print(hasil)