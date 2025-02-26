import datetime


class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Selesai" if self.is_completed else "Belum Selesai"
        return f"[{status}] {self.title} - Batas waktu: {self.due_date} \nDeskripsi: {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        print(f"Tugas '{title}' berhasil ditambahkan.")

    def list_tasks(self):
        if not self.tasks:
            print("Belum ada tugas.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_as_completed()
            print(f"Tugas nomor {task_number} telah ditandai sebagai selesai.")
        else:
            print("Nomor tugas tidak valid.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Tugas '{deleted_task.title}' telah dihapus.")
        else:
            print("Nomor tugas tidak valid.")


def main():
    task_manager = TaskManager()

    while True:
        print("\nSistem Manajemen Tugas")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Tandai Tugas Selesai")
        print("4. Hapus Tugas")
        print("5. Keluar")
        
        choice = input("Pilih menu (1-5): ").strip()

        if choice == "1":
            title = input("Judul Tugas: ").strip()
            description = input("Deskripsi Tugas: ").strip()
            due_date = input("Batas Waktu (YYYY-MM-DD): ").strip()

            try:
                due_date_obj = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
                task_manager.add_task(title, description, due_date_obj)
            except ValueError:
                print("Format tanggal tidak valid. Harap gunakan format YYYY-MM-DD.")

        elif choice == "2":
            print("\nDaftar Tugas:")
            task_manager.list_tasks()

        elif choice == "3":
            try:
                task_number = int(input("Nomor tugas yang akan diselesaikan: ").strip())
                task_manager.complete_task(task_number)
            except ValueError:
                print("Harap masukkan nomor tugas yang valid.")

        elif choice == "4":
            try:
                task_number = int(input("Nomor tugas yang akan dihapus: ").strip())
                task_manager.delete_task(task_number)
            except ValueError:
                print("Harap masukkan nomor tugas yang valid.")

        elif choice == "5":
            print("Keluar dari program. Selamat tinggal!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu antara 1-5.")


if __name__ == "__main__":
    main()
