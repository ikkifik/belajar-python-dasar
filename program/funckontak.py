def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("----------------")
        print(f"Nama: {kontak['nama']}")
        print(f"Email: {kontak['email']}")
        print(f"No.telp: {kontak['telepon']}")


def new_kontak():
    nama = input("Nama: ")
    email = input("Email: ")
    telepon = input("Telepon: ")

    kontak = {
        "nama": nama,
        "email": email,
        "telepon": telepon
    }

    return kontak

def hapus_kontak(daftar_kontak):
    telepon = input("Masukkan Telepon yang akan dihapus: ")
    index = -1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telepon == kontak["telepon"]:
            index = i
            break
    if index == -1:
        print("Data tidak ditemukan")
    else:
        del daftar_kontak[index]
        print("data berhasil dihapus")
    
def cari_kontak(daftar_kontak):
    cari_nama = input("Nama yang dicari: ")
    
    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(cari_nama.lower()) != -1:
            print("----------------")
            print(f"Nama: {kontak['nama']}")
            print(f"Email: {kontak['email']}")
            print(f"No.telp: {kontak['telepon']}")

