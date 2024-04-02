library(dplyr)
library(tidyverse)
library(ggplot2)

df_hotel <- read.csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv', na.strings = c("", "NA", " ", "N/A", "NULL"))
df_hotel <- df_hotel %>% mutate(ID = row_number()) %>% select(ID, everything())
df_hotel$arrival_date <- ymd(paste(df_hotel$arrival_date_year, df_hotel$arrival_date_month, df_hotel$arrival_date_day_of_month ,sep='-'))


df_country <- read.csv('https://gist.githubusercontent.com/tadast/8827699/raw/f5cac3d42d16b78348610fc4ec301e9234f82821/countries_codes_and_coordinates.csv')
print(head(df_country))
df_country$code <- trimws(str_replace_all(df_country$`Alpha.3.code`, "'", ""))

df <- merge(df_hotel[c('is_canceled', 'country')], df_country[c('Country', 'code')], by.x='country', by.y = 'code')
df <- filter(df, is_canceled == 0)
print(head(df))

hasil <- table(df$Country)
hasil <- sort(hasil, decreasing = TRUE)
hasil <- head(hasil, 10)
print(hasil)


barplot(hasil, horiz = TRUE, color = 'skyblue', main = "Top 10 Countries",
        xlab = "Count",
        ylab = "Country")