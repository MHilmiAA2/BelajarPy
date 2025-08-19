# # Matematika
# a = int(input("Masukkan nilai a : "))
# b = int(input("Masukkan nilai b : "))
# print(a + b)   # 13
# print(a - b)   # 7
# print(a * b)   # 30
# print(a / b)   # 3.333...
# print(a % b)   # 1 (sisa bagi)
# print(a ** b)  # 1000 (pangkat)

# # Perbandingan
# print(a > b)   # True
# print(a == b)  # False

# # Logika
# x = True
# y = False
# print(x and y) # False
# print(x or y)  # True


# Tahap 2
# List = kumpulan data yang bisa diubah (mutable), ditandai dengan [].
buah = ["Jeruk", "Apel", "Mangga"]
print(buah[0])
buah.append("Pisang")
buah.remove("Apel")
print(buah)

# Tuple = mirip list, tapi tidak bisa diubah (immutable), ditandai dengan ().
warna = ("Merah", "Biru", "Hijau")
print(warna[1])

# Dictionary = data pasangan key → value, ditandai dengan {}.
kontak = {
    "Andi": "08123",
    "Budi": "08456"
}
print(kontak["Budi"])
kontak["Jujun"] = "08789"
print(kontak)

# Set = kumpulan data unik (tidak boleh duplikat), ditandai dengan {} tapi tanpa pasangan key-value.
angka = {1, 2, 3, 4, 4}
angka.add(5)
print(angka)

# Manipulasi String juga mirip list, karena bisa diakses per karakter.
teks = "Python"
print(teks[0])
print(teks[-5])
print(teks.upper())
print(teks.lower())
print(teks.replace("Py", "My"))