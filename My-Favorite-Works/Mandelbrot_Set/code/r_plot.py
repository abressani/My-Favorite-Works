#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:03:47 2024

@author: alessandro
"""

import numpy as np
import matplotlib.pyplot as plt

# Initialize
x_n0 = .7
t = 1000

# Setup Axes
r = np.linspace(0, 4, 1000)
time = np.arange(t)
x_n_values = []
x_n_specific = [x_n0]

# Equation of interest
x_n1 = r*x_n0*(1-x_n0)

for j in r:
    x_n_specific = [x_n0]
    x_n = x_n0
    for i in range(time.size - 1):
        x_n1 = j*x_n*(1-x_n)
        x_n = x_n1
        x_n_specific.append(x_n1)
    x_n_values.append(x_n_specific)

# Remove first 50% of values
half = round(len(x_n_values)/2)
for n in x_n_values:
    for p in range(half):
        n.remove(n[0])
 

# Plot
fig, ax = plt.subplots()


ax.plot(list(r), x_n_values, 'bo', markersize=.01)

plt.xticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
plt.yticks([0, 0.5, 1])
ax.set(title = 'Equilibrium Position vs. Rate', xlabel = 'Rate', ylabel='Eq. Position')
ax.grid()
fig.tight_layout()
plt.show()