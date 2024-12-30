# Program Kalkulator Dasar
def kalkulator():
    print("=== Kalkulator Dasar ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("========================")

    pilihan = int(input("Pilih operasi (1/2/3/4): "))

    if pilihan not in [1, 2, 3, 4]:
        print("Pilihan tidak valid. Silakan coba lagi.")
        return

    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input harus berupa angka!")
        return

    # Melakukan operasi berdasarkan pilihan
    if pilihan == 1:
        hasil = angka1 + angka2
        operasi = "Penjumlahan"
    elif pilihan == 2:
        hasil = angka1 - angka2
        operasi = "Pengurangan"
    elif pilihan == 3:
        hasil = angka1 * angka2
        operasi = "Perkalian"
    elif pilihan == 4:
        if angka2 == 0:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
            return
        hasil = angka1 / angka2
        operasi = "Pembagian"

    print(f"\nHasil {operasi}: {hasil}")

if __name__ == "__main__":
    kalkulator()
