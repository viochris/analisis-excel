import pandas as pd

data = {
    'id': ['A', 'B', 'C', 'A', 'B'],
    'Makanan': [['Kopi', 'Roti'], ['Kopi', 'Teh'], ['Teh', 'Roti'], ['Kopi', 'Susu'], ['Nugget', 'Teh']],
    'Minuman': ['Kopi', 'Teh', 'Kopiii', 'Permen Kopiko', 'Kopik']
}
df = pd.DataFrame(data)
print(df)

# Salah
hasil1 = df['Minuman'].isin(['Kopi'])
print(hasil1)
def kopi(x):
    if x in ['Kopi']:
        return 'enakk'
    else:
        return False
hasil3 = df['Minuman'].apply(kopi)
print(hasil3)

# Benar
hasil2 = df['Makanan'].apply(lambda x: 'Kopi' in x)
print(hasil2)
def kopi(x):
    if 'Kopi' in x:
        return 'enakk'
    else:
        return False
hasil3 = df['Makanan'].apply(kopi)
print(hasil3)


hasil4 = df['Minuman'].str.contains('Kopi')
print(hasil4)