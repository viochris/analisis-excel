import pandas as pd
import matplotlib.pyplot as plt

# Contoh DataFrame
data = {
    'order_month': ['Jan', 'Feb', 'Jan', 'Feb', 'Jan', 'Feb', 'Jan', 'Feb'],
    'brand': ['A', 'A', 'B', 'B', 'A', 'B', 'C', 'C'],
    'GMV': [1000, 1500, 2000, 1800, 1200, 1600, 2000, 4000],
    'order': [1, 1, 2, 1, 1, 1, 2, 4]
}
df = pd.DataFrame(data)

# Groupby, Unstack, dan Plot
hasil = df.groupby(['order_month', 'brand'])['GMV'].sum()
print(hasil)

hasil_akhir = pd.pivot_table(df, index='order_month', columns='brand', values='GMV', aggfunc='sum')
print(hasil_akhir)

hasil = df.groupby(['order_month', 'brand'])['GMV'].sum().unstack()
print(hasil)
hasil = df.groupby(['order_month', 'brand'])['GMV'].sum().unstack().plot(kind='bar')
print(hasil)


plt.xlabel('Order Month')
plt.ylabel('Total GMV')
plt.title('Total GMV per Brand per Month')
plt.legend(title='Brand')
plt.show()
