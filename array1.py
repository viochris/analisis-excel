"""
Trivia

1. break: Pernyataan break digunakan untuk menghentikan 
eksekusi loop secara paksa. Ketika break dieksekusi di dalam loop, 
loop tersebut akan berhenti segera, dan eksekusi program akan melanjutkan ke 
pernyataan setelah loop. Ini berguna ketika Anda ingin keluar dari loop 
berdasarkan kondisi tertentu yang terpenuhi.

2. continue: Pernyataan continue digunakan untuk menghentikan eksekusi iterasi saat ini 
dalam loop dan melanjutkan ke iterasi berikutnya. Ketika continue dieksekusi di dalam loop,
kode di bawah continue dalam iterasi saat ini tidak akan dieksekusi, dan loop akan melanjutkan ke 
iterasi berikutnya.

3. pass: Pernyataan pass tidak melakukan apa pun. 
Ini adalah pernyataan kosong yang digunakan ketika sintaks Python memerlukan pernyataan,
tetapi Anda tidak ingin menambahkan kode di dalamnya. Biasanya, pass digunakan sebagai 
placeholder sementara atau sebagai wadah untuk kode yang akan ditambahkan nanti.

kesimpulan == jadi break = berhenti, continue = lompati, pass = tidak lakukan apapun
"""



counter = 1
while counter <= 5:
    print(counter)
    counter += 1
    
for i in range(0, 3):
    for j in range(1, 3):
        print(i,j)
        
for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1

for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))
    
for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print(f'Huruf saat ini: {huruf}')
    
    
for huruf in 'Dico ding':
    if huruf == '  ':
        break
    print('Huruf saat ini: {}'.format(huruf))
    
for huruf in 'Dico ding':
    if huruf == '  ':
        break
    print(f'Huruf saat ini: {huruf}')
    
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))
    
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print(f'Huruf saat ini: {huruf}')


    
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")
    

counter = 1
while counter <= 5:
    print('counter')
    counter += 1
else :
    print("Selesai")
    
    
# error    
n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")


x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")
    
    
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)

angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

z=0
try:
    print(1/z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi angka dengan nilai nol.")


    
var_dict = {"rata_rata": "1.0"}
try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")
    
    
var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i+1)


