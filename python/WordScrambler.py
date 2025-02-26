import random

def word_scrambler():
    print("Selamat datang di Pengacak Kata!")
    print("Masukkan sebuah kata, dan program akan mengacak hurufnya.")
    
    word = input("Masukkan kata: ")
    
    if len(word) > 1:
        # Mengacak huruf-huruf pada kata
        scrambled = ''.join(random.sample(word, len(word)))
        print(f"Kata asli: {word}")
        print(f"Kata yang sudah diacak: {scrambled}")
    else:
        print("Masukkan kata yang lebih panjang dari satu huruf.")
    
if __name__ == "__main__":
    word_scrambler()
