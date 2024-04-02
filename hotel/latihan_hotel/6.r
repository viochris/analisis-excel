library(dplyr)
library(tidyverse)
library(ggplot2)

df_hotel <- read.csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv', na.strings = c("", "NA", " ", "N/A", "NULL"))
# Assuming df_hotel is your data frame
df <- df_hotel %>% mutate(ID = row_number()) %>% select(ID, everything())

df$arrival_date <- ymd(paste(df$arrival_date_year, df$arrival_date_month, df$arrival_date_day_of_month ,sep='-'))
print(head(df))