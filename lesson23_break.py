# Belajar Break -> menghentikan proses jika suatu kondisi terpenuhi
'''
for i in range(1, 100):
    if i % 50 == 0: # ketika mencapai modulus 50 perulangan akan dihentikan
        break
    print(i)
'''

while True:
    data = input("data: ")
    if data == "x":
        break
    print(data)

print("Terimakasih")