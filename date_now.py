from datetime import datetime, date

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime('%H:%M:%S')
tahun = now.strftime('%Y')
print(now)
print(formatted_date)
print(formatted_time)
print(tahun)


now = date.today()
formatted_date = now.strftime("%Y-%m-%d")
tahun = now.strftime('%Y')
print(now)
print(formatted_date)
print(tahun)