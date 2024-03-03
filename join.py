import pandas as pd

# Contoh DataFrame
data = {'Data 1': ['aku', 'Kamu Gimana', 'kamu'], 'Data 2': ['suka', 'suka', 'suka'], 'Data 3': ['kamu', 'aku?', 'aku']}
df = pd.DataFrame(data)
print(df)

def join_data(row):
    return " ".join(row)
df['Hasil'] = df.apply(join_data, axis=1)
print(df)
def join_data(x,y,z):
    return x+" "+y+" "+z
df.loc[0:2,'Hasil'] = join_data(df['Data 1'], df['Data 2'], df['Data 3'])
print(df)


data1 = {'Data 1': ['aku', 'Kamu Gimana', 'Kamu'], 'Data 2': ['suka', 'suka', 'suka'], 'Data 3': ['kamu', 'aku?', 'aku'], 'Data 4': ['kamu', 'aku?', 'aku']}
df1 = pd.DataFrame(data1)
print(df1)
# data1 = {'Data 1': ['aku', 'Kamu Gimana', 1], 'Data 2': [3, 'suka', 'suka'], 'Data 3': ['kamu', 'aku?', 4], 'Data 4': ['kamu', 7, 'aku']}
# df1 = pd.DataFrame(data1)
# print(df1)

def join_data(row):
    return " ".join(row)
df1['Hasil'] = df1.apply(join_data, axis=1)
print(df1)
def join_data(x,y,z):
    return x+" "+y+" "+z
df1.loc[0:2,'Hasil'] = join_data(df1['Data 1'], df1['Data 2'], df1['Data 3'])
print(df1)
def join_data(x,y,z):
    return x+" "+y+" "+z
df1['Hasil'] = df1.apply(lambda row:join_data(row['Data 1'], row['Data 2'], row['Data 3']), axis=1)
print(df1)
def join_data(col):
    return " ".join(col)
df1.loc[3] = df1.apply(join_data, axis=0)
print(df1)