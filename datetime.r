library(lubridate)

datetime <- ymd_hms("2022-03-21 10:15:30")
print(datetime)
cat('\n\n')

print(year(datetime))
print(month(datetime))
print(months(datetime))
print(day(datetime))
print(hour(datetime))
print(minute(datetime))
print(second(datetime))

cat('\n\n\n\n')


datetime <- as.POSIXct("2022-03-21 10:15:30")
print(datetime)
cat('\n\n')

print(year(datetime))
print(month(datetime))
print(months(datetime))
print(day(datetime))
print(hour(datetime))
print(minute(datetime))
print(second(datetime))
print(weekdays(datetime))
print(datetime - weeks(2))