import pandas as pd

# Contoh data frame
df1 = pd.DataFrame({'A': [1, 2, 3],
                    'B': [4, 5, 6]})

df2 = pd.DataFrame({'A': [7, 8, 9],
                    'B': [10, 11, 12]})

# Concat dengan axis=0
result_vertical = pd.concat([df1, df2], axis=0)

print("Hasil concat dengan axis=0 (vertikal):")
print(result_vertical)

print('\n\n\n')

# Contoh data frame
df1 = pd.DataFrame({'A': [1, 2, 3],
                    'B': [4, 5, 6]})

df2 = pd.DataFrame({'C': [7, 8, 9],
                    'D': [10, 11, 12]})

# Concat dengan axis=1
result_horizontal = pd.concat([df1, df2], axis=1)

print("Hasil concat dengan axis=1 (horizontal):")
print(result_horizontal)





