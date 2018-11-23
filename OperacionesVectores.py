# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#Programa para las operaciones con vectores
import numpy as np

def sumvec(x,y):
	x1 = np.array[x]
	y1 = np.array[y]
	return x1 + y1
def restavec(x,y):
	x = [x]
	y = [y]
	return x - y
def mulvec(x,y):
	x = []
	y = []
	return x + y
def divvec(x,y):
	x = []
	y = []
	return x / y
def negvec(x,y):
	x = [] * -1
	y = [] * -1
	return x,y
def invec(x,y):
	x = reverse(x)
	y = reverse(y)
	return x,y

'''
#Para leer una matriz
#Pedimos la dimension de la matriz
m = int(raw_input('Dime el numero de filas: '))
n = int(raw_input('Dime el numero de columnas: '))
#Creamos una matriz nula
M = []
for i in range(m):
	M.append([0] * n)

#... y leemos su contenido de teclado
for i in range(m):
	for j in range(n):
		M[i][j] = float(raw_input('Dame el componente (%d,%d): '% (i,j)))

'''