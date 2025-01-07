import csv

def process_csv(input_file, output_file):
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Menambahkan kolom baru di header
            fieldnames = reader.fieldnames + ['Total']
            rows = []

            for row in reader:
                # Contoh: Menambahkan nilai di kolom 'Total' berdasarkan kolom 'Price' dan 'Quantity'
                price = float(row.get('Price', 0))
                quantity = int(row.get('Quantity', 0))
                row['Total'] = price * quantity
                rows.append(row)

        # Menyimpan hasil ke file baru
        with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"File berhasil diproses. Hasil disimpan di: {output_file}")

    except FileNotFoundError:
        print(f"Error: File {input_file} tidak ditemukan.")
    except Exception as e:
        print(f"Error: {e}")

# Contoh penggunaan
input_file = 'input.csv'   # Ganti dengan path file input Anda
output_file = 'output.csv' # Ganti dengan nama file output
process_csv(input_file, output_file)
