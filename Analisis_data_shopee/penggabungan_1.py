import pandas as pd
from sqlite3 import connect

path_od = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/order_detail.csv"
path_pd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/payment_detail.csv"
path_cd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/customer_detail.csv"
path_sd = "https://raw.githubusercontent.com/dataskillsboost/FinalProjectDA11/main/sku_detail.csv"
df_od = pd.read_csv(path_od)
df_pd = pd.read_csv(path_pd)
df_cd = pd.read_csv(path_cd)
df_sd = pd.read_csv(path_sd)

connection = connect(":memory:")
df_od.to_sql('order_detail', connection, index=False, if_exists='replace')
df_pd.to_sql('payment_detail', connection, index=False, if_exists='replace')
df_cd.to_sql('customer_detail', connection, index=False, if_exists='replace')
df_sd.to_sql('sku_detail', connection, index=False, if_exists='replace')

query = """
SELECT 
    order_detail.*,
    payment_detail.payment_method,
    customer_detail.registered_date,
    sku_detail.sku_name,
    sku_detail.base_price,
    sku_detail.cogs,
    sku_detail.category
FROM 
    order_detail
LEFT JOIN payment_detail
    ON payment_detail.id = order_detail.payment_id
LEFT JOIN customer_detail
    ON customer_detail.id = order_detail.customer_id
LEFT JOIN sku_detail
    ON sku_detail.id = order_detail.sku_id
"""
df = pd.read_sql(query, connection)
connection.close()

print(df)
df['order_date'] = pd.to_datetime(df['order_date'])
df['Month_num'] = df['order_date'].dt.month
df['Month'] = df['Month_num'].replace((1,2,3,4,5,6,7,8,9,10,11,12), ('jan','feb','march','apr','may','june','july','august','sept','okt','nov','dec'))
df.to_csv('Data Shopee.csv', index=False)
