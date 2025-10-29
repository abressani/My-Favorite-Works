#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 12:24:22 2024

@author: alessandro
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,fftfreq,fftshift

# Initialize
c = -1.385
z_n = 0
t = 250

# Setup Axes
time = np.arange(t)
z_n_values = np.array([z_n])

# Equation of interest
z_n1 = z_n**2 + c

for i in range(time.size - 1):
    z_n1 = z_n**2 + c
    z_n = z_n1
    z_n_values = np.append(z_n_values, z_n1)
    
# Fourier Analysis
# Won't work well for small timeframe
# Sample Sizes
samples = time.size
start_time = 0
end_time = time.size
samplerate = samples/(end_time - start_time)
h = 1/samplerate

YN = fft(z_n_values)
YN = abs(YN)
frequency = fftfreq(time.size, d = h)


# Plot
fig, ax = plt.subplots(2,1)

ax[0].plot(time, z_n_values, 'b')
ax[0].set(title = 'Equilibrium Position', xlabel = 'Iterations', ylabel='Eq Position')
ax[0].grid()

#ax[0].set_ylim(-0.5, 1)

ax[1].plot(abs(frequency), YN.real, 'r')
ax[1].set(title = 'Fourier Analysis', xlabel = 'Frequency', ylabel='Amplitude')
ax[1].grid()

ax[1].set_xlim(.01, .49)
#ax[1].set_ylim(-10, 150)

fig.tight_layout()
plt.show()