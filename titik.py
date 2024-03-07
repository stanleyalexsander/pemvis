import numpy as np
import matplotlib.pyplot as plt

# User entries the user informs the coordinates
x1 = 100; y1 = 200
x2 = 700; y2 = 700

# The user decides the line width
lw = int(10)

# Calculate the half line canvas
hw = int(lw/2)

# Setting the size of the canvas
col = int(800)
row = int(800)
print("col, row =", col, ",", row)

# Preparing the lack canvas
gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
gambar[:, :, :] = 255       # Mengubah layar ke putih

# Warna hijau
hijau = (0, 255, 0)

# Menggambar titik dengan satu piksel
gambar[y1, x1, :] = hijau
gambar[y2, x2, :] = hijau
# gambar[y1, x1, 0] = 255

for i in range(x1-hw, x1+hw):
    for j in range(y1-hw, y1+hw):
        if ((i - x1)**2 + (j-y1)**2) < hw **2:
            gambar[j, i, :] = hijau
            # gambar[j, i, 0] = 255

for i in range(x2-hw, x2+hw):
    for j in range(y2-hw, y2+hw):
        if ((i - x2)**2 + (j-y2)**2) < hw **2:
            gambar[j, i, :] = hijau
            # gambar[j, i, 0] = 255

plt.figure()
plt.imshow(gambar)
plt.show()