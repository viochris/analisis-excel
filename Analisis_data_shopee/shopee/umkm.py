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
bars = ax.barh(df['Nama Data'], df['Nilai'], color='skyblue')
# Menetapkan judul plot
ax.set_title('Preferensi Pembelian Produk UMKM')
# Menetapkan label sumbu x
ax.set_xlabel('Persentase (%)')
# Rotasi label sumbu x agar lebih mudah dibaca
plt.yticks(rotation=45, ha='right')

# Menambahkan label angka di ujung barh
for bar in bars:
    yval = bar.get_width()
    ax.text(yval, bar.get_y() + bar.get_height()/2, round(yval, 2), va='center', ha='left')

ax.invert_yaxis()
# Menampilkan plot
plt.show()
