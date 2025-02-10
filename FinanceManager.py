import csv
import os

class FinanceManager:
    def __init__(self, filename="finance_data.csv"):
        self.filename = filename
        self.transactions = []
        self.load_data()

    def load_data(self):
        """Memuat data dari file CSV jika ada."""
        if os.path.exists(self.filename):
            with open(self.filename, mode="r") as file:
                reader = csv.reader(file)
                next(reader, None)  # Lewati header
                self.transactions = [{"type": row[0], "amount": float(row[1]), "description": row[2]} for row in reader]

    def save_data(self):
        """Menyimpan data transaksi ke file CSV."""
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Amount", "Description"])
            for transaction in self.transactions:
                writer.writerow([transaction["type"], transaction["amount"], transaction["description"]])

    def add_transaction(self, trans_type, amount, description):
        """Menambahkan transaksi baru (pemasukan/pengeluaran)."""
        self.transactions.append({"type": trans_type, "amount": amount, "description": description})
        self.save_data()
        print(f"✅ {trans_type.capitalize()} sebesar Rp {amount:,} telah ditambahkan.")

    def show_summary(self):
        """Menampilkan ringkasan keuangan."""
        total_income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        total_expense = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        balance = total_income - total_expense

        print("\n===== RINGKASAN KEUANGAN =====")
        print(f"Total Pemasukan: Rp {total_income:,}")
        print(f"Total Pengeluaran: Rp {total_expense:,}")
        print(f"Saldo Akhir: Rp {balance:,}\n")

    def run(self):
        """Menjalankan aplikasi dalam mode interaktif."""
        while True:
            print("\n==== Manajemen Keuangan ====")
            print("1. Tambah Pemasukan")
            print("2. Tambah Pengeluaran")
            print("3. Lihat Ringkasan Keuangan")
            print("4. Keluar")
            choice = input("Pilih opsi (1-4): ")

            if choice == "1":
                amount = float(input("Masukkan jumlah pemasukan: Rp "))
                description = input("Masukkan keterangan: ")
                self.add_transaction("income", amount, description)

            elif choice == "2":
                amount = float(input("Masukkan jumlah pengeluaran: Rp "))
                description = input("Masukkan keterangan: ")
                self.add_transaction("expense", amount, description)

            elif choice == "3":
                self.show_summary()

            elif choice == "4":
                print("👋 Keluar dari aplikasi.")
                break
            else:
                print("⚠️ Pilihan tidak valid. Coba lagi.")

# Jalankan program
if __name__ == "__main__":
    app = FinanceManager()
    app.run()
