# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 17:51:04 2016
Programa que muestra una grafica de multiples subplots
@author: Sorek
"""
#Importamos bibliotecas importantes y necesarias para el funcionamiento
import numpy as np #Biblioteca numerica de python
import matplotlib.pyplot as plt #Biblioteca de graficos de python

#Definimos el rango de muestreo para el eje x
t = np.arange(-2.0, 2.0, 0.01)

#Se genera la funcion seno de una variable x multiplocado por pi
def seno(x):
        f1 = np.sin(np.pi * x)
        return f1
#Se genera una funcion coseno de una variable x multiplicada por  pi
def coseno(x):
        f2 = np.cos(np.pi * x)
        return f2       
 
 
# Se crea una figura con fondo negro y un tamaño de 8x8 px
fig = plt.figure(figsize=(8, 8), facecolor='black')

#Definiendo los subplots con sus caracteristicas y partes a graficar
#Se define el subplot para la columna 1 y fila 1 de 3 subplots
plt.subplot(311)
#Titulo de el subplot
plt.title('sin y cos', color='springgreen' )
#Parametros a evaluar
plt.plot(t, seno(t), 'springgreen')
plt.plot(t, coseno(t), 'deepskyblue')

plt.subplot(312)
plt.title('seno + coseno', color='deeppink')
#Se grafica la suma de la funcion seno y coseno
plt.plot(t, seno(t)+coseno(t), 'deeppink')

plt.subplot(313)
#plt.plot(t, seno(t))
plt.title('cos', color='salmon')
#Se grafica la funcion coseno
plt.plot(t, coseno(t), 'salmon')
#Se utiliza show para mostrar la grafica
plt.show()



