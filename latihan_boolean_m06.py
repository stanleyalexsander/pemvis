# 1. ada 2 input (masukkan nilai) a dan b
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

# 2. output berupa print
print("Nilai a: ", a)
print("Nilai b: ", b)

# 3. cek dengan boolean apakah a lebih besar dari b?
a_lebih_b = a > b
print("a lebih besar dari b:", a_lebih_b)

# 4. cek dengan boolean apakah b lebih besar dari a?
b_lebih_a = b > a
print("b lebih besar dari a:", b_lebih_a)

# 5. cek dengan boolean apakah a sama dengan b?
a_sama_b = a == b
print("a sama dengan b:", a_sama_b)

# 6. hitung ppn a sebesar 12%, jika lebih dari 10000
ppn_a = a * 0.12 if a > 10000 else 0
print("PPN a:", ppn_a)

# 7. hitung ppn b sebesar 12%, jika lebih dari 50000
ppn_b = b * 0.12 if b > 50000 else 0
print("PPN b:", ppn_b)

# 8. tambahkan keduai ppn a dan b, cek dengan boolean
total_ppn = ppn_a + ppn_b
print("Total PPN:", total_ppn, "(" + str(bool(total_ppn)) + ")")

# 9. hapus a dan b, cek dengan boolean
a = 0
b = 0
print("Nilai a:", bool(a))
print("Nilai b:", bool(b))
