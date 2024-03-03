import pandas as pd

# Contoh DataFrame
data = {'id': ['A', 'B', 'C', 'A', 'B'],
        'kegiatan': ['Tidur', 'Makan', 'Minum', 'Tidur', 'Makan']
        }
df = pd.DataFrame(data)
print(df)

def ubah_kegiatan(kegiatan):
    if kegiatan == 'Tidur':
        return 'tidur'
    elif kegiatan == 'Makan':
        return 'makan'
    else:
        return 'ga berubah'

df['kegiatan'] = df['kegiatan'].apply(ubah_kegiatan)
print(df)