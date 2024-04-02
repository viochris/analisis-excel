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

df <- merge(df1, df2, by = "customer_id", all = TRUE, na.strings = c("", "NA", " ", "N/A", "NULL"))
print(df)

cat("\n\n")
print("Cara 1")
# hasil <- df[is.na(df$order_id), ]
# hasil <- filter(df, is.na(order_id))
hasil <- df %>% filter(is.na(order_id))
print(hasil)

cat("\n\n")
print("Cara 2")
hasil_lain <- df[complete.cases(df), ]
print(hasil_lain)
hasil_lain <- df[rowSums(is.na(df)) == 0,]
print(hasil_lain)
hasil_lain <- df[,colSums(is.na(df)) == 0]
print(hasil_lain)
cat("\n\n")
hasil_lain <- df[!complete.cases(df), ]
print(hasil_lain)
cat("\n\n\n\n")
print(df[rowSums(is.na(df)) > 0, ])
print(ncol(df))
print(nrow(df))
print(rowSums(is.na(df)))
print(df[rowSums(is.na(df)) < ncol(df), ])
print(df[rowSums(is.na(df)) == ncol(df), ])
print(df[,colSums(is.na(df)) < nrow(df) ])
print(df[,colSums(is.na(df)) == nrow(df) ])

cat('\n\n\n\n')
print('Cara lainnya col')

df4 <- df[,colSums(is.na(df))==0]
print(df4)
df5 <- df[, !colSums(is.na(df) > 0)]
print(df5)
df5 <- df[, colSums(is.na(df)) >0]
print(df5)
df4 <- df[,!colSums(is.na(df))==0]
print(df4)

cat('\n\n\n\n')
print('Cara lainnya row')
df5 <- df[rowSums(is.na(df)) >0, ]
print(df5)
df5 <- df[rowSums(is.na(df)) ==0, ]
print(df5)
df5 <- df[!rowSums(is.na(df)) >0, ]
print(df5)
df5 <- df[!rowSums(is.na(df)) ==0, ]
print(df5)

cat("\n\n")
hasil <- colSums(is.na(df))
print(hasil)
