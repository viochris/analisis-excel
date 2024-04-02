import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('umkm.xlsx')
df = df.drop('No.', axis=1)
df['Nilai'] = df['Nilai'].str.replace(",", ".").astype(float)
print(df)
print(df.dtypes)

# Membuat subplots
fig, ax = plt.subplots()
# Membuat horizontal bar plot
bars = ax.bar(df['Nama Data'], df['Nilai'], color='skyblue')
# Menetapkan judul plot
ax.set_title('Preferensi Pembelian Produk UMKM')
# Menetapkan label sumbu x
ax.set_xlabel('Persentase (%)')
# Rotasi label sumbu x agar lebih mudah dibaca
plt.xticks(rotation=45, ha='right')


# Menambahkan label angka di ujung bar
for bar in bars:
    height = bar.get_height()
    ax.annotate('{}'.format(round(height, 2)),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Menampilkan plot
plt.show()
