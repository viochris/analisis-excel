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

# print(head(df1))
# cat("\n")
# print(head(df2))
# cat("\n\n")

df <- merge(df1, df2, by = "customer_id", all = TRUE, na.strings = c("", "NA", " ", "N/A", "NULL"))
print(df)

cat("\n\n")
print("Cara 1")
hasil <- df[is.na(df$order_id), ]
print(hasil)
hasil <- df[!is.na(df$order_id), ]
print(hasil)
hasil <- filter(df, is.na(order_id))
print(hasil)
hasil <- filter(df, !is.na(order_id))
print(hasil)
hasil <- df %>% filter(is.na(order_id))
print(hasil)
hasil <- df %>% filter(!is.na(order_id))
print(hasil)
cat('\n\n\n\n')


print('Cara 2')
hasil <- df[, colSums(is.na(df)) < (nrow(df)/2)]
print(hasil)
hasil <- df[, colSums(is.na(df)) < (nrow(df)*0.5)]
print(hasil)
hasil <- df[, colMeans(is.na(df)) < 0.5]
print(hasil)
hasil <- df[, colMeans(is.na(df))*100 < 50]
print(hasil)
hasil <- df[, !colSums(is.na(df)) > (nrow(df)/2)]
print(hasil)
hasil <- df[, !colSums(is.na(df)) > (nrow(df)*0.5)]
print(hasil)
hasil <- df[, !colMeans(is.na(df)) > 0.5]
print(hasil)
hasil <- df[, !colMeans(is.na(df)) * 100 > 50]
print(hasil)
cat('\n\n\n\n')


print('Cara 2 Untuk melihat Null')
hasil <- df[, !colSums(is.na(df)) < (nrow(df)/2)]
print(hasil)
hasil <- df[, !colSums(is.na(df)) < (nrow(df)*0.5)]
print(hasil)
hasil <- df[, !colMeans(is.na(df)) < 0.5]
print(hasil)
hasil <- df[, !colMeans(is.na(df)) < 50]
print(hasil)
hasil <- df[, colSums(is.na(df)) > (nrow(df)/2)]
print(hasil)
hasil <- df[, colSums(is.na(df)) > (nrow(df)*0.5)]
print(hasil)
hasil <- df[, colMeans(is.na(df)) > 0.5]
print(hasil)
hasil <- df[, colMeans(is.na(df))*100 > 50]
print(hasil)
cat('\n\n\n\n')


print('Cara 3')
hasil <- df[rowSums(is.na(df)) < (ncol(df)/2),]
print(hasil)
hasil <- df[rowSums(is.na(df)) < (ncol(df)*0.5),]
print(hasil)
hasil <- df[rowMeans(is.na(df)) < 0.5, ]
print(hasil)
hasil <- df[rowMeans(is.na(df))*100 < 50, ]
print(hasil)
hasil <- df[!rowSums(is.na(df)) > (ncol(df)/2),]
print(hasil)
hasil <- df[!rowSums(is.na(df)) > (ncol(df)*0.5),]
print(hasil)
hasil <- df[!rowMeans(is.na(df)) > 0.5, ]
print(hasil)
hasil <- df[!rowMeans(is.na(df))* 100 > 50, ]
print(hasil)

cat('\n\n\n\n')
print('Cara 3 Lihat Yang Null')
hasil <- df[!rowSums(is.na(df)) < (ncol(df)/2),]
print(hasil)
hasil <- df[!rowSums(is.na(df)) < (ncol(df)*0.5),]
print(hasil)
hasil <- df[!rowMeans(is.na(df)) < 0.5, ]
print(hasil)
hasil <- df[!rowMeans(is.na(df))*100 < 50, ]
print(hasil)
hasil <- df[rowSums(is.na(df)) > (ncol(df)/2),]
print(hasil)
hasil <- df[rowSums(is.na(df)) > (ncol(df)*0.5),]
print(hasil)
hasil <- df[rowMeans(is.na(df)) > 0.5, ]
print(hasil)
hasil <- df[rowMeans(is.na(df))*100 > 50, ]
print(hasil)