library("readxl")
library(openxlsx)
library(dplyr)
library(tidyr)
library(tibble)
library(ggplot2)
library(tidyverse)

df <- read_xlsx('Tes Excel Shopee Data Analyst.xlsx', sheet = 'Test',range = 'B1:B16')
df_asal <- read_xlsx('Tes Excel Shopee Data Analyst.xlsx', sheet = 'Database')
print(df)
print(df_asal)

tabel1 <- inner_join(df, df_asal[c('CUSTOMER CODE', 'CUSTOMER NAME', 'Tax')], by = c('Customer Code'='CUSTOMER CODE'))
# tabel1 <- tabel1 %>% distinct(`Customer Code`, .keep_all = TRUE)
tabel1 <- tabel1[!duplicated(tabel1$`Customer Code`), ]
print(tabel1)

tabel2 <- inner_join(df[c('Customer Code')], df_asal[c('CUSTOMER CODE', 'BOX QTY', 'TOTAL WEIGHT')], by = c('Customer Code'='CUSTOMER CODE'))
tabel2 <- tabel2 %>% group_by(`Customer Code`) %>% summarise(box_qty = sum(`BOX QTY`), totalw = sum(`TOTAL WEIGHT`))
print(tabel2)

df <- inner_join(tabel1, tabel2, by = 'Customer Code', relationship = 'many-to-many')
print(df)


df$totalqty <- df$box_qty * 100000
df$totalweightall <- df$totalw * 1000000
tax <- function(x){
    if (x == 'PKP'){
        return (0.1)
    }else if(x == 'PTKP'){
        return(0)
    }else{
        return
    }
}
df$taxpct <- sapply(df$Tax, tax)
total <- function(x, y, z){
    hasil = x+y+((x+y)*z)
    return (hasil)
}
df$total <- mapply(total, df$totalqty, df$totalweightall, df$taxpct)
print(df)

pivot <- df_asal %>% group_by(`AREA`,`CUSTOMER NAME`) %>% summarise(box_qty = sum(`BOX QTY`), totalw = sum(`TOTAL WEIGHT`))
print(head(pivot))
print(tail(pivot))


# pivot <- xtabs(cbind(`BOX QTY`, `TOTAL WEIGHT`) ~ AREA + `CUSTOMER NAME`, data = df_asal)
# print(pivot)
# pivot <- ftable(xtabs(cbind(`BOX QTY`, `TOTAL WEIGHT`) ~ AREA + `CUSTOMER NAME`, data = df_asal))
# print(pivot)