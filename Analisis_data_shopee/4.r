library(RMySQL)
library(dplyr)
library(tidyr)
library(lubridate)
library(tidyverse)

path_od <- "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/order_detail.csv"
path_pd <- "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/payment_detail.csv"
path_cd <- "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/customer_detail.csv"
path_sd <- "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/sku_detail.csv"
df_od <- read.csv(path_od)
df_pd <- read.csv(path_pd)
df_cd <- read.csv(path_cd)
df_sd <- read.csv(path_sd)

df <- df_od
df$order_date <- as.Date(df$order_date)
df <- df[df$is_valid == 1, ]
df <- filter(df, year(order_date) == 2022, month(order_date) %in% c(10, 11, 12))
# df$month <- as.character(month(df$order_date))
# df$month <- gsub("10", "Oktober", df$month)
# df$month <- gsub("11", "November", df$month)
# df$month <- gsub("12", "Desember", df$month)

# df$month <- month(df$order_date)
# df$month <- gsub(10, "Oktober", df$month)
# df$month <- gsub(11, "November", df$month)
# df$month <- gsub(12, "Desember", df$month)


# df$month <- as.character(month(df$order_date, label = TRUE))
# df$month <- month(df$order_date, label=TRUE)


# df <- df %>% mutate(
#     month = case_when(
#         month(order_date) == 10 ~ "Oktober",
#         month(order_date) == 11 ~ "November",
#         month(order_date) == 12 ~ "Desember",
#         TRUE ~ as.character(month(order_date, label = TRUE))
#     )
# )
# df$month <- factor(month(df$order_date), levels = 10:12, labels = c("Oktober", "November", "Desember"))
# print(head(df))

df$month <- str_replace_all(month(df$order_date), c("10" = "Oktober", "11" = "November", "12" = "Desember"))

weekday <- df[weekdays(df$order_date) %in% c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"), ]
weekday <- weekday %>%
    group_by(month) %>%
    summarise(weekday = round(mean(before_discount), 2))


weekend <- filter(df, weekdays(df$order_date) %in% c("Saturday", "Sunday"))
weekend <- weekend %>%
    group_by(month) %>%
    summarise(weekend = round(mean(before_discount), 2))

hasil <- inner_join(weekday, weekend, by = "month", relationship = "many-to-many")

hasil$beda <- hasil$weekend - hasil$weekday
hasil$persentase <- round(hasil$beda / hasil$weekend, 2)
print(hasil)


# barplot(
#     as.matrix(c(hasil$weekday, hasil$weekend)),
#     beside = TRUE,
#     col = c("blue", "green"),
#     xlab = "Bulan", ylab = "Penjualan",
#     main = "Diagram Penjualan Weekdays vs Weekend In 2022",
#     width = 0.2,  # Lebar setiap batang
#     space = c(2, 0.5, 0.5, 0.5, 0.5, 0.5)  # Jarak antara setiap dua set batang (disesuaikan sesuai kebutuhan)
# )

barplot(
    rbind(hasil$weekday, hasil$weekend),
    beside = TRUE,
    col = c("blue", "red"),
    names.arg = c("Desember", "November", "Oktober"),
    ylim = c(0, max(hasil$weekday, hasil$weekend) + 5), # Menyesuaikan batas atas sumbu y
    xlab = "Bulan", ylab = "Penjualan",
    main = "Diagram Penjualan Weekdays vs Weekend In 2022"
)
legend(
    "top", # Letakkan legenda di sudut kanan atas
    legend = c("Weekdays", "Weekend"), # Label untuk setiap set
    fill = c("blue", "red") # Warna yang sesuai untuk setiap set
)
