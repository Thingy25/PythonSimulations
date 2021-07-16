# -*- coding: utf-8 -*-
"""
Created on Sun May  9 18:49:40 2021

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt

R = 5
g = 980
H = 18
r1 = 0.16547
t = 0
t1 = 0
dt = 1 #1/30 Se le puede dar este valor a dt para que t se asemeje al tiempo real.
temph = 18
h = H

plt.plot([-r1, -R, R, r1, -r1], [0, H, H, 0, 0])
line, = plt.plot([-R, R], [h, h])

#Animación con solución analítica

#while h>=0:
     #h = (((-5*(r1**2)*np.sqrt(2*g)*t)/(2*((R/H)**2)))+H**(5/2))**(2/5)
     #rr = (h*R)/H
     #line.set_ydata(h)
     #line.set_xdata([-rr, rr])
     #plt.title("Tiempo (segundos):"+ str(t))
     #t+=1
     #print(h)
     
     
     #plt.pause(1/60)
  
#Animación con solución númerica   
  
while h>0:
    tmph = h
    h = ((((-1)*(r1**2)*np.sqrt(2*g*tmph))/(((R*tmph)/H)**2))*dt)+tmph
    rr = (h*R)/H
    line.set_ydata(h)
    line.set_xdata([-rr, rr])
    plt.title("Tiempo (segundos):"+ str(t))
    if t == 0:
        h = H
    if h <= 0:
        h=0
    t+=dt 
   
    plt.pause(1/30)