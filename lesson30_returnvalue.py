# Belajar Method Return value -> method function
# setelah kode program selesai dieksekusi akan mengembalikan nilai

# dengan menggunakan return value dapat lebih memfokuskan method pada fungsinya.
def jumlahkan(*list_angka): 
    total = 0
    for jumlah in list_angka: 
        total = total + jumlah
    return (total, list_angka) # mendefinisikan variabel method

total, list_angka = jumlahkan(10, 5, 30, 5) # pembuatan variabel hasil dari return value method

# Mengambil data total?
print(f"Hasil dari {list_angka} adalah {total}")
