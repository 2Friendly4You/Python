import numpy as np
import matplotlib.pyplot as plt

d, h = 800, 600  # Pixeldichte (= Bildbreite) und Bildhöhe
n, r = 100, 2.5  # Anzahl der Iterationen und Fluchtradius (r > 2)

x = np.linspace(0, 2, num=d+1)
y = np.linspace(0, 2 * h / d, num=h+1)

A, B = np.meshgrid(x - 1, y - h / d)
C = 2.0 * (A + B * 1j) - 0.5

Z = np.zeros_like(C)
T = np.zeros(C.shape)

for k in range(n):
    M = abs(Z) < r
    T[M] = T[M] + 1
    Z[M] = Z[M] ** 2 + C[M]

plt.imshow(T ** 0.5, cmap=plt.cm.twilight_shifted)
plt.savefig("Mandelbrot_set.png", dpi=800)
