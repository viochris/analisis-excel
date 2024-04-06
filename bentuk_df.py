import pandas as pd


data = [
    ['John', 28, 'Engineer'],
    ['Alice', 24, 'Data Scientist'],
    ['Bob', 32, 'Teacher']
]
print(data)
df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
print(df)
print('\n\n\n')

data = [
    ('John', 28, 'Engineer'),
    ('Alice', 24, 'Data Scientist'),
    ('Bob', 32, 'Teacher')
]
print(data)
df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
print(df)
print('\n\n\n')

data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [28, 24, 32],
    'Occupation': ['Engineer', 'Data Scientist', 'Teacher']
}
print(data)
df = pd.DataFrame(data)
print(df)
print('\n\n\n')

# data = {
#     'Person1': ('John', 28, 'Engineer'),
#     'Person2': ('Alice', 24, 'Data Scientist'),
#     'Person3': ('Bob', 32, 'Teacher')
# }
# df = pd.DataFrame(data.values(), index=data.keys(), columns=['Name', 'Age', 'Occupation'])
# print(df)
# print('\n\n\n')


data = [
    {'Name': 'John', 'Age': 28, 'Occupation': 'Engineer'},
    {'Name': 'Alice', 'Age': 24, 'Occupation': 'Data Scientist'},
    {'Name': 'Bob', 'Age': 32, 'Occupation': 'Teacher'}
]
print(data)
df = pd.DataFrame(data)
print(df)
print('\n\n\n')

# data = {
#     'Person1': {'Name': 'John', 'Age': 28, 'Occupation': 'Engineer'},
#     'Person2': {'Name': 'Alice', 'Age': 24, 'Occupation': 'Data Scientist'},
#     'Person3': {'Name': 'Bob', 'Age': 32, 'Occupation': 'Teacher'}
# }
# df = pd.DataFrame.from_dict(data, orient='index')
# print(df)
# print('\n\n\n')