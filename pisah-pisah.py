import pandas as pd

# Data awal dengan data terpisah-pisah
data = {'nama': ['a   l i     c    e', 'b  o b', 'c  a r o l']}
df = pd.DataFrame(data)

# Menghapus spasi ekstra
df['nama1'] = df['nama'].str.replace('\s+', '' , regex=True)

# Menghapus karakter non-alfanumerik
df['nama2'] = df['nama'].str.replace('[^a-zA-Z0-9]', '', regex=True)

# Menggabungkan data terpisah
df['nama3_incomplete'] = df['nama'].str.split()
df['nama3'] = df['nama'].str.split().apply(lambda x: ''.join(x))

# tidak guna, malah balek ke asal 
# df['nama4_incomplete'] = df['nama'].str.split('')
# df['nama4'] = df['nama'].str.split('').apply(lambda x: ''.join(x))

# tidak guna, malah balek ke asal. Alias sama seperti di atas. Hanya beda di awal ada , atau tidak 
# misal alice. Jika yang atas jadi [, A, l, i, c, e, ]. Jika yang dibawah ini akan jadi  [A, l, i, c, e]
# df['nama4_incomplete'] = df['nama'].apply(list)
# df['nama4'] = df['nama'].apply(list).apply(lambda x: ''.join(x))

print(df)



# Cara 1 (nama1): Menggunakan '\s+' dalam fungsi str.replace() untuk 
# mengganti satu atau lebih spasi dengan string kosong. Ini menghapus spasi 
# yang berlebihan dari setiap string di kolom nama.

# Cara 2 (nama2): Menggunakan [^a-zA-Z0-9] dalam fungsi str.replace() untuk mengganti 
# karakter non-alfanumerik dengan string kosong. Ini menghapus semua karakter non-alfanumerik 
# dari setiap string di kolom nama.

# Cara 3 (nama3): Memecah setiap string di kolom nama menjadi list kata-kata menggunakan 
# fungsi str.split(). Kemudian, menerapkan fungsi join() untuk menggabungkan kembali kata-kata tersebut 
# tanpa spasi di antara mereka.

# Dalam regex, tanda [] digunakan untuk menentukan karakter mana yang ingin 
# Anda pertahankan atau hapus. Jika Anda menggunakan [^a-zA-Z0-9], itu berarti 
# Anda ingin mempertahankan semua karakter kecuali huruf (baik huruf besar maupun kecil) dan angka.

# Sementara itu, jika Anda hanya menggunakan '' (string kosong), seperti dalam \s+, 
# itu berarti Anda ingin menggantikan pola yang cocok dengan string kosong. Dalam konteks ini, 
# \s+ akan mencocokkan satu atau lebih spasi dan menggantinya dengan string kosong, sehingga menghapus 
# spasi tersebut dari teks.


