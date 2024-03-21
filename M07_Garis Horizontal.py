#LOW LEVEL CODING FOR CREATING POINTS
print("\033c") #To close all
import numpy as np
import matplotlib.pyplot as plt

#The user informs the coordinates of the two points for the line.
# Mengubah kode sebelumnya untuk mengikuti format gambar yang diunggah pengguna:
# - Garis putus-putus merah dengan titik ujung biru.
# - Garis koordinat (x dan y) harus ditampilkan.
# - Titik a dan b harus ditandai dengan warna biru.

# Kembali mengatur variabel yang dibutuhkan
x1, y1 = 100, 200
x2, y2 = 1800, 200
lw = 10  # Lebar garis
hw = lw // 2  # Setengah lebar garis

# Ukuran kanvas
row = int(5/7 * 1080)
col = int(1 * 1920)

# Membuat kanvas putih
# First, we need to calculate the gradient 'my'
my = (y2 - y1) / (x2 - x1)

# Then we'll recreate the canvas
Gambar = np.ones(shape=(row, col, 3), dtype=np.uint8) * 255

# Fungsi untuk menggambar titik dengan warna tertentu
def draw_point(x, y, hw, Gambar, color):
    for i in range(max(0, x-hw), min(col, x+hw)):
        for j in range(max(0, y-hw), min(row, y+hw)):
            if ((i-x)**2 + (j-y)**2) < hw**2:
                Gambar[j, i] = color

# Redefine draw_dotted_line function to include my calculation inside
def draw_dotted_line(x1, y1, x2, y2, hw, Gambar, color, dash_length=20):
    my = (y2 - y1) / (x2 - x1)  # Gradient calculation
    dx = x2 - x1
    dy = y2 - y1
    dist = np.sqrt(dx**2 + dy**2)
    dashes = int(dist / dash_length)
    for dash in range(dashes):
        start = dash / dashes
        end = (dash + 0.5) / dashes
        x_start = int(x1 + start * dx)
        x_end = int(x1 + end * dx)
        y_start = int(y1 + start * dy)
        y_end = int(y1 + end * dy)
        for x in range(x_start, x_end):
            y = int(my * (x - x1) + y1)
            if 0 <= x < col and 0 <= y < row:  # Ensure that the points are within the canvas
                draw_point(x, y, hw, Gambar, color)

# Now draw everything again
draw_dotted_line(x1, y1, x2, y2, hw, Gambar, color=[255, 0, 0])
draw_point(x1, y1, hw, Gambar, color=[0, 0, 255])
draw_point(x2, y2, hw, Gambar, color=[0, 0, 255])

# Create a new plot with the sumbu koordinat
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
