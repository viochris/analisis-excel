import pandas as pd

customer = pd.read_csv('test_shopee_all/Customer.csv')

order = pd.read_csv('test_shopee_all/Orders.csv')
order['Order Date'] = pd.to_datetime(order['Order Date'])
order = order.groupby('Customer ID')['Order Date'].min().reset_index(name = 'pembelian_pertama')

print(customer.head(5))
print(order.head(5))

hasil = pd.merge(customer, order, on = 'Customer ID',how='inner')
print(hasil.head())

hasil_akhir = hasil.groupby(['City', 'pembelian_pertama'])['Customer ID'].count().reset_index(name = 'jumlah').sort_values('jumlah', ascending=False).reset_index(drop=True)
print(hasil_akhir)