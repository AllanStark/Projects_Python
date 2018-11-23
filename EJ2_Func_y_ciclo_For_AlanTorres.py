# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
El siguiente programa crea una funcion que utiliza un ciclo for 
"""
def recorrido(x):
	contador = 0 #Definimos un contador que sirve para ir guardando el valor 
	for i in range(x+1): #Se hace el recorrido por el valor de x, el +1 es porque range toma los valores de 0 a x-1 y queremos evaluar todo el valor de x
		contador += i #se va agregando el valor de i 
	return contador

#Ejemplo : 
print recorrido(3) #0 +1 + 2 + 3 = 6