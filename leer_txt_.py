# -*- coding: utf-8 -*-
"""
@author: Alan
"""
 #Se declaran las bibliotecas pertinentes para la programacion
import numpy as np #biblioteca para la soluciones numericas
from numpy.linalg import inv #biblioteca para sacar la inversa de una  matriz
from matplotlib import pyplot as plt #Biblioteca para sacar 
import math #biblioteca para uso de senos y cosenos

#directorio
entrada_vel = open("fuerza_C.txt", 'r')
entrada_desp = open("desp_C.txt", 'r')
entrada_fuerza = open("fuerza_C.txt", 'r')
entrada_pot = open("energia_pot.txt", 'r')
entrada_cin = open("energia_cin.txt", 'r')
entrada_tiempo = open("tiempo_exec.txt", 'r')

#Lectura del archivo
c1 = entrada_vel.read()
c2 = entrada_desp.read()
c3 = entrada_fuerza.read()
c4 = entrada_pot.read()
c5 = entrada_cin.read()
c6 = entrada_tiempo.read()
#division de los datos
d1 = c1.split()
d2 = c2.split()
d3 = c3.split()
d4 = c4.split()
d5 = c5.split()
d6 = c6.split()

#lista vacia para guardar los datos
datos1 = []
datos2 = []
datos3 = []
datos4 = []
datos5 = []
datos6 = []
delta_t = 0.001 # Tiempo de paso entre iteracion
T= len(datos1) # tamano del vector tiempo
time = np.arange(0.0, T, delta_t) # se define un arreglo para el vector tiempo y el paso entre mediciones

#transforma los datos en float y se puedan trabajar
for i in d1:
	datos1.append(float(i))
	datos2.append(float(i))
	datos3.append(float(i))
	datos4.append(float(i))
	datos5.append(float(i))


t = [i for i in time] # Se evalua la variable i para cada valor de tiempo
#datos = datos[:]

plt.plot(datos1) #Graficamos los valores del desplazamiento en cada unidad de tiempo
#plt.plot(datos2) #Graficamos los valores del desplazamiento en cada unidad de tiempo
#plt.plot(datos3) #Graficamos los valores del desplazamiento en cada unidad de tiempo
#plt.plot(datos4) #Graficamos los valores del desplazamiento en cada unidad de tiempo
#plt.plot(datos5) #Graficamos los valores del desplazamiento en cada unidad de tiempo
#plt.plot(t, force) # Graficamos los valores de la fuerza aplicada en cada momento de tiempo
#plt.plot(t, Kin) # Graficamos los valores de la energia cinetica para cada momento de tiempo
#plt.plot(t, Pot) #graficamos los valores de la energia potencial para cada momento de tiempo
plt.grid(True) # graficamos las celdas
plt.legend(['Magnitudes'], loc= 'upper right') # aplicamos las etiquetas de los valores
plt.title('Movimiento armonico amortiguado ') # Agregamos titulo a la grafica
plt.xlabel('tiempo en ms')
plt.show()
#print datos1,datos2, datos3, datos4, datos5 

