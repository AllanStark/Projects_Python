# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import re
import sys

def carpeta(ruta):###abre  una carpeta 
    archivos=[]
    for x in os.listdir(ruta):#nos dice todos sus elementos
       if os.path.isfile(os.path.join(ruta,x)):#verifica si es archivo y agrega
           archivos.append(x)
       else:
           try:
            os.listdir(os.path.join(ruta,x))#verifica si es carpeta y si se puede ejecutar
            archivos.append(carpeta(os.path.join(ruta,x)))
           except OSError:#pasa si no se puede ejecutar
            pass
            
    return archivos#regresa todos los archivos del directorio
   
def selec_tipo(x,g):#escoge todos los archivos del tipo seleccionado 
    tipo=[]
    for archivo in x:
        if type(archivo)==type([]):
            tipo=tipo+[selec_tipo(archivo,g)]
            
        elif g in archivo:
            tipo=tipo+[archivo]
    
        
    return tipo#regresa todos los archivos del mismo tipo
    
def cambios(x):#cambia espacios por guion bajo y mayusculas por minusculas
    nueva_lista=[]
    
    for i in x:
        if type(i)==type([]):
            nueva_lista.append(cambios(i).encode('ascii', 'ignore'))
        else:
            a=i.split()
            b='_'.join(a)
            nueva_lista.append(b.lower().encode('ascii', 'ignore'))

            #print('el nombre original del archivo es:\n'+i+'   y es cambiado por:     '+b.lower()+'\n')
    return nueva_lista




a=carpeta('C:\\')  #colocar la dirección de la carpeta que desea investigar
b=selec_tipo(a,'.mp3')  #el segundo argumento es reservado para buscar los tipos de archivos deseados
c=cambios(b)

print('los nombres de los archivos originales son\n\n\n\n'+str(b)+'\n\n\n\n\n\n\nfueron cambiados a\n\n\n'+str(c))
#este ultimo print nos arroga todos los archivos estructurados en la carpeta




        
