# -*- coding: utf-8 -*-
from __future__ import unicode_literals
###########################################################################
###                                                                     ###
### Simulacion de estabilizacion de un pendulo invertido Simple         ###
###                                                                     ###
###########################################################################
#Alan Iván Torres Sánchez
# x1' = x2
# x2' = mgl sin x

#De la Bibloteca numerica se importa seno y coseno
from numpy import sin, cos
#Se importa la Biblioteca numerica como np
import numpy as np
#Se importa  la biblioteca de graficos como plt
import matplotlib.pyplot as plt
#Se importa el modulo de integracion de la biblioteca cientifica
import scipy.integrate as integrate
#Se importa el modulo de animacion
import matplotlib.animation as animation
#Iniciando Caracterisiticas del carrito
#FCart = 2   #Fuerza de empuje sobre el carrito
#mCart = 1.0 #Masa del carrito
#Se declara una funcion pendulo que determina el comportamiento de este
def pendulo():
    # Parametros del sistema
    g = 9.8  # Gravedad
    l = 1.0  # Longitud del péndulo
    m = 1.0  # Masa del pendulo es 1kg
    

    # parámetros de simulación
    dt=0.025             # paso de integración
    tf=10              # Tiempo total de simulación
    t=np.arange(0,tf,dt) # tiempo 


    x10, x20 =  np.pi/2,np.pi/2    # condiciones iniciales para los valores de x en radianes
    x = np.array([x10,x20]) # Estado inicial de los valores de x


    # Las ecs dif del sistema se meten en una funcion
    def sist(x, t):
        xp = np.zeros_like(x) #se declara un arreglo de 0 del tamaño de x
        xp[0] = x[1]
        xp[1] = -m*g*l*sin(x[0]) #se define el comportamiento del movimiento del pendulo
        return xp

    # Simulando (simular es integrar)
    sol = integrate.odeint(sist,x,t)
    return [sol,t]


def coord_cartesianas(sol):
    l=1.0
    x1 = l*sin(sol[:, 0])
    x2 = l*sin(sol[:, 0])
    y1 = l*sin(sol[:, 0])
    return [x1,y1,x2]

def animar(coord):
    x1=coord[0]
    y1=coord[1]
    x2=coord[2]

    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
    ax.grid()

    line, = ax.plot([], [], 'o-', lw=2)# Configuracion de ancho de linea y tipo de muestreo para el pendulo
    time_template = 'Tiempo = %.1fs' #Configuracion del tiempo a mostrar
    time_text = ax.text(0.5,0.9, '', transform=ax.transAxes) #Configuracion de la etiqueta para mostrar tiempo 
    

    def init():             #Se define el contructor para la animacion
        line.set_data([], [])   #Se configuran los arreglos de datos a moestrear
        time_text.set_text('')  #Se inicia con la etiqueta vacia
        return line, time_text  #Se regresa los parametros a animar


    def animate(i):     #Se define la funcion de animación
        dt=0.025        #Se declara el valor del muestreo de la derivada
        x = [x1[i], y1[i]]
        y = [x2[i], 0]
        #x2 = np.zeros_like(i)
        #x = [x1[i],y1[i]]
        #x = [y1[i], x1[i]]  
        #y = [y1[i],x2]
        #y = [0, y1[i]]

        line.set_data(x, y)
        time_text.set_text(time_template % (i*dt))
        return line, time_text

    ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y1)),
                                  interval=25, repeat= True,
                                  blit=True, init_func=init)

    #ani.save('double_pendulum.mp4', fps=15)
    plt.show()


simul=pendulo()
coordenadas=coord_cartesianas(simul[0])
animar(coordenadas)


