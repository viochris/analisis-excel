from datetime import datetime, timedelta, date
import time

# Mendapatkan tanggal dua minggu yang lalu
two_weeks_ago = datetime.today() - timedelta(weeks=2)


# Menambahkan satu bulan ke tanggal tertentu
one_month_from_now = datetime.today() + timedelta(days=30)

print("Dua minggu yang lalu:", two_weeks_ago)
print("Satu bulan dari sekarang:", one_month_from_now)



# Mendapatkan tanggal dua minggu yang lalu
two_weeks_ago = date.today() - timedelta(weeks=2)

# Menambahkan satu bulan ke tanggal tertentu
one_month_from_now = date.today() + timedelta(days=30)

print("Dua minggu yang lalu:", two_weeks_ago)
print("Satu bulan dari sekarang:", one_month_from_now)


print(datetime.today())
print(datetime.now())
print(date.today())
print(time)
print(time.localtime())  # Mendapatkan waktu saat ini dalam bentuk struktur waktu
print(time.strftime("%H:%M:%S"))  # Mendapatkan waktu saat ini dalam format jam:menit:detik
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strftime("%Y-%m-%d"))