import pandas as pd

data = {
    'Daerah': ['Bandung', 'Jakarta', 'Surabaya', 'Bali', 'Yogyakarta', 'Lombok', 'Malang', 'Surabaya', 'Jakarta'],
    'Kota': ['Bandung', 'Jakarta', 'Surabaya', 'Denpasar', 'Yogyakarta', 'Mataram', 'Malang', 'Malang', 'Bandung']
}
df = pd.DataFrame(data)

def prov(x):
    if x in ['Bandung', 'Jakarta', 'Surabaya']:
        return 'Jawa'
    else : return 'Luar Jawa'
df['Provinsi'] = df['Daerah'].apply(prov)
print(df)
hasil = df['Provinsi'].value_counts()
print(hasil)