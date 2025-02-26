import math

r = float(input("Masukkan jari-jari lingkaran (dalam satuan cm): "))

luas = math.pi * r ** 2
keliling = 2 * math.pi * r

print(f"Luas lingkaran dengan jari-jari {r} cm adalah: {luas:.2f} cm²")
print(f"Keliling lingkaran dengan jari-jari {r} cm adalah: {keliling:.2f} cm")
