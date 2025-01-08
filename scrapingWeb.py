## pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# URL yang akan di-scrape
url = 'https://example.com'  # Ganti dengan URL yang Anda tuju

# Mengirim permintaan GET ke URL
response = requests.get(url)

# Memeriksa apakah permintaan berhasil (status code 200)
if response.status_code == 200:
    # Parsing konten HTML menggunakan BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Menemukan semua elemen dengan tag <h2> yang berisi judul artikel
    # (Anda bisa mengganti tag atau selector sesuai dengan struktur HTML halaman yang ingin di-scrape)
    titles = soup.find_all('h2')  # Misalnya artikel berada dalam <h2>

    # Menampilkan semua judul artikel yang ditemukan
    for title in titles:
        print(title.get_text())  # Mendapatkan teks dari elemen <h2>

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
