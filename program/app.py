# Program management kontak

# import function
import funckontak

# List of dictionary
daftar_kontak = []
daftar_kontak.append({
    "nama": "Zuhdi Fikri",
    "email": "fikriganteng@gmail.com",
    "telepon": "097867222123"
})

daftar_kontak

# Menu program
while True:
    print("===================")
    print("Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar")

    menu = input("Pilih menu: ")

    if menu == "0":
        break
    elif menu == "1":
        funckontak.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = funckontak.new_kontak()
        daftar_kontak.append(kontak)
    elif menu == "3":
        funckontak.hapus_kontak(daftar_kontak)
    elif menu == "4":
        funckontak.cari_kontak(daftar_kontak)
    else:
        print("Menu tidak tersedia!")
        break



print("Program selesai berjalan, terimakasih!")