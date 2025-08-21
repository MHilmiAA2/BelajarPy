import os

def tambahFile():
    namaFile = input("Nama File :")
    isiFile = input("Isi Catatan :")
    print("Catatan berhasil dibuat!")

    with open(namaFile + ".txt", "w") as file:
        file.write(isiFile)

def cariFile():
    namaFile = str(input("Nama file yang dicari :"))
    try:
        with open(namaFile + ".txt", "r") as file:
            isi = file.read()
            print(isi)
    except FileNotFoundError:
        print("File yang dicari tidak ada!")
    except Exception as e:
        print(f"Terjadi kesalahan : {e}")

def hapusCatatan():
    namaFile = input("File yang ingin dihapus :")
    hapusFile = f"{namaFile}.txt"
    try:
        os.remove(hapusFile)
        print(f"File {namaFile} berhasil dihapus!")
    except FileNotFoundError:
        print("File tidak ditemukan!")
    except PermissionError:
        print(f"Tidak memiliki izin untuk menghapus file {namaFile}")
    except Exception as e:
        print(f"Terjadi kesalahan : {e}")

while True:
    print("1. Tambah Catatan")
    print("2. Lihat Catatan")
    print("3. Hapus Catatan")
    print("4. Keluar")

    try:
        x = int(input("Pilih nomor :"))
    except ValueError:
        print("Harap masukkan angka!")

    if x == 1:
        tambahFile()
    elif x == 2:
        cariFile()
    elif x == 3:
        hapusCatatan()
    elif x == 4:
        print("Sampai Jumpa Kawan!")
        break
    else:
        print("Harap masukkan nomor dengan benar!")