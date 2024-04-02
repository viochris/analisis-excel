library("readxl")
library(openxlsx)
library(dplyr)
library(tidyr)
library(tibble)
library(ggplot2)
library(tidyverse)

df <- read_xlsx('Tes Excel Shopee Data Analyst.xlsx', sheet = 'Test', range='B1:B16')
df_asal <- read_xlsx('Tes Excel Shopee Data Analyst.xlsx', sheet = 'Database')

print(df)
print(head(df_asal))

df1 <- inner_join(df, df_asal[, c('CUSTOMER CODE', 'CUSTOMER NAME', 'Tax')], by = c('Customer Code' = 'CUSTOMER CODE'), relationship = "many-to-many")
# df1 <- merge(df, df_asal[, c('CUSTOMER CODE', 'CUSTOMER NAME', 'Tax')], by.x = 'Customer Code', by.y = 'CUSTOMER CODE')
df1 <- distinct(df1, `Customer Code`, .keep_all = TRUE)
print(df1)


# df2 <- inner_join(df[, 'Customer Code'], df_asal[, c('CUSTOMER CODE', 'BOX QTY', 'TOTAL WEIGHT')], by = c('Customer Code' = 'CUSTOMER CODE'), relationship = "many-to-many")
df2 <- merge(df[, 'Customer Code'], df_asal[, c('CUSTOMER CODE', 'BOX QTY', 'TOTAL WEIGHT')], by.x = 'Customer Code', by.y= 'CUSTOMER CODE')
df2 <- df2 %>% group_by(`Customer Code`) %>% summarise(box_qty = sum(`BOX QTY`), tweight = sum(`TOTAL WEIGHT`))
print(df2)


# df <- merge(df1, df2, by = 'Customer Code')
df <- inner_join(df1, df2, by = 'Customer Code')
print(df)
df$total_qty <- df$box_qty * 100000
df$total_weight <- df$tweight * 1000000
tax <- function(x){
    if(x == 'PKP'){
        return(0.1)
    }
    else if(x == 'PTKP'){
        return(0)
    }else {
        return (0)
    }
}
df$pajak <- sapply(df$Tax, tax)
total <- function(x,y,z){
    hasil = x+y+((x+y)*z)
    return(hasil)
}
df$total_akhir <- mapply(total, df$total_qty, df$total_weight, df$pajak)
print(df)

pivot <- df_asal %>% group_by(AREA, `CUSTOMER NAME`) %>% summarise(box_qty = sum(`BOX QTY`), tweight = sum(`TOTAL WEIGHT`))
print(pivot)


# pivot1 <- ftable(xtabs(cbind(`BOX QTY`, `TOTAL WEIGHT`) ~ AREA + `CUSTOMER NAME`, data = df_asal))
# print(pivot1)

