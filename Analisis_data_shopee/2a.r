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

df <- inner_join(df_od, df_sd, by = c("sku_id" = "id"))
df$order_date <- as.Date(df$order_date)
df <- filter(df, is_valid == 1)

tabel21 <- df[year(df$order_date) == 2021, ]
tabel21 <- tabel21 %>%
    group_by(category) %>%
    summarise(jumlah21 = sum(qty_ordered))
tabel22 <- df[year(df$order_date) == 2022, ]
tabel22 <- tabel22 %>%
    group_by(category) %>%
    summarise(jumlah22 = sum(qty_ordered))
tabel_akhir <- merge(tabel21, tabel22, by = "category")
tabel_akhir$perbedaan <- tabel_akhir$jumlah22 - tabel_akhir$jumlah21
tabel_akhir <- tabel_akhir %>% mutate(
    penjelasan = case_when(
        perbedaan > 0 ~ "Naik",
        perbedaan < 0 ~ "Turun",
        .default = NULL
    )
) %>% arrange(perbedaan)
print(tabel_akhir)
cat('\n\n\n\n\n\n\n')



print('tabel khusus kategori others')
df <- filter(df, category == 'Others')
tabel21 <- df[year(df$order_date) == 2021, ]
tabel21 <- tabel21 %>%
    group_by(sku_name) %>%
    summarise(jumlah21 = sum(qty_ordered))
tabel22 <- df[year(df$order_date) == 2022, ]
tabel22 <- tabel22 %>%
    group_by(sku_name) %>%
    summarise(jumlah22 = sum(qty_ordered))
tabel_akhir <- merge(tabel21, tabel22, by = "sku_name", all = TRUE)
tabel_akhir[is.na(tabel_akhir)] <- 0
tabel_akhir$perbedaan <- tabel_akhir$jumlah22 - tabel_akhir$jumlah21
tabel_akhir <- tabel_akhir %>% mutate(
    penjelasan = case_when(
        perbedaan > 0 ~ "Naik",
        perbedaan < 0 ~ "Turun",
        .default = NULL
    )
) %>% arrange(perbedaan)
print(head(tabel_akhir, 20))