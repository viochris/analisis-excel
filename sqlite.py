import sqlite3

# Membuat koneksi ke database (jika database tidak ada, akan dibuat baru)
conn = sqlite3.connect('example.db')

# Membuat kursor untuk berinteraksi dengan database
cursor = conn.cursor()

# Membuat tabel
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Memasukkan beberapa data ke dalam tabel
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 25))

# Menyimpan perubahan (commit) ke database
conn.commit()

# Melakukan kueri untuk mengambil data dari tabel
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Menampilkan hasil kueri
for row in rows:
    print(row)

# Menutup koneksi
conn.close()
