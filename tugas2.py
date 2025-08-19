# print("1. Tambah Kontak")
# print("2. Lihat Semua Kontak")
# print("3. Cari Kontak")
# print("4. Hapus Kontak")
# print("5. Keluar")

# x = int(input("Pilih Menu : "))

# kontak = {
#     "Ardi": "08123",
#     "Budi": "08456"
# }

# if x == 1:
#     a = str(input("Masukkan Nama : "))
#     b = int(input("Masukkan Nomor : "))
#     kontak[a] = b
#     print("Kontak Berhasil Ditambah")
#     print(kontak)
# elif x == 2:
#     print(kontak)
# elif x == 3:
#     a = str(input("Siapa yang dicari : "))
#     print(kontak[a])
# elif x == 4:
#     a = str(input("Siapa yang mau dihapus : "))
#     kontak.remove(a)
# elif x == 5:
#     print("Sampai Jumpa Lagi!")
# else:
#     print("Perintah tidak ditemukan")


# Revisi
kontak = {
    "Ardi": "08123",
    "Budi": "08456"
}

while True:
    print("=== Menu Kontak ===")
    print("1. Tambah Kontak")
    print("2. Lihat Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")

    x = int(input("Pilih Nomor : "))

    if x == 1:
        a = str(input("Masukkan Nama : "))
        b = str(input("Masukkan Nomor : "))
        kontak[a] = b
        print("Kontak Berhasil Ditambahkan!")

    elif x == 2:
        print("\nDaftar Kontak")
        for nama, nomor in kontak.items():
            print(f"{nama} : {nomor}")

    elif x == 3:
        a = str(input("Siapa yang dicari? : "))
        if a in kontak:
            print(f"{a} : {kontak[a]}")
        else:
            print("Kontak tidak tersedia")

    elif x == 4:
        a = str(input("Siapa yang mau dihapus? : "))
        if a in kontak:
            del kontak[a]
            print("Kontak berhasil dihapus!")
        else:
            print("Kontak tidak ditemukan")

    elif x == 5:
        print("Sampai jumpa lagi!")
        break

    else:
        print("Perintah tidak ditemukan")