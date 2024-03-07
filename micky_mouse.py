import matplotlib.pyplot as plt
import numpy as np

#Tentukan wilayah (domain) diagram Cartesian dan rasio lebar dan tinggi diagram
x = np.linspace(-8,7,100000)
plt.figure(figsize=(9,5.5))

#Tentukan persamaan matematika yang diinginkan
y = x -x -0
y1 = (18-x**2)**0.5
y2 = -(18-x**2)**0.5

y3 = 4 + (4-(x-4.8)**2)**0.5
y4 = 4 - (4-(x-4.8)**2)**0.5

y7 = 4 + (4-(x+4.8)**2)**0.5
y8 = 4 - (4-(x+4.8)**2)**0.5

plt.plot(x, y1, '-k')
plt.plot(x, y2, '-k')
plt.plot(x, y3, '-k')
plt.plot(x, y4, '-k')
plt.plot(x, y7, '-k')
plt.plot(x, y8, '-k')

plt.legend(loc='upper center')
plt.grid()
plt.show()