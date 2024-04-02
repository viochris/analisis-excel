import pandas as pd

# Buat DataFrame
data = {'words': ["apple", "banana", "grape", "orange", "pineapple"]}
df = pd.DataFrame(data)

# Cocokkan pola 'apple' dalam kolom 'words'
df['contains_apple'] = df['words'].str.contains('apple')


# Cocokkan pola 'an' dalam kolom 'words'
df['contains_an'] = df['words'].str.contains('an')


# Cocokkan pola 'pear' dalam kolom 'words'
df['contains_pear'] = df['words'].str.contains('pear')
print(df)
