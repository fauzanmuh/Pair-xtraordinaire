# Fungsi untuk menghitung BMI
def hitung_bmi(berat, tinggi):
    # Menghitung BMI dengan rumus BMI = berat (kg) / (tinggi (m))^2
    bmi = berat / (tinggi ** 2)
    return bmi

# Fungsi untuk menentukan kategori BMI
def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Underweight (Kekurangan Berat Badan)"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight (Berat Badan Normal)"
    elif 25 <= bmi < 29.9:
        return "Overweight (Kelebihan Berat Badan)"
    else:
        return "Obesity (Obesitas)"

# Input berat badan dan tinggi badan dari pengguna
print("Kalkulator BMI")
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (meter): "))

# Menghitung BMI
bmi = hitung_bmi(berat, tinggi)

# Menampilkan hasil BMI dan kategori
print(f"\nBMI Anda adalah: {bmi:.2f}")
print(f"Kategori BMI Anda: {kategori_bmi(bmi)}")
