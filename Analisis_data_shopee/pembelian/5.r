library(RMySQL)
library(dplyr)
library(lubridate)

# Ganti 'dbname', 'username', 'password', dan 'host' sesuai dengan informasi database Anda
con <- dbConnect(MySQL(), dbname = "pembelian", user = "root", password = "", host = "localhost")

query <- "SELECT * FROM salesman"
df <- dbGetQuery(con, query)
dbDisconnect(con)

print(df)

hasil <- select(df, c(salesman_name, commision))
hasil <- select(df, salesman_name, commision)
print(hasil)
hasil <- arrange(hasil, desc(commision))
print(hasil)
print(head(hasil, 1))