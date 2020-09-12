# Belajar Default parameter argument value
'''
def say_hello(name = "Unknown"):
    print(f"Hello {name}!")

say_hello()
'''

def say_hello(first_name = "Unknown", last_name = "Unknown"): # jika parameter pertama menggunakan default value, parameter ke 2 juga harus menggunakan default value
    print(f"Hello {first_name} {last_name}!")

say_hello()
say_hello(first_name= "Zuhdi", last_name= "Fikri")