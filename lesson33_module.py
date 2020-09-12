# Belajar module

# jika module berada di folder yang sama, gunakan command
# import nama_module -> tanpa ekstensi .py

# import function

# import method tertentu dalam sebuah module
from function import say_hello
from function import total

hello = say_hello("Fikri") # ketika menggunakan module, panggil nama file terlebih dahulu sebelum memanggil method/function
print(hello) 

hasil = total(10, 3, 2)
print(hasil)




