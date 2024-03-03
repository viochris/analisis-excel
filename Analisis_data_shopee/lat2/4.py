import pandas as pd

# Membuat DataFrame contoh
data = {
    'order_date': pd.date_range(start='2021-01-01', end='2021-12-31', freq='D'),
    'product': ['A', 'B', 'C'] * 122,  # 3 produk untuk setiap hari
    'quantity': [1, 2, 3] * 122,  # Jumlah barang
}

df = pd.DataFrame(data)
print("DataFrame Awal:")
print(df)

# Menambahkan kolom year_month
df['year_month'] = df['order_date'].dt.to_period('M')
print("\nDataFrame dengan Kolom year_month:")
print(df)

# Memilih tahun dan bulan yang diinginkan
selected_month_year = pd.Period('2021-10', 'M')

# Melakukan filter berdasarkan tahun dan bulan yang dipilih
df_filtered = df[df['year_month'] == selected_month_year]

# Menampilkan hasil filter
print(f"\nDataFrame Setelah Filter untuk {selected_month_year}:")
print(df_filtered)
