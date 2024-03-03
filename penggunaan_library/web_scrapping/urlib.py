from urllib.request import urlopen

# Pengambilan konten
url = "http://www.dicoding.com/"
page = urlopen(url)
html = page.read().decode("utf-8")

# Mencari indeks awal dan akhir
start_index = html.find("<footer>") + len("<footer>")
end_index = html.find("</footer>")

# Mengekstrak dan mencetak judul halaman
title = html[start_index:end_index]
print(title)