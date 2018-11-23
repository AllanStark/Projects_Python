# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#importar la biblioteca turtle
import turtle
#De la biblioteca Turtle importar todos los metodos 
from turtle import *
#Numero phi que es la relacion que existe entre los números de Fibonacci
fi = 1.618033988749895

def espiral(n):
	'''
	Function: espiral
	Summary: Dibuja una espiral del tamaño n
	Examples: espiral(10)
	Attributes: 
		@param (n):es el valor que va cambiando para el tamaño de la espiral
	Returns: El dibujo de la espiral
	'''
	radio = 10

	for i in range(n): #Dibujar un circulo n veces
		circle(radio,90) #Se dibuja un circulo con cierto radio y valor del arco a dibujar

		radio *=fi #Se incrementa el valor del radio por la razón aurea.

hideturtle() #Oculta la figura de la tortuga
setheading(270) #Pone a la tortuga mirando a 270 grados
espiral(8)#Repite el proceso 8 veces
done()#Termina el proceso pero mantiene la ventana abierta.
