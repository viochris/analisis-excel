from matplotlib import axis
import pandas as pd


# df = pd.DataFrame({
#     'a': range(1, 11),
#     'b': range(11, 21)
# })

# print(df)

df1 = pd.DataFrame({
    'a': [i for i in range(1,11)],
    'b': [i for i in range(11,21)]
})

print(df1)


df2 = pd.DataFrame({
    'a': [1,None, 3,4,6, None, 7,None,9, 10, 11, 12, 13, 14, 15, 16, 17],
    'b': [None, None,1, 6,6, 5, 6, 1,6,1, 6, 1,1,5,5,5,5]
})
print(df2['b'].value_counts())
print(df2.mode())
df2 = df2.fillna(df2.mode().iloc[2]) 
# fill NaN with the most common value of that column or with smallest value if there is no common value
print(df2)

myList = ['Python', 'Hub']
mylist = []
for i in myList:
    mylist.append(i.upper())
print(mylist)


nama_depan = 'Silvio'
nama_belakang = 'Christian'
nama =  nama_depan + ' ' + nama_belakang
print(nama)
print(f"{nama_depan} {nama_belakang}")
namaa = " ".join([nama_depan, nama_belakang ])
print(namaa)

df = pd.DataFrame({
    'depan': ['Silvio', 'Stefanus'],
    'belakang': ['Christian', 'Loveniko']
})
df['lengkap']=  df['depan'] + ' ' + df['belakang']
print(df)
df['nama lengkap'] = df.apply(lambda x: ' '.join([x['depan'], x['belakang']]), axis=1)
print(df)
df['nama lengkap 1'] = df.apply(lambda x: x['depan'] + ' ' + x['belakang'], axis=1)
print(df)

def nama(x,y):
    hasil = ' '.join([x,y])
    return hasil
df['nama lengkap 2'] = df.apply(lambda x: nama(x['depan'], x['belakang']), axis=1)
print(df)

df['nama+i'] = df['depan'].apply(lambda x: x+'i')
print(df)