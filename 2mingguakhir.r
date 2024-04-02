library(dplyr)
library(lubridate)

now <- Sys.time()
print(now)

today <- today()
print(today)

hari_ini <- ymd('2024-03-21')
print(hari_ini)

waktu_ini <- hms('12:30:45')
print(waktu_ini)

two_weeks_ago1 <- now - weeks(2)
print(two_weeks_ago1)


two_weeks_ago2 <- today - weeks(2)
print(two_weeks_ago2)

two_weeks_ago3 <- hari_ini - weeks(2)
print(two_weeks_ago3)

df <- data.frame(
    Date = c("2024-02-25", "2024-03-16", "2024-02-01", "2024-05-10", "2024-04-01"),
    Terjual = c("Sapu", "Sapi", "Engkrak", "Nasgor", "sushi")
)
df$Date <- as.Date(df$Date)
print(df)
hasil <- df[df$Date >= two_weeks_ago2, ]
print(hasil)