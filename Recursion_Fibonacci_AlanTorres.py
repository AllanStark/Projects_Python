# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
Programa que define una función recursiva para la serie de Fibonacci
'''
def fibonacci(n):
	'''

	Function: fibonacci

	Summary: Regresa el valor del numero n junto con su serie de fibonacci

	Examples: fibonacci(15)

	Attributes: 

		@param (n):Debe ser un número positivo 

	Returns: serie de Fibonacci

	'''
	if n ==1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fibonacci(n-1) + fibonacci(n-2) #regresamos los dos valores anteriores hasta llegar a las primeras condiciones
#El siguiente ciclo muestra los numeros de fibonacci d

el 1 al 13
for n in range(1,13):
 	print(n,  ":", fibonacci(n))
 	
#El siguiente ciclo regresa el valor de la serie de fibonacci y de sus anteriores sin guardar en memoria, por lo tanto tarda mas en hacer las operaciones
# for n in range(1,101):
# 	print(n, ':', fibonacci(n))
