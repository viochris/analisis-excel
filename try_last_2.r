library(arules) # For association rule mining
library(dplyr) # For data manipulation
library(tidyverse) # Collection of useful R packages
library("readxl")
library(openxlsx)
library(tibble)
library(ggplot2)
library(readr) # For CSV reading
library(lubridate)

df <- read.csv('bread basket.csv')
print(head(df))
cat('\n\n\n')
print(summary(df))
cat('\n\n\n')
print(str(df))
cat('\n\n')

df$date_time <- dmy_hm(df$date_time)
df$month <- factor(month(df$date_time), levels = 1:12, labels=c("jan", "feb", "march", "apr", "may", "june", "july", "august", "sept", "okt", "nov", "dec"))
df$month1 <- dplyr::recode(month(df$date_time), "jan", "feb", "march", "apr", "may", "june", "july", "august", "sept", "okt", "nov", "dec")
REPLACE_STR <- c(
    "^1$" = "jan", "2" = "feb", "3" = "mar", "4" = "apr",
    "5" = "may", "6" = "jun", "7" = "jul", "8" = "aug",
    "9" = "sep", "10" = "okt", "11" = "nov", "12" = "dec"
)
df$month2 <- str_replace_all(month(df$date_time), REPLACE_STR)
print(head(df))

cat('\n\n\n')
print(unique(df$Item))
cat('\n\n\n')
print(unique(df$period_day))
cat('\n\n\n')
print(unique(df$weekday_weekend))
cat('\n\n\n')
print(distinct(df, Item))
cat('\n\n\n')
print(distinct(df, period_day))
cat('\n\n\n')
print(distinct(df, weekday_weekend))
cat('\n\n')


tabel_baru <- df %>% group_by(Transaction, Item) %>% summarise(Jumlah = n())
print(head(tabel_baru))
tabel_pivot <- xtabs(data=tabel_baru, Jumlah ~ Transaction + Item)
tabel_pivot[is.na(tabel_pivot)] <- 0
ubah <- function(x){
    if(x > 0 ){
        return(TRUE)
    }else if (x == 0){
        return(FALSE)
    }
}
tabel_pivot <- apply(tabel_pivot, c(1,2), ubah)
print(tabel_pivot)
transaksi <- as(tabel_pivot, 'transactions')
tabel_apriori <- apriori(transaksi, support = 0.015, target ='frequent')
inspect(tabel_apriori)
cat('\n\n')
tabel_rules <- apriori(transaksi, support = 0.015, conf = 0.5, target='rules')
inspect(tabel_rules)
tabel_rules <- sort(tabel_rules, by='confidence',decreasing = TRUE)
inspect(tabel_rules)
inspect(head(tabel_rules, n = 11, by='confidence'))