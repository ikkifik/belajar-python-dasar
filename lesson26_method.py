# Belajar membuat method / function
# tempat menyimpan code-block yang dapat dieksekusi berulang kali
# eksekusi method setelah didefinisikan

nama = []

def template():
    print("================")
    for data in nama:
        print(data)

nama.append("Zuhdi")
template()

nama.append("Fikri")
template()

nama.append("Ganteng")
template()