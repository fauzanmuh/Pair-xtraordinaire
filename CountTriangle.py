def hitung_luas_segitiga(alas, tinggi):
    """
    Menghitung luas segitiga menggunakan rumus:
    luas = 0.5 * alas * tinggi
    """
    return 0.5 * alas * tinggi


def main():
    print("Program Penghitung Luas Segitiga")
    print("-" * 30)

    # Input alas dan tinggi dari pengguna
    try:
        alas = float(input("Masukkan panjang alas (cm): "))
        tinggi = float(input("Masukkan tinggi segitiga (cm): "))

        # Validasi input
        if alas <= 0 or tinggi <= 0:
            print("Alas dan tinggi harus bernilai positif.")
            return

        # Hitung luas
        luas = hitung_luas_segitiga(alas, tinggi)
        print(f"Luas segitiga adalah {luas:.2f} cm²")

    except ValueError:
        print("Input harus berupa angka.")


# Menjalankan program utama
if __name__ == "__main__":
    main()
