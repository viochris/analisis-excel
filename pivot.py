import pandas as pd

# Membuat DataFrame dari R ke Python
df_asal = pd.DataFrame({
    'AREA': ["A", "A", "B", "B", "A", "B"],
    'CUSTOMER_NAME': ["Cust1", "Cust2", "Cust1", "Cust2", "Cust1", "Cust2"],
    'CUSTOMER_NAME2': ["Cust3", "Cust4", "Cust3", "Cust4", "Cust3", "Cust4"],
    'BOX_QTY': [10, 20, 15, 25, 30, 35],
    'TOTAL_WEIGHT': [100, 200, 150, 250, 300, 350]
})

print(df_asal)

pivot = pd.pivot_table(df_asal, index = ['AREA', 'CUSTOMER_NAME', 'CUSTOMER_NAME2'], values = ['BOX_QTY', 'TOTAL_WEIGHT'], aggfunc=sum)
print(pivot)