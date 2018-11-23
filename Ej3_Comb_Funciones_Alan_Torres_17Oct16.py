# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
El siguiente programa es el ejercicio que quedo pendiente el día martes 17 de octubre del 2016
Determina la combinacion de dos funciones f1 y f2 en las condiciones pedidas por f3
'''
t = 5 
def f1(a=1, b=0):
	"""

	Function: f1

	Summary: Funcion que determina los valores de una recta con pendiente en a y origen b 

	Examples: InsertHere

	Attributes: 

		@param (a) default=1: valor de la pendiente 

		@param (b) default=0: valor del origen

	Returns: InsertHere

	"""
	def f(t):
		return a*t+b
	return f

def f2(a=2, b=1):
	def f(t):
		return a*t+b
	return f

def f3(f1=f1(),f2=f2(),ti):

    if f1 <= ti:
		return f1(t)
    else: return f2(t)
		#return f2(t)
  
f1 = f1()
f2 = f2()