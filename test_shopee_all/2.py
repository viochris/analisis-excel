import pandas as pd

customer = pd.read_csv('test_shopee_all/Customer.csv')
customer = customer.groupby('City')['Customer ID'].unique().explode().reset_index(name = 'ID')

order = pd.read_csv('test_shopee_all/Orders.csv')

print(customer.head(5))
print(order.head(5))

hasil = pd.merge(customer, order, left_on= 'ID', right_on='Customer ID', how = 'inner')
hasil = hasil.groupby('City')['Order ID'].count().reset_index(name='jumlah').sort_values('jumlah', ascending=False).reset_index(drop=True)
print(hasil)