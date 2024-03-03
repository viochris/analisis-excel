from datetime import datetime


tanggal = int(input('tanggal lahir:'))
bulan = int(input('bulan lahir:'))
tahun = int(input('tahun lahir:'))

now = datetime.now()
lahir = datetime(tahun, bulan, tanggal)

umur = now - lahir

tahun_umur = umur.days // 365
bulan_umur = (umur.days % 365) // 30
hari_umur = (umur.days % 365) % 30

# Cetak umur
print("Umur:", tahun_umur, "tahun", bulan_umur, "bulan", hari_umur, "hari")
