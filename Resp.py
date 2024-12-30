def main():
    print("Selamat datang di program ini!")
    nama = input("Masukkan nama Anda: ")
    usia = int(input("Masukkan usia Anda: "))
    
    print(f"\nHalo, {nama}!")
    
    if usia < 18:
        print("Anda masih remaja. Nikmati masa muda Anda!")
    elif 18 <= usia < 60:
        print("Anda adalah seorang dewasa. Semangat untuk meraih impian!")
    else:
        print("Anda sudah bijaksana. Bagikan pengalaman Anda dengan generasi muda!")
    
    print("\nTerima kasih telah menggunakan program ini!")

if __name__ == "__main__":
    main()
