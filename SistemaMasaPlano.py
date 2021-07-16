# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import math
from tkinter import* 


V = 0 
x = 0
y = 15
m = 0 
Fr = 0 
Fa = 0 
An = 0 
g = 9.80 
dt = 0.1
t = 0

dataList = []

window=Tk()

window.title("Inserte los datos aquí")
window.config(bg="blue")

Box=Frame(window,width=1500,height=1500)
Box.pack()

VFrame=Entry(Box)
VFrame.grid(row=0,column=1)
VName=Label(Box,text="Velocidad inicial: ")
VName.grid(row=0,column=0)

mFrame=Entry(Box)
mFrame.grid(row=1,column=1)
mName=Label(Box,text="Masa: ")
mName.grid(row=1,column=0)

FrFrame=Entry(Box)
FrFrame.grid(row=2,column=1)
FrName=Label(Box,text="Fricción masa/plano: ")
FrName.grid(row=2,column=0)

FaFrame=Entry(Box)
FaFrame.grid(row=3,column=1)
FaName=Label(Box,text="Fricción del aire: ")
FaName.grid(row=3,column=0)

AFrame=Entry(Box)
AFrame.grid(row=4,column=1)
AName=Label(Box,text="Angulo de inclinación: ")
AName.grid(row=4,column=0)

lFrame=Entry(Box)
lFrame.grid(row=5,column=1)
nombrel=Label(Box,text="Distancia en x en el plano: ")
nombrel.grid(row=5,column=0)

AFrame=Entry(Box)
AFrame.grid(row=6,column=1)
AName=Label(Box,text="Altura del plano: ")
AName.grid(row=6,column=0)

def Btn():
    V=VFrame.get()
    m=mFrame.get()
    Fr=FrFrame.get()
    Fa=FaFrame.get()
    An=AFrame.get()
    d=lFrame.get()
    A=AFrame.get()
    
    dataList.append(V)
    dataList.append(m)
    dataList.append(Fr)
    dataList.append(Fa)
    dataList.append(An)
    dataList.append(d) 
    dataList.append(A)

    window.destroy()

    pass

boton = Button(window, text = "Empezar", command = Btn)
boton.pack()


window.mainloop()


V= float(dataList[0])
m= float(dataList[1])
Fr= float(dataList[2])
Fa= float(dataList[3])
An= float(dataList[4]) 
d= float(dataList[5])
A= float(dataList[6]) 

An=An*math.pi/180     


plt.plot([d,0,0,d],[0,A,A,0],'k')
plt.axis([0, d,0, A])
mass,=plt.plot(0,A,'sc')


while y>0:
    V = ((g*math.sin(An))-((Fr+Fa))/m)*dt + V
    x = V*dt + x
    y = (A*d-A*x)/d
    mass.set_ydata(y)
    mass.set_xdata(x)

    plt.pause(1/30)
    t = t+dt
    print(x)
    print(y)  