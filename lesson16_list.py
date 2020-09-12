# Belajar (Struktur data)List -> []

nama = ["Zuhdi", "Ganteng", "Fikri", "Tampan"]
# index->  0         1          2        3
print(nama)
print(nama[1])

# memasukkan data ke dalam List
nama.append("Sekali")
print(nama)
print(nama[4])

# menghitung jumlah data list
print(len(nama))

# menghapus data
nama.remove("Ganteng")
print(nama)
print(nama[1]) # karena "Ganteng" berada di index ke 1, ketika dihapus maka data "Fikri" akan bergeser ke depan