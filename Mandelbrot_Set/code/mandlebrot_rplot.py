#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 12:57:23 2024

@author: alessandro
"""

import numpy as np
import matplotlib.pyplot as plt

# Initialize
z_n0 = 0
t = 1000

# Setup Axes
c = np.linspace(-2, .5, 1000)
time = np.arange(t)
z_n_values = []
z_n_specific = [z_n0]

# Equation of interest
z_n1 = z_n0**2 + c

for j in c:
    z_n_specific = [z_n0]
    z_n = z_n0
    for i in range(time.size - 1):
        z_n1 = z_n**2 + j
        z_n = z_n1
        z_n_specific.append(z_n1)
    z_n_values.append(z_n_specific)

# Remove first 50% of values
half = round(len(z_n_values)/2)
for n in z_n_values:
    for p in range(half):
        n.remove(n[0])
 

# Plot
fig, ax = plt.subplots()

ax.plot(list(c), z_n_values, 'bo', markersize=.01)

plt.xticks([-2, -1.5, -1, -0.5, 0, 0.25, 0.5])
ax.set(title = 'Rate to equilibrium position', xlabel = 'c-value', ylabel='Eq. Position')
ax.grid()
fig.tight_layout()
plt.show()