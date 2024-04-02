library(dplyr)
library(tidyverse)
library(ggplot2)

df_hotel <- read.csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv', na.strings = c("", "NA", " ", "N/A", "NULL"))
df <- df_hotel %>% mutate(ID = row_number()) %>% select(ID, everything())
df$arrival_date <- ymd(paste(df$arrival_date_year, df$arrival_date_month, df$arrival_date_day_of_month ,sep='-'))

df <- filter(df, is_canceled == 0)
df_checkout <- df %>% group_by(hotel, customer_type) %>% summarise(adr = mean(adr))
print(df_checkout)


plot <- ggplot(df_checkout, aes(x = adr, y = hotel, fill = customer_type)) +
    geom_boxplot() +
    geom_point(position = position_dodge(width = 0.75), size = 3, alpha = 0.5) +
    labs(title = "Boxplot ADR berdasarkan Jenis Hotel dan Tipe Pelanggan",
        x = "ADR",
        y = "Jenis Hotel") +
    theme_minimal() +
    theme(legend.position = "top") +
    guides(fill = guide_legend(title = "Tipe Pelanggan"))

print(plot)