# -*- coding: utf-8 -*-
from __future__ import unicode_literals

######################################################################
# 			Programa que gráfica una espiral por medio de turtle   ###
#		Torres Sánchez Alan Iván								   ###
######################################################################
#Espiral de Arquimedes
#Espiral aurea
#Biblioteca de graficos por instrucciones, pertenece a tkinter
import turtle
#Biblioteca para los aleatorios
import random
colores = ['red','blue','yellow','purple']
#Se asigna a una variable el objeto Turtle, es decir creamos nuestra tortuga
Donnie = turtle.Turtle() #Donnie es la mejor tortuga ninja
Donnie.color('purple','red')#Colores de la tortuga, color de linea y de figura
Donnie.shape('turtle') #Le damos la forma de tortuga
Donnie.pensize(3) #Ancho de la linea que deja Donnie
#Donnie.setx(-300)#Inicializa la posicion en x
Donnie.speed(0)#Velocidad de Donnie


#Se crea la ventana donde se va a mover la tortuga
Ventana = turtle.Screen()
Ventana.bgcolor("lightgreen")      # Color de fondo
Ventana.title("Espiral")      # Nombre de la ventana

#Se define la funcion recursiva que recibe los parametros Donnie= Objeto tortuga , linelen= largo de la linea a graficar y parte recursiva de la fun.
def drawSpiral(Donnie, lineLen):
#Condicion de uso. Si el parametro de ancho de linea es mayor a 0 ejecuta lo siguiente
    if lineLen > 0:
        Donnie.forward(1.1 + 1 ) #Dibuja una linea hacia adelante del tamaño del largo del parametro. Parte recursiva que va a ir cambiando en cada ciclo,
        Donnie.right(0.59)#Gira hacia la derecha los grados que recibe
        Donnie.radians()#Convierte a radianes los grados
        drawSpiral(Donnie,lineLen-0.9)#Parte recursiva que se vuelve a evaluar


    else:
		Donnie.color(random.choice(colores),random.choice(colores))	#Elegimos un valor aleatorio para el color de Donnie
		Donnie.backward(lineLen/23) #Dibuja una linea hacia atras del tamaño del largo del parametro. Parte recursiva que va a ir cambiando en cada ciclo
		Donnie.left(0.59)#Gira hacia la izquierda con el valor que lleva dentro
		Donnie.radians()
		drawSpiral(Donnie,lineLen-8)

drawSpiral(Donnie,100)
Ventana.exitonclick()


###################################################################################
'''
#Las siguientes lineas muestran el codigo que se utilizaria en un ciclo for
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()                # This is new
size = 20
for i in range(30):
   tess.stamp()             # Leave an impression on the canvas
   size = size + 3          # Increase the size on every iteration
   tess.forward(size)       # Move tess along
   tess.right(24)           #  ...  and turn her

wn.mainloop()
'''

