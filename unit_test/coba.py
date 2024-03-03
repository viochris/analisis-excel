string = "www.dicoding.com"

# Menghapus karakter 'c', '.', 'm', 'o', dan 'w' dari awal dan akhir string
result = string.strip('w.com')
print(result)  # Output: "wwdicoding."


alpha = 'c0d!ng'
hasil = alpha.isalnum()
print(hasil)
print(hasil == False)

s = "dicoding"
# Coba cari index dari substring 'coding' di dalam string 'dicoding'
index_coding = s.index('coding')
print("Index dari 'coding' dalam 'dicoding' adalah:", index_coding)