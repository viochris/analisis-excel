library(dplyr)
library(tidyverse)
library(ggplot2)
# library(plyr)

df_hotel <- read.csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv", na.strings = c("", "NA", " ", "N/A", "NULL"))
# Assuming df_hotel is your data frame
df <- df_hotel %>%
    mutate(ID = row_number()) %>%
    select(ID, everything())

df <- df[df$is_canceled == 0, ]
hasil <- df %>%
    group_by(hotel, arrival_date_month) %>%
    summarise(total = n())

# plot <- ggplot(data = df, aes(x = arrival_date_month, fill = hotel)) +
#     geom_bar(position = "dodge") +
#     labs(x = "Month", y = "Count", title = "Arrival Plot") +
#     theme_minimal()
# print(plot)


# Mengganti nama bulan dengan angka bulan
# df <- df %>% mutate(arrival_date_month = recode(arrival_date_month,
#                                         'January' = 1,
#                                         'February' = 2,
#                                         'March' = 3,
#                                         'April' = 4,
#                                         'May' = 5,
#                                         'June' = 6,
#                                         'July' = 7,
#                                         'August' = 8,
#                                         'September' = 9,
#                                         'October' = 10,
#                                         'November' = 11,
#                                         'December' = 12))
replace <- c(
    "January" = "1",
    "February" = "2",
    "March" = "3",
    "April" = "4",
    "May" = "5",
    "June" = "6",
    "July" = "7",
    "August" = "8",
    "September" = "9",
    "October" = "10",
    "November" = "11",
    "December" = "12"
)
df$arrival_date_month <- as.numeric(str_replace_all(df$arrival_date_month, replace))
# df$arrival_date_month <- as.numeric(plyr::mapvalues(df$arrival_date_month, from = names(replace), to= replace))
hasil2 <- df %>%
    group_by(hotel, arrival_date_month) %>%
    summarise(total = n())
print(hasil2, n = 24)




plot <- ggplot(data = df, aes(x = arrival_date_month, fill = hotel)) +
    geom_bar(position = "dodge") +
    labs(x = "Month", y = "Count", title = "Arrival Plot") +
    theme_minimal() +
    scale_x_continuous(breaks = 1:12, labels = 1:12)
print(plot)


# plot <- ggplot(data = df, aes(x = arrival_date_month, fill = hotel)) +
#     geom_bar(position = "dodge") +
#     labs(x = "Month", y = "Count", title = "Arrival Plot") +
#     theme_minimal() +
#     scale_x_continuous(breaks = 1:12, labels =
#     c('January',
#         'February',
#         'March',
#         'April',
#         'May',
#         'June',
#         'July',
#         'August',
#         'September',
#         'October',
#         'November',
#         'December'))
# print(plot)
