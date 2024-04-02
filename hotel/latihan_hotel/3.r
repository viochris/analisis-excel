library(dplyr)
library(tidyverse)
library(ggplot2)

df_hotel <- read.csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv', na.strings = c("", "NA", " ", "N/A", "NULL"))
# Assuming df_hotel is your data frame
df_hotel <- df_hotel %>% mutate(ID = row_number()) %>% select(ID, everything())
city <- filter(df_hotel, hotel == 'City Hotel')
hasil <- prop.table(table(city$is_canceled))
print(hasil)


resort <- filter(df_hotel, hotel == 'Resort Hotel')
hasil <- prop.table(table(resort$is_canceled))
print(hasil)