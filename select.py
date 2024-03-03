import pandas as pd
import numpy as np

df = pd.DataFrame({
    'daftar': ['a', 'b', 'c', 'd', 'e', 'b', 'c', 'd', 'c', 'e'],
    'daftar2': ['makanan', 'minuman', 'minuman', 'makanan', 'makanan', 'minum', 'makan', 'maka', 'minu', 'makan']
})


df['penjelasan'] = np.select(
    [df['daftar'].isin(['a', 'b', 'c'])],
    ['good']
    ,default='bad'
)
df['penjelasan2'] = np.select(
    [
        (df['daftar2'].str.lower().str.contains('makan')),
        (df['daftar2'].str.lower().str.contains('minum'))],
    ['enak', 'segar'],
    default='entah'
)

def jelas(x):
    if x in ['a', 'b', 'c']:
        return 'good'
    else: 
        return 'bad'
df['jelas'] = df['daftar'].apply(jelas)


# # entahlah kenapa gagal
# def jelas2(x):
#     if str(x).lower().find('makan') != -1:
#         return 'enak'
#     elif str(x).lower().find('minum') != -1:
#         return 'segar'
#     else:
#         return 'entah'
# df['jelas2'] = df['daftar'].apply(jelas2)
print(df)