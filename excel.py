import pandas as pd
df = pd.read_csv('Data Shopee.csv')
print(df.head())
df['order_date'] = pd.to_datetime(df['order_date'])


# df['aov'] = df['before_discount'].sum() / df['id'].nunique()
df['net_profit'] = df['before_discount'] - df['cogs'] * df['qty_ordered']
print(df.head())


hasil = df.groupby([df['order_date'].dt.year, df['order_date'].dt.month]).agg({'net_profit': 'sum', 'before_discount':'sum', 'id': 'nunique', 'after_discount': 'sum'})
hasil['aov'] = hasil['before_discount'] / hasil['id']
print(hasil)