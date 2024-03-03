import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df1 = pd.DataFrame(data)
print(df1)

def join_data(row):
    return sum(row)
df1['Hasil'] = df1.apply(join_data, axis=1)
print(df1)

def join_data(row):
    return sum(row)
df1['Hasil'] = df1.apply(join_data, axis=1)
print(df1)

def join_data(col):
    return sum(col)
df1.loc[len(df1)] = df1.apply(join_data)
print(df1)