#Case 1
print("Case 1")
#Data bertipe Boolean yang Kita Deklarasikan (Cara Standar)
f = bool(True)
g = bool(False)
print(f)
print(g)
print("================================================")

# Case 2
print("Case 2")
# Boolean values in different contexts
# Automatically tracked by the computer without declaration
print(3 > 2)
print(3 + 2 == 5)
print(3 < 2)
print("=============================================================")

# Case 3
print("Case 3")
Penghasilan = 20000000
penghasilan_tanpa_pajak = 4000000
if penghasilan_tanpa_pajak >= Penghasilan:
    pajak_yang_harus_dibayar = 0
if Penghasilan > penghasilan_tanpa_pajak:
    pajak_yang_harus_dibayar = 0.1 * Penghasilan

print("Pajak yang harus Anda bayar: Rp ", pajak_yang_harus_dibayar)

print("Case 4")
# Semua data yang tidak nol (kosong) memiliki nilai Boolean True

a = 3
b = "Ini data string."
c = "laptop", "buku", "ballpen"  # tuple
d = ["laptop", "buku", "ballpen"]  # list
e = {"Laptop": "asus", "buku": "buku_teks", "ballpen": "arrow"}  # dictionary
f = {1, 2, 3, 4, 5}  # set
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print("=============================================================")

# PART 3
# Case 5: Variables that are empty have a Boolean value of False
print("Case 5")

a = 0
b = ""
c = ()
d = []
e = {}

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("=============================================================")

# Case 6: Variables with a length of zero have a Boolean value of False
print("Case 6")

class MyClass:
    def _len_(self):
        return 0

print(bool(MyClass()))
print("=============================================================")