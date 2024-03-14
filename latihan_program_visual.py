import numpy as np
import matplotlib.pyplot as plt

rowmax = int(1079)
colmax = int(1919)

radius_max = int(1000)
batas1 = int(0.4 * radius_max)
batas2 = int(0.5 * radius_max)
# batas3 = int(1.2 * radius_max)
# batas4 = int(1.6 * radius_max)
# batas5 = int(2 * radius_max)
# batas6 = int(2.4 * radius_max)

gambar = np.zeros(shape=(rowmax + 1, colmax + 1, 3), dtype=np.int16)
for i in range(0, rowmax + 1):
    for j in range(0, colmax + 1):
        if (i ** 2 + j ** 2) >= 0 and (i ** 2 + j ** 2) < batas1 ** 2:
            gambar[i, j] = [255, 255, 0]
        elif (i ** 2 + j ** 2) >= batas1 ** 2 and (i ** 2 + j ** 2) < batas2 ** 2:
            gambar[i, j] = [255, 0, 0]
        elif (i**2+j**2) >= batas2**2 or (i**2+j**2) < radius_max**2:
            gambar[i, j] = [255, 255, 255]


plt.figure()
plt.imshow(gambar)
plt.show()
