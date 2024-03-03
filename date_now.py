from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime('%H:%M:%S')
tahun = now.strftime('%Y')
print(now)
print(formatted_date)
print(formatted_time)
print(tahun)