# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#Today we're gonna see everything about list comprehension
#Listas
nums = [1,3,6,3]

suma = nums + nums
agrega = nums + 2*[3,5,2]

pares = [[2,3],[10,30]]

#Ejecutar
pares[1]
pares[1][1]
pares[0] = pares[1]

def contar(s, valor):
	'''

	Function: contar

	Summary: cuenta las ocurrencias del numero valor en la lista s.

	Examples: InsertHere

	Attributes: 

		@param (s):InsertHere

		@param (valor):InsertHere

	Returns: InsertHere

	'''

	total = 0
	for elem in s:
		if elem == valor:
			total += 1
	return total

lista = [1,2,3,4,3,4,4,5,5,6,3,1,3,3,3,3]
contar(lista, 4)
print contar(lista, 4)

#Lista del elemento 3 al 7
lista[3:7]
#Lista del primer elemento al quinto
lista[:5]
#Lista del sexto elemento en adelante
lista[6:]
#Para contar de derecha a izquierda los elementos
#lista[-n] #Donde n es el elemento que se cuenta de derecha a izquierda
#Para devolver todos los elementos de derecha a izquierda
lista[::-1]
#Declarar una lista vacia
lvacia = []
#Lista mixta
lmixta = [42,"What's the question?", 3.1415]
lcadenas = ["Stuttgart", "Freiburg", "Munich", "Nurnberg"]

#Las cadenas son listas
str = "Python me la pela"
len(str)
str2 = "Python" + "Me" + "La" + "Pela"

#Tuplas . Las tuplas no se pueden modificar
# tupla = (2,3) + (5,6)

# tupla = 4*tupla

# tupla.append(75)

# tupla = tupla + (75,)

#Sets
x = set([1,2,3,4,22,4,4,32,2,2,2,43,3,2,2,4,4])
###x >>>>  {32,1,2,3,4,43,22}
y = {1,2,3,4,22,4,4,32,2,2,43,3,2,2,4,4} # Si solo lo ponemos entre llaves se crea un conjunto
#x == y

##Diccionarios 
city = {"New York City":8175133, "Los Angeles":3792621, "Washington":632323}

city["New York City"] #Muestra la clave asignada a su valor
###>>>8175133
city["Halifax"] = 390096 #Sirve para agregar una clave- valor  al diccionario

#Tarea
##Construir un diccionario de ingles a frances y otro de frances a ingles
##Empezar con un diccionario vacio e ir agregando elementos
# en_fr={}

# Hacer una funcion que reciba una cadena y genere la frecuencia morse en ella
# Buscar libro (The) Code

####
#########
###########
#xpar = {i for i in x if i%2==0} ### Operacion modulo 2 que son numeros pares
#ximpar = {i for i in x if i%2==1}#Se crea un conjunto que toma los elementos del conjunto x para numeros impares
#xparlista = [i for i in x if i%2 == 0]
#x = [x**2 for x in range(20)]

from math import sqrt
n = 100
sqrt_n = int(sqrt(n))
no_primos = [i for i in range(2, sqrt_n) for j in range(i*2, n ,i)]
no_primos

