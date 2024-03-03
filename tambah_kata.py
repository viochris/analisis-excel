import pandas as pd

df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': ['A', 'B', 'C'],
})

def tahun(x):
    return str(x) + ' tahun'
def tahun2(x):
    return f'{x} tahun'
df['a'] = df['a'].apply(tahun2)
df['b'] = df['b'].apply(tahun)
print(df)