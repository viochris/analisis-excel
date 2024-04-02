library(RMySQL)
library(dplyr)
library(lubridate)

# Ganti 'dbname', 'username', 'password', dan 'host' sesuai dengan informasi database Anda
con <- dbConnect(MySQL(), dbname = "pembelian", user = "root", password = "", host = "localhost")

query <- "SELECT * FROM salesman"
df <- dbGetQuery(con, query)
dbDisconnect(con)

print(df)

hasil <- df[c('salesman_name', 'commision')]
hasil <- hasil %>% arrange(desc(commision))
print(hasil)
print(head(hasil, 1))



hasil1 <- select(df, salesman_name, commision)
hasil1 <- hasil1 %>% arrange(desc(commision))
print(hasil1)
print(head(hasil1, 1))