library(dplyr)
library(tidyverse)
library(ggplot2)

df_hotel <- read.csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv", na.strings = c("", "NA", " ", "N/A", "NULL"))
df_hotel <- df_hotel %>%
    mutate(ID = row_number()) %>%
    select(ID, everything())
df_hotel$id <- rownames(df_hotel)
# df_hotel$id2 <- rownames_to_column(df_hotel) tidak bisa


check <- function(df) {
    data <- data.frame(
        Nama = colnames(df),
        Dtypes = sapply(df, class),
        Null1 = colSums(is.na(df)),
        Null2 = sapply(df, function(x) sum(is.na(x))),
        Nullpct1 = paste(round(colSums(is.na(df)) / dim(df)[1] * 100, 2), "%"),
        Nullpct2 = paste(round(colSums(is.na(df)) / length(df$ID) * 100, 2), "%"),
        Nullpct5 = paste(round(colSums(is.na(df)) / length(row.names(df)) * 100, 2), "%"),
        # Nullpct6 = paste(round(colSums(is.na(df)) / length(row_number()) * 100, 2), "%"),
        Nullpct3 = paste(round(colMeans(is.na(df)) * 100, 2), "%"),
        nullpct4 = sapply(df, function(x) mean(is.na(df))),
        unique1 = sapply(df, function(x) length(unique(x))),
        unique2 = sapply(df, function(x) length(unique(na.omit(x)))),
        unique3 = sapply(df, function(x) length(unique(x[!is.na(x)])))
        # min = apply(df, 2, min),
        # max = apply(df, 2, max),
        # median = apply(df, 2, median)
    )
    return(data)
}

hasil <- check(df_hotel)
print(hasil)


null1 <- df_hotel %>% summarise(across(everything(), n_distinct))
print(as.data.frame(null1))
cat()
null1 <- df_hotel %>% summarise(across(everything(), ~ n_distinct(.[!is.na(.)])))
print(as.data.frame(null1))
cat()
null1 <- df_hotel %>% summarise(across(everything(), ~ n_distinct(na.omit(.))))
print(as.data.frame(null1))
cat('\n\n\n\n\n')


modus <- names(which.max(table(df_hotel$arrival_date_year)))
print(modus)