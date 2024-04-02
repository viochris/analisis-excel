library(dplyr)
library(tidyverse)
library(ggplot2)

df_hotel <- read.csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv', na.strings = c("", "NA", " ", "N/A", "NULL"))
# Assuming df_hotel is your data frame
df_hotel <- df_hotel %>% mutate(ID = row_number()) %>% select(ID, everything())

hasil <- table(df_hotel$is_canceled)
print(hasil)
proporsi <- prop.table(table(df_hotel$is_canceled))
print(proporsi)

barplot(
    height = proporsi,
    names.arg = levels(df_hotel$is_canceled),
    main = "Pembatalan",
    xlab = "Kategori",
    ylab = "Proporsi",
)
