# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from math import sqrt
# n = 100
# sqrt_n = int(sqrt(n))
# no_primos = [j for i in range(2, sqrt_n) for j in range(i*2, n ,i)]
# print(no_primos)

#Generando conjunto de no_primos
n = 100
sqrt_n = int(sqrt(n))
no_primes = {j for i in range(2,sqrt_n) for j in range(i*2, n, i)}
#print(no_primes)
primes = {i for i in range(n) if i not in no_primes}
#print(primes)

#Tarea
##### Cambiar el ciclo for de cualquiera de los problemas que hemos hecho y poner el arreglo anterior para generar listas o conjuntos
