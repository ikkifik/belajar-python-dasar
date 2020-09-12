# Belajar Continue -> digunakan untuk 'skip' proses dalam perulangan

for i in range(1, 100):
    if i % 2 == 0: # jika nilai true, maka akan kembali ke atas tanpa print hasil dibawahnya terlebih dahulu
        continue
    print(i)
    