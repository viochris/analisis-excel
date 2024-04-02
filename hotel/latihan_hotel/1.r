library(dplyr)
library(tidyverse)

df_hotel <- read.csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv', na.strings = c("", "NA", " ", "N/A", "NULL"))
# Assuming df_hotel is your data frame
df_hotel <- df_hotel %>% mutate(ID = row_number()) %>% select(ID, everything())


check <- function(df){
    hasil <- data.frame(
        nama = colnames(df),
        dtypes = sapply(df, class),
        null = colSums(is.na(df)),
        null2 = sapply(df, function(x) sum(is.na(x))),
        nullpct = paste0(round(colSums(is.na(df)) / dim(df)[1], 2), '%'),
        nullpct2 = paste0(round(colSums(is.na(df)) / length(df$ID), 2), '%'),
        nullpct3 = paste0(round(colMeans(is.na(df)), 2), '%'),
        nullpct4 = paste0(round(sapply(df, function(x) mean(is.na(x))), 2), '%'),
        unique1 = sapply(df, function(x) length(unique(x))),
        unique2 = sapply(df, function(x) length(unique(na.omit(x)))),
        unique3 = sapply(df, function(x) length(unique(x[!is.na(x)])))
    )
    return (hasil)
}



hasil <- check(df_hotel)
print(hasil)