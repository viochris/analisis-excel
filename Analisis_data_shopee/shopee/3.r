library(RMySQL)
library(dplyr)
library(tidyr)
library(lubridate)

# Ganti 'dbname', 'username', 'password', dan 'host' sesuai dengan informasi database Anda
con <- dbConnect(MySQL(), dbname = "pembelian_shopee", user = "root", password = "", host = "localhost")

query1 <- "SELECT * FROM order_detail"
query2 <- "SELECT * FROM sku_detail"

df1 <- dbGetQuery(con, query1)
df2 <- dbGetQuery(con, query2)
dbDisconnect(con)

print(head(df1))
cat("\n")
print(head(df2))
cat("\n\n")

# df <- merge(df1, df2, by.x = "sku_id", by.y = "id", all=FALSE)
df <- inner_join(df1, df2, by = c("sku_id" = "id"), relationship = "many-to-many")
print(head(df))
cat("\n\n")

df <- df[df$is_valid == 1, ]
df$order_date <- as.Date(df$order_date)
print(head(df))



tabel2021 <- df %>% filter(year(order_date) == 2021)
tabel2021 <- tabel2021 %>%
    group_by(category) %>%
    summarise(total2021 = sum(after_discount))
print(head(tabel2021))

cat("\n\n")

tabel2022 <- filter(df, year(order_date) == 2022)
tabel2022 <- tabel2022 %>%
    group_by(category) %>%
    summarise(total2022 = sum(after_discount))
print(head(tabel2022))
cat("\n\n")



hasil <- merge(tabel2021, tabel2022, by = "category", all = FALSE)

pengurangan <- function(x, y) {
    return(y - x)
}
# hasil$perbedaan  <- pengurangan(hasil$total2021, hasil$total2022)
# hasil <- hasil %>% mutate(perbedaan = pengurangan(total2021, total2022))
hasil$perbedaan <- hasil$total2022 - hasil$total2021

penjelasan <- function(x) {
    if (x > 0) {
        return("Naik")
    } else if (x < 0) {
        return("Turun")
    } else {
        return("Tetap")
    }
}
hasil$penjelasan <- sapply(hasil$perbedaan, penjelasan)

hasil <- hasil %>% arrange(desc(perbedaan))
print(hasil)
