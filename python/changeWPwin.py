import os
import time
import requests
import ctypes
from io import BytesIO
from PIL import Image

# URL untuk mengambil gambar acak dari Unsplash
UNSPLASH_URL = "https://source.unsplash.com/random/1920x1080"

# Folder untuk menyimpan gambar sementara
WALLPAPER_DIR = os.path.join(os.getcwd(), "wallpapers")
if not os.path.exists(WALLPAPER_DIR):
    os.makedirs(WALLPAPER_DIR)

def download_random_image():
    """Mendownload gambar acak dari Unsplash dan menyimpannya."""
    response = requests.get(UNSPLASH_URL)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image_path = os.path.join(WALLPAPER_DIR, "wallpaper.jpg")
        image.save(image_path)
        return image_path
    return None

def set_wallpaper(image_path):
    """Mengatur gambar sebagai wallpaper desktop."""
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

def main():
    """Loop utama untuk mengganti wallpaper setiap 10 detik."""
    print("Memulai penggantian wallpaper otomatis...")
    while True:
        image_path = download_random_image()
        if image_path:
            set_wallpaper(image_path)
            print(f"Wallpaper diperbarui: {image_path}")
        time.sleep(10)  # Ganti wallpaper setiap 10 detik

if __name__ == "__main__":
    main()
