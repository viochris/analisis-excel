library(arules) # For association rule mining
library(dplyr) # For data manipulation
library(tidyverse) # Collection of useful R packages
library("readxl")
library(openxlsx)
library(tibble)
library(ggplot2)
library(readr) # For CSV reading
library(lubridate)






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

df$month3 <- ifelse(df$months == 1, "jan",
                    ifelse(df$months == 2, "feb",
                            ifelse(df$months == 3, "march",
                                    ifelse(df$months == 4, "apr",
                                            ifelse(df$months == 5, "may",
                                                ifelse(df$months == 6, "june",
                                                        ifelse(df$months == 7, "july",
                                                                ifelse(df$months == 8, "august",
                                                                        ifelse(df$months == 9, "sept",
                                                                            ifelse(df$months == 10, "okt",
                                                                                    ifelse(df$months == 11, "nov",
                                                                                            ifelse(df$months == 12, "dec",
                                                                                                    NA))))))))))))


# # Membuat vektor penggantian string
# "1": Ini adalah pola regex yang tidak mengikat kedua ujung string. Dengan kata 
# lain, itu akan mencocokkan setiap angka 1 yang ada di dalam string, tidak peduli apakah itu berdiri 
# sendiri atau di dalam angka lain, seperti "10" atau "21".

# "^1$": Ini adalah pola regex yang menggunakan ^ untuk menandakan awal string dan $ untuk menandakan 
# akhir string. Dengan menggunakan kedua tanda ini, kita memaksa pola hanya mencocokkan kasus di mana angka 
# 1 itu sendiri adalah satu-satunya karakter dalam string, dan tidak terdapat di dalam angka lain.
REPLACE_STR <- c(
    "^1$" = "jan", "2" = "feb", "3" = "mar", "4" = "apr",
    "5" = "may", "6" = "jun", "7" = "jul", "8" = "aug",
    "9" = "sep", "10" = "okt", "11" = "nov", "12" = "dec"
)
# REPLACE_STR <- c(
#     "^1$" = "jan", "^2$" = "feb", "^3$" = "mar", "^4$" = "apr",
#     "^5$" = "may", "^6$" = "jun", "^7$" = "jul", "^8$" = "aug",
#     "^9$" = "sep", "^10$" = "okt", "^11$" = "nov", "^12$" = "dec"
# )
df$month1 <- str_replace_all(df$months, REPLACE_STR)
df <- df %>% mutate(
    month2 = str_replace_all(months, REPLACE_STR)
)



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
#xtabs(values ~ x + y) atau xtabs(values ~ baris+kolom)
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
# print('sebelum:')
# print(class(tabel_pivot))

# # Membuat objek transaksi dari tabel pivot
transaksi <- as(tabel_pivot, "transactions")
# print('sesudah: ')
# print(class(tabel_pivot))

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
