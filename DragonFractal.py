# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from turtle import *
def curva(n):
    """Devuelve una lista de caracteres con los giros
       requeridos para dibujar la curva de dragón de orden
       n. La letra 'I' significa girar a la izquierda, 
       mientras que la letra 'D' significa girar a la 
       derecha.
    """
    if n == 0:
        return []
    else:
        c = curva(n - 1)
        r = c[::-1]
        i = ['I' if g == 'D' else 'D' for g in r]
        return c + ['I'] + i
# for i in range(6):
#     print('orden {0}: {1}'.format(i, ''.join(curva(i))))


def dragon(n, x):
    """Dibuja una curva de dragón de orden n en donde
       cada segmento de la curva es de longitud x.
    """
    fd(x)
    for g in curva(n):
        if g == 'I':
            lt(90)
        else: # g == 'D'
            rt(90)
        fd(x)

hideturtle()       
pensize(1)         
color('SteelBlue')
speed('fastest')   
setheading(180)    
dragon(13, 5)      
done()