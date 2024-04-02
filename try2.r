library(dplyr) # For data manipulation
library(tidyverse) # Collection of useful R packages
library("readxl")
library(openxlsx)
library(tibble)
library(ggplot2)
library(readr) # For CSV reading
library(arules) # For association rule mining



df <- read.csv("bread basket.csv")
print(head(df))
cat("\n\n")
print(summary(df))
cat("\n\n")
print(str(df))
df$date_time <- as.Date(df$date_time, format = "%d-%m-%Y")
# df$date_time <- as.POSIXct(df$date_time, format='%d-%m-%Y %H:%M')
# df$date_time <- dmy_hm(df$date_time)
df$months <- month(df$date_time)
print(head(df))
cat("\n\n")
df$month <- factor(df$months, levels = 1:12, labels = c("jan", "feb", "march", "apr", "may", "june", "july", "august", "sept", "okt", "nov", "dec"))


print(head(df))
print(sapply(df, class))
df$month1 <- dplyr::recode(df$months, "jan", "feb", "march", "apr", "may", "june", "july", "august", "sept", "okt", "nov", "dec")
print(head(df))


cat("\n\n")
print(distinct(df, Item))
print(distinct(df, period_day))
print(distinct(df, weekday_weekend))
cat("\n\n")
print(unique(df$Item))
print(unique(df$period_day))
print(unique(df$weekday_weekend))

tabel_baru <- df %>%
    group_by(Transaction, Item) %>%
    summarise(Jumlah = n())
# tabel_baru <- df %>% group_by(Transaction, Item) %>% summarise(Jumlah = n(), .groups = "drop")
print(tabel_baru)
cat("\n")
tabel_pivot <- xtabs(Jumlah ~ Transaction + Item, data = tabel_baru)
tabel_pivot[is.na(tabel_pivot)] <- 0
print(head(tabel_pivot))
cat("\n")

kosong <- function(x) {
    if (x > 0) {
        return(TRUE)
    } else if (x == 0) {
        return(FALSE)
    }
}
tabel_pivot <- apply(tabel_pivot, c(1, 2), kosong)
print(head(tabel_pivot))

# Membuat objek transaksi dari tabel pivot
transaksi <- as(tabel_pivot, "transactions")

# Melakukan analisis apriori
tabel_apriori <- apriori(transaksi, support = 0.015, target = "frequent")
# tabel_apriori <- apriori(transaksi, parameter = list(support = 0.015, target = "frequent"))
# print(tabel_apriori)
inspect(tabel_apriori)


# tabel_apriori <- apriori(transaksi, supp = 0.015, conf = 0.5, target = "rules")
tabel_apriori <- apriori(transaksi, support = 0.015, conf = 0.5, target = "rules")
# tabel_apriori <- arrange(tabel_apriori, desc(confidence))
tabel_apriori <- sort(tabel_apriori, by = "confidence", decreasing = TRUE)
# Menampilkan hasil analisis apriori
# print(tabel_apriori)
inspect(tabel_apriori)
inspect(head(tabel_apriori, n = 11, by = "confidence"))
