import pandas as pd

# Assuming you have a DataFrame named df
data = {'target_column': [0, 1, 1, 1, 0, 1, 0, 1, 0, 1]}
df = pd.DataFrame(data)

# Mapping 0 to 'no' and 1 to 'yes' in the 'target_column'
df['target_column'] = df['target_column'].map({0: 'no', 1: 'yes'})

# Display the modified DataFrame
print(df)
