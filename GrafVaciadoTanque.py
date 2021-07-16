# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:48:36 2021

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
dt = 1

rootg = np.sqrt(2*g)
p1 = -5*(r1**2)
p2 = 2*((R/H)**2)
p3 = H**(5/2)

(((-5*(r1**2)*np.sqrt(2*g)*t)/(2*((R/H)**2)))+H**(5/2))**(2/5)

hArr = []
tArr = []

hN = []

#Gráfica Analítica
while t<= 40:

    h = (((-5*(r1**2)*np.sqrt(2*g)*t)/(2*((R/H)**2)))+H**(5/2))**(2/5)

    print(h)
    print("Han transcurrido", t, "segundos")
    hArr.append(h)
    tArr.append(t)

    t+=1

#Gráfica Numérica    
while t1<=40:
    tmph = h
    h = ((((-1)*(r1**2)*np.sqrt(2*g*tmph))/(((R*tmph)/H)**2))*dt)+tmph
    if t1 == 0:
        h = H
    if h <= 0:
        h=0
    hN.append(h)
    t1+=dt
print(hArr)
print(tArr)
plt.xlabel("Tiempo")
plt.ylabel("Nivel de agua")
plt.plot(tArr, hArr, ".-")
plt.plot(tArr, hN)

    