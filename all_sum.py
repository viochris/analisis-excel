import pandas as pd

# Membuat dataframe
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Menampilkan dataframe
print(df)
print(df.values.sum())
print()

print(df.sum())
print(df.sum(axis=1))
print(df['A'].sum())
print(df.loc[:, 'A'].sum())
print(df.loc[0, :].sum())