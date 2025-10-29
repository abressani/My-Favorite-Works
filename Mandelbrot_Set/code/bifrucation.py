#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:54:20 2024

@author: alessandro
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,fftfreq,fftshift

# Initialize
r = 3.843
#r = 3.9
x_n = .3
t = 150

# Setup Axes
time = np.arange(t)
x_n_values = np.array([x_n])

# Equation of interest
x_n1 = r*x_n*(1-x_n)

for i in range(time.size - 1):
#    print(x_n)
    x_n1 = r*x_n*(1-x_n)
    x_n = x_n1
    x_n_values = np.append(x_n_values, x_n1)
    
# Fourier Analysis
# Won't work well for small timeframe
# Sample Sizes
samples = time.size
start_time = 0
end_time = time.size
samplerate = samples/(end_time - start_time)
h = 1/samplerate

YN = fft(x_n_values)
YN = abs(YN)
frequency = fftfreq(time.size, d = h)


# Plot
#fig, ax = plt.subplots(2,1)
fig, ax = plt.subplots()

ax.plot(time, x_n_values, 'b')
ax.set(title = 'Equilibrium Population', xlabel = 'Time (yrs)', ylabel='Pct. Possible Population')
ax.grid()

ax.set_ylim(-.1, 1.1)

'''
ax[1].plot(abs(frequency), YN.real, 'r')
ax[1].set(title = 'Fourier Analysis', xlabel = 'Frequency', ylabel='Amplitude')
ax[1].grid()

ax[1].set_xlim(.01, .55)
#ax[1].set_ylim(-10, 150)
'''

fig.tight_layout()
plt.show()