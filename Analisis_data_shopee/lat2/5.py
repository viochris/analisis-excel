import pandas as pd

# Contoh DataFrame
data = {'order_date': ['2021-09-15', '2021-10-05', '2021-10-12', '2021-11-20', '2021-10-25'],
        'product': ['A', 'B', 'C', 'A', 'B']}
df = pd.DataFrame(data)
print(df)

# Menambahkan kolom 'year_month'
df['order_date'] = pd.to_datetime(df['order_date'])
df['year_month'] = df['order_date'].dt.to_period('M')
print(df)

# Memilih bulan Oktober 2021
selected_month_year = pd.Period('2021-10', 'M')
df_filtered = df[df['year_month'] == selected_month_year]

# Menampilkan DataFrame setelah penyaringan
print("DataFrame setelah penyaringan:")
print(df_filtered)
