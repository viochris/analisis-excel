import pandas as pd

# Contoh DataFrame
data = {'id': ['A', 'B', 'C', 'A', 'B', 'D', 'E', 'F','E','F'],
        'no': [1,2,2,4,2,6,7,2,5,7],
        'kegiatan': ['Tidur', 'Makan', 'Minum', 'Tiduri', 'Makan', 'Olahraga', 'Belajar', 'Ngemil', 'Belajar', 'Ngemil']
        }
df = pd.DataFrame(data)
print(df)

# def ubah_kegiatan(kegiatan):
#     if kegiatan in ['Tidur', 'Makan', 'Minum']:
#         return 'pokok'
#     else:
#         return 'sekunder'

# df['Keterangan'] = df['kegiatan'].apply(ubah_kegiatan)
# print(df)

hal1 = df['kegiatan'].isin(['Tidur'])
hal2 = df['kegiatan'].str.contains('Tidur')
print(df[hal1])
print(df[hal2])
hal1 = df['no'].isin([2])
hal2 = df['no'].astype(str).str.contains('2')
print(df[hal1])
print(df[hal2])
hal1 = df['no'].between(1,4)
print(df[hal1])

def check(x):
        if 'Minum' in x:
                return 'enakkk'
        else: 
                return 'oklahhh'
df['ket'] = df.apply(lambda x: check(x['kegiatan']), axis=1)
print(df)