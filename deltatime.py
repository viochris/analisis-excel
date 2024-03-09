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
# time.struct_time(tm_year=2024, tm_mon=3, tm_mday=8, tm_hour=12, tm_min=54, tm_sec=43, tm_wday=4, tm_yday=68, tm_isdst=0) 
# Tahun: 2024.
# Bulan: Maret (3).
# Hari: 8.
# Jam: 12 (jam tengah hari).
# Menit: 54.
# Detik: 43.
# Hari dalam minggu: Kamis (4).
# Hari dalam tahun: Hari ke-68 dalam tahun (Minggu ke-10).
# Tidak berada dalam Daylight Saving Time (DST).
print(time.localtime())  # Mendapatkan waktu saat ini dalam bentuk struktur waktu
print(time.strftime("%H:%M:%S"))  # Mendapatkan waktu saat ini dalam format jam:menit:detik
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strftime("%Y-%m-%d"))