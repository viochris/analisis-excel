import pandas as pd

df = pd.DataFrame({
    'Nama': [None, 'Niko', 'Gaby', 'Vio', 'Maria'],
    'Umur': [12, 13, None, 18, 34],
    'Kelas': [12, 13, 12, 16, None]
})
print(df)
print()
print(df[df['Umur'].isnull()])
print('\nNot Null')
print(df[df['Umur'].notnull()])
print('\n\n\n\n\n')
print(df.isnull().sum())
print()
print(df.isnull().sum(axis=1))
print()
print(df[df[['Umur', 'Kelas']].isna().any(axis=1)])
print()
print(df[df.isnull().any(axis=1)])
print()
print(df[df.isnull().sum(axis=1) > 0])
print()
print(df.loc[:, df.isnull().any(axis=0)])
print()
print(df.loc[:, df.isnull().sum() > 0])


