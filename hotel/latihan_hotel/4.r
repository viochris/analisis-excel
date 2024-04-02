library(dplyr)
library(tidyverse)
library(ggplot2)

df_hotel <- read.csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv', na.strings = c("", "NA", " ", "N/A", "NULL"))
# Assuming df_hotel is your data frame
df_hotel <- df_hotel %>% mutate(ID = row_number()) %>% select(ID, everything())

df_1 <- df_hotel[df_hotel$is_canceled == 0, ]
print(head(df_1))
df_checkout <- df_hotel[df_hotel$reservation_status == 'Check-Out',]
print(head(df_checkout))