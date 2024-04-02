library(dplyr)
library(tidyverse)
library(ggplot2)

df_hotel <- read.csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv', na.strings = c("", "NA", " ", "N/A", "NULL"))
# Assuming df_hotel is your data frame
df <- df_hotel %>% mutate(ID = row_number()) %>% select(ID, everything())

df <- df[df$is_canceled ==0,]
hasil <- df %>% group_by(hotel, arrival_date_month) %>% summarise(total = n())


# Mengganti nama bulan dengan angka bulan
df <- df %>% mutate(arrival_date_month = recode(arrival_date_month, 
                                        'January' = 1,
                                        'February' = 2,
                                        'March' = 3,
                                        'April' = 4,
                                        'May' = 5,
                                        'June' = 6,
                                        'July' = 7,
                                        'August' = 8,
                                        'September' = 9,
                                        'October' = 10,
                                        'November' = 11,
                                        'December' = 12))
hasil2 <- df %>% group_by(hotel, arrival_date_month) %>% summarise(total = n())
print(hasil2)

# Membuat plot bar
plot <- ggplot(data = df, aes(x = arrival_date_month, fill = hotel)) +
    geom_bar(position = "dodge") +
    labs(x = "Month", y = "Count", title = "Arrival Plot") +
    theme_minimal() +
    scale_x_discrete(labels = c("1" = "January", "2" = "February", "3" = "March", 
                                "4" = "April", "5" = "May", "6" = "June", 
                                "7" = "July", "8" = "August", "9" = "September", 
                                "10" = "October", "11" = "November", "12" = "December"))
print(plot)