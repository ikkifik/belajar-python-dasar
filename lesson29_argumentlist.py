# Belajar Argument list

def jumlahkan(*list_angka): # argument list dengan menambahkan tanda bintang di depan nama parameter(*)
    total = 0
    for jumlah in list_angka: # operasi matematika dilakukan dengan menggunakan looping
        total = total + jumlah
    print(f"Total {list_angka} = {total}")

jumlahkan(10, 5, 30, 5)

'''
notes: jika ingin membuat multiple parameter, argument list diletakkan di bagian paling belakang
def jumlahkan(x, *list_angka):
'''