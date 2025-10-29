#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:34:29 2024

@author: alessandro
"""
import numpy as np
import matplotlib.pyplot as plt

#Creating lattice
N = 300
comp_plane = np.zeros([N,N])
zarr = np.zeros((N,N,3), dtype=int)
zarr[:N] = [255,0,0]

x = np.linspace(-2, 1, N)
y = 1j*np.linspace(-1, 1, N)
imag_nums = np.array([])

# Making sample of complex numbers
for i in x:
    for j in y:
        imag_nums = np.append(imag_nums, i + j)

# Making the set
x_index = 0
y_index = 0
for k in imag_nums:
    z_n0 = 0
    z_n = 0
    t = 25
    time = np.arange(t)
    for i in range(time.size - 1):
        z_n1 = z_n**2 + k
        z_n = z_n1
        if np.real(z_n) > 10:
            zarr[x_index, y_index] = [0,0,80]
            break
    x_index += 1
    if x_index > N-1:
        x_index = 0
        y_index += 1

# Plot
fig, ax = plt.subplots()
ax.imshow(zarr,interpolation='none')
ax.set_title('Mandlebrot Set')
ax.set_xlabel('Real Numbers')
ax.set_ylabel('Imaginary Numbers')

plt.tight_layout()
plt.show()