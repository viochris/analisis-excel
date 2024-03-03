import pandas as pd

data = {'A': [1, 2, 3], 'B': ['4', '5', '6'], 'C': [7, 8, 9]}
df1 = pd.DataFrame(data)
print(df1)

def join_data(x,y):
    return x+y
df1['Hasil'] = df1.apply(lambda row: join_data(row['A'], row['C']), axis=1)
print(df1)


data = {'A': [1, '2', 3], 'B': [4, '5', 6], 'C': [7, '8', 9]}
df1 = pd.DataFrame(data)
print(df1)
def join(x,y):
    return x+y
df1.loc[3] = df1.apply(lambda col: join(col[0], col[2]))
print(df1)