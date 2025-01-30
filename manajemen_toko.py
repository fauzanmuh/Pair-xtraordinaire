# Program Sistem Manajemen Toko Sederhana

# Dictionary untuk menyimpan inventaris produk
inventaris = {}

def tambah_produk():
    nama = input("Masukkan nama produk: ")
    harga = float(input("Masukkan harga produk: "))
    stok = int(input("Masukkan stok produk: "))
    
    if nama in inventaris:
        print("Produk sudah ada. Stok akan diperbarui.")
        inventaris[nama]['stok'] += stok
    else:
        inventaris[nama] = {'harga': harga, 'stok': stok}
    print(f"Produk '{nama}' berhasil ditambahkan/ diperbarui.")

def lihat_produk():
    if not inventaris:
        print("Inventaris kosong.")
    else:
        print("\nDaftar Produk:")
        for nama, detail in inventaris.items():
            print(f"Nama: {nama}, Harga: Rp{detail['harga']}, Stok: {detail['stok']}")

def hapus_produk():
    nama = input("Masukkan nama produk yang ingin dihapus: ")
    if nama in inventaris:
        del inventaris[nama]
        print(f"Produk '{nama}' berhasil dihapus.")
    else:
        print(f"Produk '{nama}' tidak ditemukan.")

def main():
    while True:
        print("\n=== Sistem Manajemen Toko ===")
        print("1. Tambah Produk")
        print("2. Lihat Produk")
        print("3. Hapus Produk")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            tambah_produk()
        elif pilihan == '2':
            lihat_produk()
        elif pilihan == '3':
            hapus_produk()
        elif pilihan == '4':
            print("Terima kasih! Program dihentikan.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program
if __name__ == "__main__":
    main()
