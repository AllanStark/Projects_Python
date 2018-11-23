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
# VelPendulo = rad/seg
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

#Se declara una funcion pendulo que determina el comportamiento de este
def pendulo():
    # Parametros del sistema
    g = 9.8  # Gravedad
    l = 1.0  # Longitud del péndulo
    m = 1.0  # Masa del pendulo es 1kg
    #Iniciando Caracterisiticas del carrito
    M = 1.0  # masa del carrito   
    u = 0.5  #Fuerza sobre el carrito
    # parámetros de simulación
    dt=0.025             # paso de integración
    tf=10              # Tiempo total de simulación
    t=np.arange(0,tf,dt) # tiempo 

    x10, x20 = (np.pi),np.pi  # condiciones iniciales para los valores de x donde x10 = angulo y x20 = 2
    x11, x21 = 0, u
    x = np.array([x10,x20,x11,x21]) # Estado inicial de los valores de x
    #np.radians(x)


    # Las ecs dif del sistema se meten en una funcion
    def sist(x, t):
        xp = np.zeros_like(x) #xp contiene la cantidad de x en 0 es decir ([0,0])
        xp[0] = x[0]
        xp[2] = x[2] # - m*g*sin(np.pi)
        xp[1] = (u+m*l*sin(x[0])*(xp[2])**2)# - (m*g*cos(x[0])*sin(x[0]))) / (M+m-m*(cos(x[0])**2)) #se define el comportamiento del movimiento del pendulo
        xp[3] = (u*cos(x[0])#-(m+M)*g*sin(x[0])+m*l*(cos(x[0])*sin(x[0]))*xp[1]) / (m*l*cos(x[0])**2-(M+m)*l)
        return xp 

    # Simulando (simular es integrar)
    sol = integrate.odeint(sist,x,t)
    print(sol)
    exit()
    return [sol,t]


def coord_cartesianas(sol):
    l=1
    g= 9.8
    r= np.radians(np.pi/2)
    m = 1.0
    M = 1.0
    f = 1.0

    y1 = -1*m*cos(sol[:,0])
    x2 = (l*m*sin(sol[:,0]))
    x1 = l*sin(sol[:,0])
    y2 = 0   
    return [x1,y1,x2,y2]

def animar(coord):#Funcion que determina los parametros y todo lo que se grafica y anima
    x1=coord[0]
    y1=coord[1]
    x2=coord[2]
    y2=coord[3]

    fig = plt.figure()# Se crea una figura
    fig.canvas.set_window_title('Péndulo Invertido') #Nombre de la ventana 
    plt.title('Alan Torres')
    fig.patch.set_facecolor('#3CB371') #Color del fondo
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2),axisbg='#CCFFE5')#Configuracion del subplot, color y limites
    ax.grid(color='springgreen', linewidth=2, linestyle='-')#Activacion de la rejilla y color
    

    line, = ax.plot([], [], 'o-', lw=3)# Configuracion de ancho de linea y tipo de muestreo para el pendulo
    line1, = ax.plot([], [], 'o:', lw=3)#Figura de la fuerza ejercida sobre el carrito
    time_template = 'Tiempo = %.1f seg' #Configuracion del tiempo a mostrar
    time_text = ax.text(0.5,0.9, '', transform=ax.transAxes) #Configuracion de la etiqueta para mostrar tiempo
    
    time_template2 = 'Tiem = %.1f seg' #Configuracion del tiempo a mostrar
    time_text2 = ax.text(0.6,1.9, '', transform=ax.transAxes) #Configuracion de la etiqueta para mostrar tiempo  

    ax.text(0.95, 0.01, 'Péndulo Invertido',  #Estas lineas ponen una etiqueta en la figura
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='red', fontsize=15)
    
    def init():             #Se define el contructor para la animacion
        line.set_data([], [])   #Se configuran los arreglos de datos a muestrear
        line1.set_data([], [])

        time_text.set_text('')  #Se inicia con la etiqueta vacia
        return line, line1, time_text  #Se regresa los parametros a animar


    def animate(i):     #Se define la funcion de animación
        dt=0.025        #Se declara el valor del muestreo de la derivada
        #x = [0, x2[i]]
        #x3 = [y1[i], 0]
        #y = [0, [i]]
        #y2 = [0,0]
        x = [x1[i],y1[i]]
        y = [x2[i],y2[i]]

        line.set_data(x, y)
        line1.set_data(x3,0)
        time_text.set_text(time_template % (i*dt))
        #return line,line1, time_text
        return line, time_text
    ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y1)),
                                  interval=25, repeat= True,
                                  blit=True, init_func=init)

    #ani.save('double_pendulum.mp4', fps=15)
    plt.show()

simul=pendulo()
coordenadas=coord_cartesianas(simul[0])
animar(coordenadas)


