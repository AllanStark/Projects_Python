# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Tkinter import *
# from youtube_dl import *
# from YTD import *
import YTD 
 
def Call(): # Definimos la funcion
        lab= Label(root, text = 'Usted presiono\nel boton')
        lab.pack()
        boton['bg'] = 'blue' # Al presionar queda azul
        boton['fg'] = 'white' # Si pasamos el Mouse queda blanco
        YTD.realmain() and 'https://www.youtube.com/watch?v=dbC2UjM6AKs'
 
root = Tk() # Ventana de fondo
root.geometry('100x110+350+70') # Geometría de la ventana
boton = Button(root, text = 'Presionar', command = Call)
boton.pack()
 
root.mainloop()