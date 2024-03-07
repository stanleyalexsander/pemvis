# Membaca elemen-elemen set dari input pengguna
set1_elements = input("Masukkan elemen-elemen set 1 (pisahkan dengan koma): ").split(',')
set2_elements = input("Masukkan elemen-elemen set 2 (pisahkan dengan koma): ").split(',')

# Membuat set dari elemen-elemen yang dimasukkan pengguna
set1 = set(map(int, set1_elements))
set2 = set(map(int, set2_elements))

print("Set 1:", set1)
print("Set 2:", set2)

# Operasi gabungan (union) dari dua set
union_set = set1.union(set2)
print("Gabungan dari dua set:", union_set)

# Operasi irisan (intersection) dari dua set
intersection_set = set1.intersection(set2)
print("Irisan dari dua set:", intersection_set)

# Operasi selisih (difference) antara set1 dan set2
difference_set = set1.difference(set2)
print("Selisih set1 dan set2:", difference_set)

# Operasi selisih simetris (symmetric difference) antara dua set
symmetric_difference_set = set1.symmetric_difference(set2)
print("Selisih simetris dari dua set:", symmetric_difference_set)

# Menambahkan elemen ke dalam set1
elem_to_add = int(input("Masukkan elemen yang ingin ditambahkan ke dalam set 1: "))
set1.add(elem_to_add)
print("Set 1 setelah menambahkan elemen", elem_to_add, ":", set1)

# Menghapus elemen dari set2
elem_to_remove = int(input("Masukkan elemen yang ingin dihapus dari set 2: "))
set2.discard(elem_to_remove)
print("Set 2 setelah menghapus elemen", elem_to_remove, ":", set2)
