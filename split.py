import pandas as pd

# Membuat DataFrame dengan kolom 'nama'
data = {'nama1': ['Alice Bob', 'Charlie David', 'Alice David', 'Alice'],
        'nama2': ['A l ice', 'B ob', 'C harlie', 'D avid']}
df = pd.DataFrame(data)

# Memecah string di kolom 'nama' menjadi bagian terpisah
# df['nama_terpisah1'] = df['nama1'].str.split()
# df['nama_terpisah2'] = df['nama2'].str.split()
df['nama_terpisah1a'] = df['nama1'].str.split('')
# df['nama_terpisah2a'] = df['nama2'].str.split('')
df['nama_terpisah1aa'] = df['nama1'].apply(list)
# df['nama_terpisah2aa'] = df['nama2'].apply(list)
# df['nama_gabung1'] = df['nama1'].str.split().apply(lambda x: ''.join(x))
# df['nama_gabung2'] = df['nama2'].str.split().apply(lambda x: ''.join(x))

print(df)
