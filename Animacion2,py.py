# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 23:21:19 2016

@author: Sorek
"""

"""
PROGRAMA QUE DEFINE 3 GRAFICAS ANIMADAS 
EN LA PRIMERA SENO Y COSENO DE UN VALOR
EN LA SEGUNDA LA SUMA DE SENO  MaS COSENO
EN LA TERCERA LA TRANSFORMADA DE FOURIER

"""
#importamos la biblioyyrvs numerica como np
import numpy as np
import matplotlib.pyplot as plt                #importamos la libreria matplotlib como plt
import matplotlib.animation as animation       #importamos la biblioteca animation para las animaciones y la llamamos animation
from scipy.fftpack import fft
#Creamos una figura que contiene subplots
fig, ax = plt.subplots() 
ax1 = fig.add_subplot(311)      #Agregamos un subplot de 3 espacios en 1 columna en la posicion 1
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

#x = np.arange(0, 2*np.pi, 0.01)
freq = np.arange(0, 200, 0.1)
x = np.arange(0, 2*np.pi, 0.01)
y = np.arange(0, 2*np.pi, 0.01)
sumasc = np.sin(x) + np.cos(x)
       
fft_out = fft(sumasc)     
 

line1, = ax1.plot(x, np.sin(x))
line2, = ax1.plot(x, np.cos(x))
line3, = ax2.plot(x, sumasc)
#line4, = ax3.plot(freq, fft_out)




def animate(i):
    line1.set_ydata(x + i/100)  # update the data
    line2.set_ydata(x + i/100)  # update the data
    line3.set_ydata(x + i/100)  # update the data
    #line3.set_ydata(np.cos(x + i/10.0))
    #line4.set_xdata(freq)  # update the data
    return line1, line2, line3,# line4


# Init only required for blitting to give a clean slate.
def init():
    line1.set_ydata(np.ma.array(x, mask=True))
    #line4.set_xdata(np.ma.array(y, mask=True))
    return line1,# line4,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
                              interval=25, blit=True)

plt.show()
#fig.savefig("PUTO.jpeg")