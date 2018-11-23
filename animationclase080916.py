# Importando las bibliotecas que se usaran a lo largo del archivo

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.animation as animation

import time



#se crea un arreglo de 0 a 2pi de 1000 elementos

x=np.linspace(0, 2*np.pi,100) #Se usar como eje x 


"""

fig = plt.figure()            # Se crea una figura

ax = fig.add_subplot(111) #agrega ejes coordenados

"""

"""Una animacin consiste en desplegar imagenes una tras otra lo

suficientemente rpido para que el cerebro cree la ilusin de

movimiento. En el codigo que sigue se grafican sucesivamente funciones

seno cada una desplazada con respecto a la otra.



"""

"""

for i in range(0,500):

    y=np.sin(x-i)  # Calcula la funcin a graficar

    ax.clear()     # Borra la imagen anaterior

    plt.hold(True) # Se asgura que la grafica est en la misma figura

    ax.plot(x,y)   # Grafica la nueva funcin

    plt.pause(0.1) # Una pausa antes de graficar la siguiente 


"""


#=================================================

# Cerrar la figura antes de continuar

#=================================================



"""El siguiente codigo hace lo mismo que el anterior pero llamando a

 la funcion animation.FuncAnimation.  Esta funcin recibe como mnimo

 dos argumentos: la figura en la que se va a graficar y la funcin de

 animacin.  La funcin de animacin debe depender de un

 parametro. Este FuncAnimation cambia este parametro automaticamente.



FuncAnimation tiene varias opciones que le dicen que tan rapido hay

que llamar a la funcin de animacin, en cuanto se incrementa el

parametro de la funcin de animacin, etc.



"""



fig = plt.figure()            # Se crea una figura

ax1 = fig.add_subplot(311) #agrega ejes coordenados
ax2= fig.add_subplot(312) #agrega ejes coordenadosax = fig.add_subplot(111) #agrega ejes coordenados
ax3= fig.add_subplot(313) #agrega ejes coordenados

def animate(i):

    y1 = (np.sin(x-i))
    y2 = (np.cos(x-i))

    ax1.clear()

    ax1.plot(x,y1 )
    ax1.plot(x,y2 )

    ax2.clear()

    ax2.plot(x,y1+y2)

    y3=np.fft.fft(y1+y2)

    """   

    def myfft(senal):
    	n2=int(len(senal)/2)
    	f=np.fft.fft(senal)/n2	
    	f=f[range(n2)]
    	refft=abs(f)
    	return refft


    y3=myfft
    """


    ax3.clear()

    ax3.plot(x,y3)




ani = animation.FuncAnimation(fig, animate)

plt.show()

