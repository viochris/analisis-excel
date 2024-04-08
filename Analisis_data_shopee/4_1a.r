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

df <- df_od
df$order_date <- ymd(df$order_date)
df <- filter(df, is_valid == 1, year(order_date) == 2022, month(order_date) %in% c(10:12))
df$month <- factor(month(df$order_date), levels = 10:12, labels = c("oktober", "november", "desember"))
print(head(df))

days <- filter(df, weekdays(order_date) %in% c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))
days <- days %>%
    group_by(month) %>%
    summarise(rata_days = mean(before_discount))
end <- df[weekdays(df$order_date) %in% c("Saturday", "Sunday"), ]
end <- end %>%
    group_by(month) %>%
    summarise(rata_end = mean(before_discount))
tabel <- merge(days, end, by = "month")
tabel <- tabel %>% arrange(month)
tabel$beda <- tabel$rata_end - tabel$rata_days
tabel$persentase <- tabel$beda / tabel$rata_end * 100
print(tabel)

barplot(
    rbind(tabel$rata_days, tabel$rata_end),
    beside = TRUE,
    col = c("blue", "red"),
    names.arg = c("Desember", "November", "Oktober"),
    ylim = c(0, max(tabel$rata_days, tabel$rata_end) + 5), # Menyesuaikan batas atas sumbu y
    xlab = "Bulan", ylab = "Penjualan",
    main = "Diagram Penjualan Weekdays vs Weekend In 2022"
)
legend(
    "top", # Letakkan legenda di sudut kanan atas
    legend = c("Weekdays", "Weekend"), # Label untuk setiap set
    fill = c("blue", "red") # Warna yang sesuai untuk setiap set
)