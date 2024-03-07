import numpy as np
import matplotlib.pyplot as plt

y1 = 1000
x1 = 100
y2 = 200
x2 = 100

pd = int(6); pr = 255; pg = 255; pb = 0
lw = int(6); lr = 255; lg = 255; lb = 0

col = int(1200)
row = int(1200)

def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)
    hd = int(pd/2)
    hw = int(lw/2)

    # Draw filled circles for endpoints (unchanged)
    for i in range(x1 - hd, x1 * hd):
        for j in range(y1 - hd, y1 * hd):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                gambar[j, i, 0] = pr
                gambar[j, i, 1] = pg
                gambar[j, i, 2] = pb

    for i in range(x2 - hd, x2 * hd):
        for j in range(y2 - hd, y2 * hd):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                gambar[j, i, 0] = pr
                gambar[j, i, 1] = pg
                gambar[j, i, 2] = pb

    # Draw the vertical line using pixel manipulation
    for y in range(min(y1, y2), max(y1, y2) + 1):
        for x in range(x1 - hw, x1 + hw + 1):
            gambar[y, x, 0] = lr
            gambar[y, x, 1] = lg
            gambar[y, x, 2] = lb

    return gambar

hasil = buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb)

plt.figure()
plt.imshow(hasil)
plt.show()