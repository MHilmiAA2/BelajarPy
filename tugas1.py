# Kalkulator
a = int(input("Masukkan angka pertama : "))
b = int(input("Masukkan angka kedua : "))

y = input("Pilih operasi hitung (+, -, /, *, ^, %, q untuk keluar) : ")

if y == "+":
    print("Hasil : ", a + b)
elif y == "-":
    print("Hasil : ", a - b)
elif y == "/":
    print("Hasil : ", a / b)
elif y == "*":
    print("Hasil : ", a * b)
elif y == "^":
    print("Hasil : ", a ** b)
elif y == "%":
    print("Hasil : ", a % b)
elif y == "q":
    print("Terimakasih sudah menggunakan kalkulator")
else:
    print("Operasi tidak valid")