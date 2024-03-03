import requests
from bs4 import BeautifulSoup

# URL halaman web yang ingin di-scrape
url = "http://www.dicoding.com/"

# Mengambil konten halaman web
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    footer = soup.find('footer')
    footer_text = footer.get_text()
    print(footer_text)
else:
    print("Gagal mengambil konten halaman web.")