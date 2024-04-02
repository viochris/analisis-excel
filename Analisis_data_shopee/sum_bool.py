import pandas as pd

my_list = [True, False, True, False, True]
print(sum(my_list))
print(my_list.count(True))
print(my_list.count(False))
print()
print()

df = pd.DataFrame({
    'data': my_list
})
print(df)
print()
print(df.value_counts()[True])
print()
print(df.value_counts()[False])
print()
print(df.value_counts())
print()