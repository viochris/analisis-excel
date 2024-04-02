library("readxl")
library(openxlsx)
library(dplyr)
library(tidyr)
library(tibble)
library(ggplot2)
library(tidyverse)

df <- read_xlsx('Tes Excel Shopee Data Analyst.xlsx', sheet = 'Test', range="B1:B16")
df_asal <- read_xlsx('Tes Excel Shopee Data Analyst.xlsx', sheet = 'Database')
print(df)
print(df_asal)

# hasil1 <- merge(df, df_asal[, c('CUSTOMER CODE', 'CUSTOMER NAME', 'Tax')], by.x = 'Customer Code', by.y='CUSTOMER CODE')
hasil1 <- inner_join(df, df_asal[, c('CUSTOMER CODE', 'CUSTOMER NAME', 'Tax')], by = c('Customer Code' = 'CUSTOMER CODE'))
hasil1 <- hasil1 %>% distinct(`Customer Code`, .keep_all = TRUE)
print(hasil1)


hasil2 <- inner_join(df[, 'Customer Code'], df_asal[, c('CUSTOMER CODE', 'BOX QTY', 'TOTAL WEIGHT')], by = c('Customer Code' = 'CUSTOMER CODE'))
hasil2 <- hasil2 %>% group_by(`Customer Code`) %>% summarise(box_qty = sum(`BOX QTY`), weight = sum(`TOTAL WEIGHT`))
print(hasil2)

df <- inner_join(hasil1, hasil2, by = 'Customer Code', relationship='many-to-many')
print(df)

df$price_qty <- df$box_qty*100000
df$totalW <- df$weight * 1000000
df <- df %>% mutate(
    pajak = case_when(
        Tax == 'PKP' ~ 0.1,
        Tax == 'PTKP' ~ 0,
        TRUE ~ 0
    )
)
total <- function(x,y,z){
    hasil = x+y+((x+y)*z)
    return(hasil)
}
df$total_akhir <- mapply(total, df$price_qty, df$totalW, df$pajak)
print(df)


pivot <- df_asal %>% group_by(AREA, `CUSTOMER NAME`) %>% summarise(box_qty = sum(`BOX QTY`), weight = sum(`TOTAL WEIGHT`)) %>% arrange(AREA)
print(head(pivot))
print(tail(pivot))



pivot_xtabs <- ftable(xtabs(cbind(`BOX QTY`, `TOTAL WEIGHT`) ~ AREA + `CUSTOMER NAME`, data = df_asal))
print(pivot_xtabs)
print(dim(pivot_xtabs))



write.xlsx(df, 'tes_shopee.xlsx')