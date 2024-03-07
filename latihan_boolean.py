# Membaca input dari pengguna
input_a = input("Masukkan nilai a (True/False): ").lower()
input_b = input("Masukkan nilai b (True/False): ").lower()

# Konversi input menjadi boolean
a = input_a == 'true'
b = input_b == 'true'

# Menampilkan nilai variabel boolean
print("Nilai a:", a)
print("Nilai b:", b)

# Operasi logika AND
c = a and b
print("Hasil dari a AND b:", c)

# Operasi logika OR
d = a or b
print("Hasil dari a OR b:", d)

# Operasi logika NOT
e = not a
print("Hasil dari NOT a:", e)
