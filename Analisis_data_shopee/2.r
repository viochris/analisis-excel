library(RMySQL)
library(dplyr)
library(tidyr)
library(lubridate)

path_od <- "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/order_detail.csv"
path_pd <- "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/payment_detail.csv"
path_cd <- "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/customer_detail.csv"
path_sd <- "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/sku_detail.csv"
df_od <- read.csv(path_od)
df_pd <- read.csv(path_pd)
df_cd <- read.csv(path_cd)
df_sd <- read.csv(path_sd)


df <- inner_join(df_od, df_sd, by = c("sku_id" = "id"), relationship = "many-to-many")
df <- df[df$is_valid == 1, ]
df$order_date <- as.Date(df$order_date)

print(head(df))

tabel21 <- df[year(df$order_date) == 2021, ]
tabel21 <- tabel21 %>%
    group_by(category) %>%
    summarise(jumlah21 = sum(qty_ordered))


tabel22 <- filter(df, year(order_date) == 2022)
tabel22 <- tabel22 %>%
    group_by(category) %>%
    summarise(jumlah22 = sum(qty_ordered))


hasil <- inner_join(tabel21, tabel22, by = "category", relationship = "many-to-many")


beda <- function(x, y) {
    return(y - x)
}
# hasil$perbedaan <- hasil$jumlah22 - hasil$jumlah21
# hasil$perbedaan <- beda(hasil$jumlah21, hasil$jumlah22)
# hasil <- hasil %>% mutate(perbedaan = beda(jumlah21, jumlah22))
hasil <- hasil %>% mutate(perbedaan = jumlah22 - jumlah21)



ket <- function(x) {
    if (x > 0) {
        return("Naik")
    } else if (x < 0) {
        return("Turun")
    } else {
        return("Tetap")
    }
}
hasil$keterangan <- sapply(hasil$perbedaan, ket)

hasil <- arrange(hasil, perbedaan)
print(hasil)


print("Dari Kategori Others")
df <- filter(df, category == "Others")

tabel21 <- df[year(df$order_date) == 2021, ]
tabel21 <- tabel21 %>%
    group_by(sku_name) %>%
    summarise(jumlah21 = sum(qty_ordered))

tabel22 <- filter(df, year(order_date) == 2022)
tabel22 <- tabel22 %>%
    group_by(sku_name) %>%
    summarise(jumlah22 = sum(qty_ordered))
hasil <- full_join(tabel21, tabel22, by = "sku_name", relationship = "many-to-many")
print(colSums(is.na(hasil)))
print(colMeans(is.na(hasil)))
hasil[is.na(hasil)] <- 0
print(colSums(is.na(hasil)))
print(colMeans(is.na(hasil)))

hasil <- hasil %>% mutate(perbedaan = jumlah22 - jumlah21)
hasil$keterangan <- sapply(hasil$perbedaan, ket)

hasil <- arrange(hasil, perbedaan)
print(hasil)
