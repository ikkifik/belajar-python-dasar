# Belajar Dictionary

# [] -> List
# () -> Tuple
# {} -> Set
# {key:value} -> dictionary

customer = {
    "name": "Fikri", # penamaan key pada dictionary case-sensitive, besar kecil huruf diperhatikan!
    "age": 20,
    "address": "Jogja"
}

# menambahkan dan mengubah data baru ke dalam dictionary
customer["company"] = "X"
customer["name"] = "Zuhdi"

del customer["address"] # menghapus key dan value address

# pemanggilan data dictionary dengan loop
for key, value in customer.items(): 
    print(f"{key}:{value}")

