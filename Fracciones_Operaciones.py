# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from fractions import Fraction # La clase fraction utiliza varios metodos para realizar operaciones
#Ejemplo basico del uso de Fraction es: Fraction(1,2) >>> Fraction(1,2)
#Funcion Suma
def sumafrac(a,b,c,d):
	# f1 = Fraction(a,b)
	# f2 = Fraction(c,d)
	# suma = f1 + f2
	# return suma
	return Fraction(a,b) + Fraction(c,d)
#Funcion Resta
def restafrac(a,b,c,d):
	# f1 = Fraction(a,b)
	# f2 = Fraction(c,d)
	# resta = f1 - f2
	# return suma
	return Fraction(a,b) - Fraction(c,d)
#Funcion Multiplicacion
def mulfrac(a,b,c,d):
	# f1 = Fraction(a,b)
	# f2 = Fraction(c,d)
	# multiplicacion = f1 * f2
	# return multiplicacion
	return Fraction(a,b) * Fraction(c,d)
#Funcion Division
def divfrac(a,b,c,d):
	# f1 = Fraction(a,b)
	# f2 = Fraction(c,d)
	# division = f1 / f2
	# return division
	return Fraction(a,b) / Fraction(c,d)
#Funcion inverso
def invfrac(a,b):
	resultado =b,a 
	#resultado = reverse(a,b)
	#texto= str(resultado) #Esta linea de codigo muestra el resultado como un string 'b/a'
	return resultado
#Funcion negativo
def negfrac(a,b):
	negativo = Fraction(-a,b)
	return negativo

#Tarea para el 22 de Septiembre del 2016
#Realizar una funcion que realize la sig operacion
#((fraccion-fraccion)/(fraccion+(fraccion*fraccion)))
def foperaciones(a,b,c,d):
	'''

	Function: foperaciones

	Summary: Utiliza la clase fraction para resolver la operacion ((fraccion-fraccion)/(fraccion+(fraccion*fraccion))) 

	Examples: foperaciones(1,2,3,4)

	Attributes: 

		@param (a):Numerador 1

		@param (b):Denominador 1

		@param (c):Numerador 2

		@param (d):Numerador 2

	Returns: fracccion como, 1,2

	'''

	f1 = Fraction(a,b)
	f2 = Fraction(c,d)
	resultado = ((f1-f2)/(f1+(f1*f2)))
	return resultado 

"""
La clase Fraction puede ser llamada de diferentes formas
Desde un Float
Fraction(2.5) >>> Fraction(5,2)
Desde un Decimal
from decimal import Decimal 
Fraction(Decimal('1.1')) >>> Fraction(11,10)
Tambien se puede iniciar con un String 
Fraction('9/16') >>>Fraction(9,16)
Reduce automaticamente
Fraction(153, 272) >>> Fraction(9,16)
Para la suma 
Fraction(1,2) + Fraction(3,4) >>> Fraction(5,4)
Resta 
Fraction(5, 16) - Fraction(1, 4) >>> Fraction(1, 16)
Multiplicacion
Fraction(1, 16) * Fraction(3, 16) >>> Fraction(3, 256)
Division 
Fraction(3, 16) / Fraction(1, 8) >>> Fraction(3, 2)
"""

# Las sig. lineas son la funcion que diseño Israel sin embargo no funca.
# def sumafrac(xa,xb):

# 	numerador1 = xa[0]*xb[1]
# 	numerador2 = xb[0]*xa[1]
# 	comundenominador = xa[1]*xb[1]

# 	resultado = (numerador1 + numerador2, comundenominador)
# 	return resultado
#Las sig. Lineas muestras la forma de reduccion de Farey
# from fractions import *
# def Farey(a,b):
#     n = a.numerator+b.numerator
#     d = a.denominator+b.denominator
#     return Fraction(n,d)

# a = Fraction(3,4)
# b = Fraction(1,13)
# print(Farey(a,b))
#Las siguientes lineas forman parte de la clase Fraction
#Sacado de la pagina https://howchoo.com/g/nddmztjkmwe/dealing-with-fractions-in-python
#https://hg.python.org/cpython/file/2.7/Lib/fractions.py
#https://pymotw.com/2/fractions/
#https://en.wikibooks.org/wiki/Mathematics_with_Python_and_Ruby/Fractions_in_Python

