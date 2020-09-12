# Belajar Set -> konsepnya sama yaitu menyimpan data >1

# [] -> List
# () -> Tuple
# {} -> Set

# set -> jika menambahkan data harus unique/ tidak menerima data duplikat
# Set tidak mendukung pengambilan data dengan index, karena hasil akan berubah
# Mengambil data dapat menggunakan for loop
# Set hanya ada fasilitas menambah data dengan xxx.add() dan menghapus data dengan xxx.remove()

nama = {"Zuhdi", "Fikri", "Ganteng", "Banget"}
nama.remove("Zuhdi")

for i in nama:
    print(i)
print(nama)
