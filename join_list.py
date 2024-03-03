import pandas as pd

# Contoh DataFrame
df = pd.DataFrame({
    'antecedents': [frozenset({'apple', 'banana'}), frozenset({'orange', 'pear'}), frozenset({'grape', 'kiwi'})],
    'consequents': [frozenset({'juice', 'smoothie'}), frozenset({'jam', 'jelly'}), frozenset({'wine', 'cake'})]
})

print(df)

df['antecedents'] = df['antecedents'].apply(lambda x: ' '.join(list(x)))
df['consequents'] = df['consequents'].apply(lambda x: ' '.join(list(x)))
print(df)