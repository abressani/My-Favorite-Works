#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:28:21 2024

@author: alessandro
"""
import numpy as np
import math
import matplotlib.pyplot as plt


# Change target number (1-7) to see data of other stars
f = open('target4mags','r')

# Creating arrays of data
mag = np.array([])
magerr = np.array([])
time = np.array([])
tvar = 0
for line in f:
    s = line.split()
    mag = np.append(mag,float(s[1]))
    magerr = np.append(magerr,float(s[2]))
    tvar += 25
    time = np.append(time, tvar)
f.close()

# Check averge values of magnitudes by setting this to 20, then lower to remove outliers 
highest = 12

for n in range(len(mag)):
    if mag[n] > highest:
        magerr = np.delete(magerr, n)
        time = np.delete(time, n)
mag = mag[mag <= highest]

'''
Plotting Info
    Change title of graph accordingly 
    Write %matplotlib qt for better graph window
'''
fig, ax = plt.subplots()
ax.errorbar(time, mag, yerr=magerr, fmt='ro', linestyle='none', label='data')
ax.set(title='Target 1 Magnitude', xlabel='Time (s)', ylabel='Magnitude')
leg = ax.legend(loc='best')
ax.grid()
plt.show()