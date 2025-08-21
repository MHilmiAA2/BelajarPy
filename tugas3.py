
# siswa = {
#     "Andi": "80"
# }
# while True:
#     print("1. Tambah Siswa")
#     print("2. Lihat Nilai")
#     print("3. Hitung Rata-Rata Kelas")
#     print("4. Keluar")

#     x = int(input("Pilih nomor :"))

#     if x == 1:
#         a = str(input("\nMasukkan Nama Siswa : "))
#         b = str(input("Masukkan Nilai Siswa : "))
#         siswa[a] = b
#         print("Data siswa berhasil ditambahkan!\n")

#     elif x == 2:
#         print("\nDaftar Siswa dan Nilai")
#         for nama, nilai in siswa.items():
#             print(f"{nama} : {nilai}")
#             y = ''.join({nilai})
#             z = int(y)
#             if z >= 70:
#                 print("Lulus")
#             else:
#                 print("Tidak Lulus")

#     elif x == 3:
#         print("\nNilai rata-rata siswa")
#         nilaiFloat = [float(v) for v in siswa.values()]
#         rataRata = sum(nilaiFloat) / len(nilaiFloat)
#         print(rataRata)

#     elif x == 4:
#         print("Sampai Jumpa Lagi!")
#         break

#     else:
#         print("Harap masukkan nomor dengan benar!")


# Revisi
siswa = {
    "Andi": 80
}

def tambah_siswa():
    a = input("\nMasukkan Nama Siswa : ")
    b = int(input("Masukkan Nilai Siswa : "))
    siswa[a] = b
    print("Data siswa berhasil ditambahkan!\n")

def lihat_nilai():
    print("\nDaftar Siswa dan Nilai")
    for nama, nilai in siswa.items():
        status = "Lulus" if nilai >= 70 else "Tidak Lulus"
        print(f"{nama} : {nilai} ({status})")

def hitung_rata_rata():
    print("\nNilai rata-rata siswa")
    nilaiFloat = [float(v) for v in siswa.values()]
    rataRata = sum(nilaiFloat) / len(nilaiFloat)
    print("Rata-rata:", rataRata)

while True:
    print("\n=== Menu Nilai Siswa ===")
    print("1. Tambah Siswa")
    print("2. Lihat Nilai")
    print("3. Hitung Rata-Rata Kelas")
    print("4. Keluar")

    x = int(input("Pilih nomor : "))

    if x == 1:
        tambah_siswa()
    elif x == 2:
        lihat_nilai()
    elif x == 3:
        hitung_rata_rata()
    elif x == 4:
        print("Sampai Jumpa Lagi!")
        break
    else:
        print("Harap masukkan nomor dengan benar!")
