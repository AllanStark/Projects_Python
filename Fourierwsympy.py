# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 00:16:14 2016

@author: Sorek
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

#Importamos todo el modulo sympy
from sympy import *
#ademas importamos las variables simbolicas 'n' y 't'
from sympy.abc import t, n

ao = integrate(2 / pi, (t, 0, pi / 2))
#integramos la funcion (2/pi) cuya variable es 't'
#y limites de integracion entre 0 y pi/2

print "\n"+"a0 = "
pprint(ao)
#Usamos la funcion pprint para mostrar ao


an = integrate((2 / pi) * cos(2 * n * t), (t, 0, pi / 2))
#integramos la funcion (2/pi)*cos(2nt)
#Su variable es 't' y sus limites de integracion son 0 y pi/2

print "\n"+"an = "
pprint(an)
#Usamos la funcion pprint para mostrar an

bn = together(integrate((2 / pi) * sin(2 * n * t), (t, 0, pi / 2)))
#integramos la funcion (2/pi*cos(2nt)
#Su variable es 't' y sus limites de integracion
#son 0 y pi/2. Ademas usamos la funcion "together"
#para simplificar la expresion

print "\n"+"bn = "
pprint(bn)
#Usamos la funcion pprint para mostrar bn

print "\n"+"f(x) = "

armonicos = 100
serie = (ao/2)
for i in range(1, armonicos + 1):
    serie = serie + (an*cos(2*n*t)).subs(n, i)
for j in range(1, armonicos + 1):
    serie = serie + (bn*sin(2*n*t)).subs(n, j)

pprint(serie)

plotting.plot(serie, ylim=(-0.5, 1.5), xlim=(-0.5,5)) #Usando el modulo para graficas de sympy