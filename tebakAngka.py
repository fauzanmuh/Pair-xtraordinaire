import random

def tebak_angka():
    print("Selamat datang di Game Tebak Angka!")
    print("Saya telah memilih sebuah angka antara 1 sampai 100.")
    print("Coba tebak angkanya!")

    # Komputer memilih angka secara acak
    angka_rahasia = random.randint(1, 100)
    percobaan = 0
    
    while True:
        try:
            # Meminta tebakan dari pengguna
            tebakan = int(input("Masukkan tebakan Anda: "))
            percobaan += 1
            
            if tebakan < angka_rahasia:
                print("Terlalu kecil! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu besar! Coba lagi.")
            else:
                print(f"Selamat! Anda berhasil menebak angkanya {angka_rahasia} dalam {percobaan} percobaan.")
                break
        except ValueError:
            print("Masukkan angka yang valid!")

if __name__ == "__main__":
    tebak_angka()
