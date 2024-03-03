import re
import pandas as pd

pola= '^d....n$'
string_tes= 'dragon'
hasil = re.match(pola, string_tes)

if hasil:
    print('Pencarian berhasil')
else:
    print('Gagal')
    
    


# Membuat DataFrame contoh
data = {'text': ['apple', 'banana', 'orange', 'dragonfruit']}
df = pd.DataFrame(data)

# Memeriksa apakah teks dalam kolom 'text' mengandung 'd...'
result = df[df['text'].str.contains('..a..') == False]
print(result)
print()

def match(text):
    pola = '^a...e$'
    hasil = re.match(pola, text)
    return bool(hasil)
data = {'text': ['apple', 'banana', 'orange', 'dragonfruit']}
df = pd.DataFrame(data)

hasil = df[df['text'].apply(match) == True]
print(hasil)