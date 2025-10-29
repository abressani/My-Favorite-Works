#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:44:50 2024

@author: alessandro
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

f = open('target5mags','r')

# Creating arrays of data
mag = np.array([])
magerr = np.array([])
x = np.array([])
tvar = 0
for line in f:
    s = line.split()
    mag = np.append(mag,float(s[1]))
    magerr = np.append(magerr,float(s[2]))
    tvar += 25
    x = np.append(x, tvar)
f.close()


f = open('target4mags','r')

# Creating arrays of data
mag4 = np.array([])
mag4err = np.array([])
time4 = np.array([])
t4var = 0
for line in f:
    s = line.split()
    mag4 = np.append(mag4,float(s[1]))
    mag4err = np.append(mag4err,float(s[2]))
    t4var += 25
    time4 = np.append(time4, t4var)
f.close()

# Find offset values to reduce fluctuations in individual data
y = mag - mag4
flux_err = (magerr + mag4err)/2
    
def segments_fit(X, Y, count, xanchors=slice(None), yanchors=slice(None)):
    xmin = X.min()
    xmax = X.max()
    seg = np.full(count - 1, (xmax - xmin) / count)

    px_init = np.r_[np.r_[xmin, seg].cumsum(), xmax]
    py_init = np.array([Y[np.abs(X - x) < (xmax - xmin) * 0.01].mean() for x in px_init])

    def func(p):
        seg = p[:count - 1]
        py = p[count - 1:]
        px = np.r_[np.r_[xmin, seg].cumsum(), xmax]
        py = py[yanchors]
        px = px[xanchors]
        print('px anchors:',px[xanchors])
        print('py anchors:',py[yanchors] )
        return px, py

    def err(p):
        px, py = func(p)
        Y2 = np.interp(X, px, py)
        return np.mean((Y - Y2)**2)
    
    r = optimize.minimize(err, x0=np.r_[seg, py_init], method='Nelder-Mead')
    return func(r.x)

'''
# apply the segment fit
fx, fy = segments_fit(x, y, 5)
#plt.plot(fx, fy, 'o-')
plt.plot(x, y, '.k')
#plt.errorbar(x, y, yerr=flux_err, ms=10, fmt='black', ecolor = 'black',linestyle='none', label='data')
# apply the segment fit with some consecutive points having the 
# same anchor
fx, fy = segments_fit(x, y, 5, yanchors=[1,1,2,2,3,3])
plt.plot(fx, fy, 'o--r')
plt.grid()

'''

fig, ax = plt.subplots()
# Data
ax.errorbar(x, y, yerr=flux_err, linestyle='none', elinewidth = 1.5, label='data')

# Fit
fx, fy = segments_fit(x, y, 5, yanchors=[1,1,2,2,3,3])
ax.plot(fx,fy,'o--r', label='Fit')

# Shading
ax.axvspan(5442.65141893, 11246.60256336, color='gray', alpha=0.5, label = 'transit')

ax.set(title='Relative Flux of Target Star', xlabel='Time (s)', ylabel='Relative Flux')
leg = ax.legend(loc='upper left')
ax.grid()
plt.show()



