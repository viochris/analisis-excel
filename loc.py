import pandas as pd
import numpy as np

# Membuat DataFrame train
train = pd.DataFrame({
    'PassengerId': [1, 2, 3, 4, 5],
    'Survived': [0, 1, 1, 1, 0],
    'Pclass': [3, 1, 3, 1, 3],
    'Name': ["Braund, Mr. Owen Harris", "Cumings, Mrs. John Bradley (Florence Briggs Thayer)", "Heikkinen, Miss. Laina", "Futrelle, Mrs. Jacques Heath (Lily May Peel)", "Allen, Mr. William Henry"],
    'Sex': ["male", "female", "female", "female", "male"],
    'Age': [22, 38, 26, 35, np.nan],
    'Cabin': [np.nan, "C85", np.nan, "C123", np.nan],
    'Embarked': ["S", "C", "S", np.nan, "S"]
})

# Menampilkan DataFrame train
print(train['Embarked'].mode())
print(train['Embarked'].mode()[0])
train['Embarked'] = train['Embarked'].fillna(train['Embarked'].mode()[0])

print('\n\n\n')
print(train)
print('\n\n\n')

print(train[train.index == 3])
print()
print(train.loc[3, 'Name'])
print()
print(train.iloc[3, 3])
print()
print(train['Name'])

print('\n\n\n')
print(train.loc[0:2, 'PassengerId':'Pclass'])
print(train.iloc[0:3, 0:4])