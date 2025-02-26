def tampilkan_menu():
    print("\nTo-Do List Manager")
    print("------------------")
    print("1. Tambah Tugas")
    print("2. Lihat Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")

def tambah_tugas(to_do_list):
    tugas = input("Masukkan nama tugas: ")
    to_do_list.append({"tugas": tugas, "selesai": False})
    print(f"Tugas '{tugas}' berhasil ditambahkan.")

def lihat_tugas(to_do_list):
    if not to_do_list:
        print("Belum ada tugas dalam daftar.")
        return
    
    print("\nDaftar Tugas:")
    for idx, item in enumerate(to_do_list, start=1):
        status = "✔ Selesai" if item["selesai"] else "✖ Belum Selesai"
        print(f"{idx}. {item['tugas']} [{status}]")

def tandai_selesai(to_do_list):
    lihat_tugas(to_do_list)
    if not to_do_list:
        return

    try:
        nomor = int(input("Masukkan nomor tugas yang selesai: "))
        if 1 <= nomor <= len(to_do_list):
            to_do_list[nomor - 1]["selesai"] = True
            print(f"Tugas '{to_do_list[nomor - 1]['tugas']}' ditandai selesai.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")

def hapus_tugas(to_do_list):
    lihat_tugas(to_do_list)
    if not to_do_list:
        return

    try:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 1 <= nomor <= len(to_do_list):
            tugas = to_do_list.pop(nomor - 1)["tugas"]
            print(f"Tugas '{tugas}' berhasil dihapus.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")

def main():
    to_do_list = []
    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu: "))
            if pilihan == 1:
                tambah_tugas(to_do_list)
            elif pilihan == 2:
                lihat_tugas(to_do_list)
            elif pilihan == 3:
                tandai_selesai(to_do_list)
            elif pilihan == 4:
                hapus_tugas(to_do_list)
            elif pilihan == 5:
                print("Terima kasih telah menggunakan To-Do List Manager!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Masukkan angka yang valid.")

# Jalankan program
if __name__ == "__main__":
    main()
