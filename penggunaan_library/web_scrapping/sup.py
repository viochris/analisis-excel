from urllib.request import urlopen
from bs4 import BeautifulSoup

# Pengambilan konten
url = "http://www.dicoding.com/"
page = urlopen(url)
html = page.read().decode("utf-8")

# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

footer = soup.find('footer')
footer_text = footer.get_text()

# Mencetak judul halaman
print(soup.title)
print(footer.text.strip())
print(footer_text)