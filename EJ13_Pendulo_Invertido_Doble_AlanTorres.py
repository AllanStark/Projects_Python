# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Double pendulum formula translated from the C code at
# http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c
###########################################################################
###																		###
### Programa que simula el movimiento de dos pendulos invertidos para  	###
###	Estabilizar en linea vertical uno de estos							###
###########################################################################
#Alan Iván Torres Sánchez
#Se importan los valores de seno y coseno de la biblioteca numerica
from numpy import sin, cos
#Se importa la biblioteca numerica como np
import numpy as np
#Se importa la biblioteca para graficos como plt
import matplotlib.pyplot as plt
#Se importa el modulo integracion de la biblioteca cientifica
import scipy.integrate as integrate
#Se importa el modulo de animacion de la biblioteca de graficos
import matplotlib.animation as animation

#Se establecen los valores que son constantes
G = 9.8  # Gravedad en m/s**2
L1 = 1.0  # longitud del pendulo 1 en m
L2 = 0.2  # longitud del pendulo 2 en m
M1 = 1.0  # masa del pendulo 1 en kg
M2 = 100.0  #masa del pendulo 2 en kg

#Se define una funcion que evalua los diferentes valores de derivacion
def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    del_ = state[3] - state[1]
    den1 = (M1 + M2)*L1 - M2*L1*cos(del_)*cos(del_)
    dydx[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_) +
               M2*G*sin(state[2])*cos(del_) +
               M2*L2*state[1]*state[1]*sin(del_) -
               (M1 + M2)*G*sin(state[1]))/den1

    dydx[2] = state[3]

    den2 = (L2/L1)*den1
    dydx[3] = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_) +
               (M1 + M2)*G*sin(state[0])*cos(del_) -
               (M1 + M2)*L1*state[1]*state[1]*sin(del_) -
               (M1 + M2)*G*sin(state[2]))/den2

    return dydx

# se crea un arreglo de 0 a 100 muestras con valores de 0.05 por cada cambio
dt = 0.05
t = np.arange(0.0, 30, dt)#Se determina el tiempo de muestreo en 30

# th1 y th2 son los angulos iniciales en grados
# w10 y w20 son las velocidades angulares iniciales en grados por segundo
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# Estado inicial
state = np.radians([th1, w1, th2, w2]) #Se convierten los valores a radianes

# se integra nuestra ODE utilizando el modulo scipy.integrate
y = integrate.odeint(derivs, state, t)

x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1

#Se crea una figura para graficar los valores
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2)) #Se establece el subplot con sus caracteristicas y limites
#Se activa el cuadriculado
ax.grid()
#Se establece la parte a graficar con sus caracteristicas de tipo de linea y ancho de esta
line, = ax.plot([], [], 'o-', lw=2)
#Se establece una etiqueta para mostrar los cambios de la animacion
time_template = 'Tiempo = %.1fs'
#Se establecen los valores de colocacion para la etiqueta
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

#Se define el constructor de los valores que se grafican y usan para la animacion
def init():
    line.set_data([], [])#Inicia los valores de la grafica en blanco
    time_text.set_text('')#Inicia los valores de la etiqueta como vacia
    return line, time_text

#Funcion de animacion
def animate(i):
    thisx = [0, x1[i], x2[i]]#Establece todos los valores de x que se van a ir cambiando
    thisy = [0, y1[i], y2[i]]#Establece los valores de las y que se van a animar
#Los valores de thisx y thisy se ponen como valores del grafico
    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt)) #se establece el como cambiar la etiqueta para mostrar el tiempo
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
                              interval=25, blit=True, init_func=init)

#ani.save('double_pendulum.mp4', fps=15) #Para guardar el video se necesita el modulo ffmpeg
plt.show() #Muestra la animacion
