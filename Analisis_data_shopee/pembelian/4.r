library(RMySQL)
library(dplyr)
library(tidyr)
library(lubridate)

# Ganti 'dbname', 'username', 'password', dan 'host' sesuai dengan informasi database Anda
con <- dbConnect(MySQL(), dbname = "pembelian", user = "root", password = "", host = "localhost")

query1 <- "SELECT * FROM orders"
query2 <- "SELECT * FROM customers"

df1 <- dbGetQuery(con, query1)
df2 <- dbGetQuery(con, query2)
dbDisconnect(con)

print(head(df1))
cat("\n")
print(head(df2))
cat("\n\n")

df <- merge(df1, df2, by = 'customer_id', all=TRUE, na.strings = c("", "NA", " ", "N/A", "NULL"))
print(df)
cat("\n\n")

print(is.na(df$order_id))
print(sum(is.na(df$order_id)))
cat("\n\n")

hasil <- df  %>% group_by(customer_name) %>% summarise(jumlah = sum(!is.na(order_id))) %>% arrange(desc(jumlah))
print(hasil)