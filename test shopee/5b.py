import pandas as pd
df = pd.read_csv('order.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df = df.sort_values(by=['Customer ID', 'Order ID'])
coba = df[df['Customer ID'] == 'AA-10480']
print(coba[['Customer ID', 'Order Date', 'Sales']])

hasil = df.groupby('Customer ID').agg({'Order Date': 'min','Sales': 'first' }).reset_index()
print(hasil)