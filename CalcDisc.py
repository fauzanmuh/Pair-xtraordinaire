def hitung_total_belanja():
    print("Selamat datang di program Kalkulator Diskon!")
    print("---------------------------------------------")
    
    total_harga = 0
    
    while True:
        try:
            harga = float(input("Masukkan harga barang (ketik 0 untuk selesai): "))
            if harga == 0:
                break
            if harga < 0:
                print("Harga tidak boleh negatif. Silakan coba lagi.")
                continue
            total_harga += harga
        except ValueError:
            print("Input tidak valid. Masukkan angka!")
    
    print("\nTotal harga sebelum diskon: Rp {:.2f}".format(total_harga))
    
    if total_harga > 500_000:
        diskon = 0.20  # Diskon 20% untuk belanja di atas 500,000
    elif total_harga > 250_000:
        diskon = 0.10  # Diskon 10% untuk belanja di atas 250,000
    else:
        diskon = 0  # Tidak ada diskon
    
    total_diskon = total_harga * diskon
    total_bayar = total_harga - total_diskon
    
    print("Diskon yang diberikan: Rp {:.2f}".format(total_diskon))
    print("Total yang harus dibayar: Rp {:.2f}".format(total_bayar))
    print("Terima kasih telah menggunakan program ini!")

# Jalankan program
if __name__ == "__main__":
    hitung_total_belanja()
