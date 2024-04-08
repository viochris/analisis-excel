import pandas as pd

# Membuat dataframe dengan data yang lebih banyak
import numpy as np
np.random.seed(123)
n_rows = 1000
df = pd.DataFrame({
    'sku_name': np.random.choice(list('ABCDE'), n_rows),
    'category': np.random.choice(['X', 'Y', 'Z'], n_rows),
    'customer_id': np.random.randint(1, 201, n_rows)
})
print(df.shape)

# Menggunakan drop_duplicates bersama dengan groupby
tabel2 = df.drop_duplicates('customer_id')
print(tabel2.shape)
tabel2 = tabel2.groupby(['sku_name', 'category'])['customer_id'].nunique().reset_index(name='jumlah_pelanggan')

# Menampilkan hasil
print(tabel2)
