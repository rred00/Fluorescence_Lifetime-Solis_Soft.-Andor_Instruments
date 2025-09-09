#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
from scipy.signal import fftconvolve
from scipy.ndimage import gaussian_filter1d
from scipy.optimize import curve_fit
from scipy.ndimage import gaussian_filter

from count import ASCIIDataLoader

f=open('ASCII file location','r')

## convert the ASCII raw in 3d cube 

  # if you save this class in count.py

loader = ASCIIDataLoader("1stimage560nm.asc")
loader.parse_header()
loader.summary()
cube = loader.build_cube()
print("Cube shape:", cube.shape)

## initiating the fitting class
delay=1 # ns
model=Fitting(delay)

############

## preprocessing of the experimental data, smoothing and filtering, one can use other smoothing and filtering processes

ypix_total=len(cube[0,:,0])
xpix_total=len(cube[0,0,:])
for i in range(ypix_total):
    for j in range(xpix_total):
        y=cube[:,i,j]
        cube[:,i,j]= gaussian_filter1d(y, sigma=1.0)
count_cube=cube.copy()
###############

tau_map = np.zeros((count_cube.shape[1], count_cube.shape[2]))

for y in range(count_cube.shape[1]):
    for x in range(count_cube.shape[2]):
        y_data = count_cube[:, y, x]
        A0= np.max(y_data) 
        tau0 = 3 
        B0=np.mean(y_data[-10:])
        center= t[np.argmax(y_data)]
        width=3.5  ### choose wisely 
        p0=[A0,tau0,B0,center,width]
        bound=([0,0.08,0,1,2],[10000,30,5000,15,20])
        z=new_model.fit_pixel(t,y_data,p0,bound)
        tau_map[y, x] = z[1]
#################
## post processing again, smoothing the tau values in the pixel grid
sigma = 1.0  # Adjust this value to control smoothing strength
smoothed_roi = gaussian_filter(tau_map, sigma=sigma)
smoothed_data=  smoothed_roi



################

plt.figure(figsize=(6, 5))
im = plt.imshow(smoothed_data, cmap='jet', origin="lower")  
plt.axis('off')  # Remove x-axis ticks
# plt.set_yticks([]) 
# Colorbar for scale
cbar = plt.colorbar(im)
cbar.set_label("Lifetime (ns)", fontsize=12)

plt.title("Lifetime Map", fontsize=14)
# plt.xlabel("X pixel")
# plt.ylabel("Y pixel")
plt.tight_layout()

#plt.savefig('FLIM1stimage_03',dpi=600) 
plt.show()







