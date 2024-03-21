import numpy as np
import matplotlib.pyplot as plt

# Mengatur titik a dan b
x1, y1 = 100, 200
x2, y2 = 100, 1000
lw = 10  # Lebar garis
hw = lw // 2  # Setengah lebar garis

# Ukuran kanvas
row = int(1 * 1080)
col = int(5/7 * 1920)

# Membuat kanvas putih
Gambar = np.ones(shape=(row, col, 3), dtype=np.uint8) * 255

# Fungsi untuk menggambar titik dengan warna tertentu
def draw_point(x, y, hw, Gambar, color):
    for i in range(max(0, x-hw), min(col, x+hw)):
        for j in range(max(0, y-hw), min(row, y+hw)):
            if ((i-x)**2 + (j-y)**2) < hw**2:
                Gambar[j, i] = color

# Fungsi untuk menggambar garis putus-putus menggunakan SPL-2
def draw_dashed_spl2_line(x1, y1, x2, y2, hw, Gambar, color, dash_length=20):
    if x2 - x1 != 0:  # Handle case for non-vertical lines
        mx = (y2 - y1) / (x2 - x1)  # Gradient calculation
        x_delta = x2 - x1
        dist = np.sqrt(x_delta**2 + (y2 - y1)**2)
        dashes = int(dist / dash_length)
        for dash in range(dashes):
            start = dash / dashes
            end = (dash + 0.5) / dashes
            x_start = int(x1 + start * x_delta)
            x_end = int(x1 + end * x_delta)
            y_start = int(mx * (x_start - x1) + y1)
            y_end = int(mx * (x_end - x1) + y1)
            for x in range(x_start, x_end):
                y = int(mx * (x - x1) + y1)
                if 0 <= x < col and 0 <= y < row:  # Ensure that the points are within the canvas
                    draw_point(x, y, hw, Gambar, color)
    else:  # Handle case for vertical lines
        dist = abs(y2 - y1)
        dashes = int(dist / dash_length)
        for dash in range(dashes):
            start = dash / dashes
            end = (dash + 0.5) / dashes
            y_start = int(y1 + start * (y2 - y1))
            y_end = int(y1 + end * (y2 - y1))
            for y in range(y_start, y_end):
                if 0 <= x1 < col and 0 <= y < row:  # Ensure that the points are within the canvas
                    draw_point(x1, y, hw, Gambar, color)

# Gambar garis putus-putus menggunakan fungsi baru
draw_dashed_spl2_line(x1, y1, x2, y2, hw, Gambar, color=[255, 0, 0], dash_length=30)

# Gambar titik a dan b
draw_point(x1, y1, hw, Gambar, color=[0, 0, 255])
draw_point(x2, y2, hw, Gambar, color=[0, 0, 255])

# Gambar sumbu koordinat
plt.figure(figsize=(10, 6))
plt.imshow(Gambar)
plt.xlim(0, col)
plt.ylim(row, 0)  # Flip the y-axis to match typical Cartesian coordinate system
plt.xlabel('x')
plt.ylabel('y')
plt.scatter([x1, x2], [y1, y2], c='blue')  # Mark points a and b
plt.text(x1, y1, 'a (x1, y1)', color='blue', verticalalignment='bottom', horizontalalignment='right')
plt.text(x2, y2, 'b (x2, y2)', color='blue', verticalalignment='bottom', horizontalalignment='right')
plt.tight_layout()
plt.show()
