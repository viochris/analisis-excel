import pandas as pd

df = pd.DataFrame({
    'EmbarkedS': [1,2,3,4,5],
    'EmbarkedQ' : [1,2,3,4,5],
    'EmbarkedR' : [1,2,3,4,5]
})

print(df)
# df.columns = df.columns.str.replace('Embarked', ' ')
# print(df)
# print(df[' S'])


df.columns = df.columns.str.replace('Embarked', ' ').str.strip()
print(df)
print(df['S'])