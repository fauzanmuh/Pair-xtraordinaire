import os
import time
import sys
from pyfiglet import Figlet

def animate_text(text, delay=0.1, width=50):
    fig = Figlet(font='slant')  # Menggunakan font keren
    ascii_text = fig.renderText(text).split('\n')
    
    max_length = max(len(line) for line in ascii_text)
    padding = ' ' * width  # Ruang kosong untuk animasi
    
    for i in range(width + max_length):
        os.system('cls' if os.name == 'nt' else 'clear')  # Membersihkan layar
        
        for line in ascii_text:
            print(padding[:width - i] + line)
        
        time.sleep(delay)

if __name__ == "__main__":
    text = input("Masukkan teks yang ingin dianimasikan: ")
    animate_text(text)
