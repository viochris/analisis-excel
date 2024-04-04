library(arules) # For association rule mining
library(dplyr) # For data manipulation
library(tidyverse) # Collection of useful R packages
library("readxl")
library(openxlsx)
library(tibble)
library(ggplot2)
library(readr) # For CSV reading
library(lubridate)

df <- read_csv('bread basket.csv')
print(head(df))
cat('\n')
print(str(df))
cat('\n')
print(summary(df))
cat('\n')
df$date_time <- ymd_hm(df$date_time)
# df$month <- factor(month(df$date_time), levels = 1:12, labels = c('jan','feb','march','apr','may','june','july','august','sept','okt','nov','dec'))
df$month <- dplyr::recode(month(df$date_time), "jan", "feb", "march", "apr", "may", "june", "july", "august", "sept", "okt", "nov", "dec")
print(head(df))
print(distinct(df, Item))
cat('\n\n')
print(distinct(df, period_day))
cat('\n\n')
print(distinct(df, weekday_weekend))
cat('\n\n')

print(unique(df$Item))
cat('\n\n')
print(unique(df$period_day))
cat('\n\n')
print(unique(df$weekday_weekend))
cat('\n\n')
print(unique(df$Item))
cat('\n\n')
print(unique(df$period_day))
cat('\n\n')
print(unique(df$weekday_weekend))
cat('\n\n')

tabel_baru <- df %>% group_by(Transaction, Item) %>% summarise(jumlah = n())
print(head(tabel_baru))

tabel_pivot <- xtabs(jumlah ~ Transaction + Item, data = tabel_baru)
tabel_pivot[is.na(tabel_pivot)] <- 0

kosong <- function(x){
    if (x > 0){
        return (TRUE)
    }else if (x == 0){
        return(FALSE)
    }
}
tabel_pivot <- apply(tabel_pivot, c(1,2), kosong)

transaksi <- as(tabel_pivot, 'transactions')

tabel_apriori <- apriori(transaksi, support=0.015, target = 'frequent')
inspect(tabel_apriori)


hasil <- apriori(transaksi, support=0.015,conf = 0.5 ,target = 'rules')
inspect(hasil)
hasil <- sort(hasil, by = 'confidence', decreasing = TRUE)
inspect(hasil)
inspect(head(hasil, n = 11, by='confidence'))