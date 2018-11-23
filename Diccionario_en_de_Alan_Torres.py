# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
El siguiente programa es un diccionario de aleman a ingles y viceversa
'''



#inglés a danés
en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
#danes a frances
de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}
farben = {"weiss" : "white", "schwarz" : "black", "grau" : "gray", "braun" : "brown", "gelb" : "yellow"}
zahlen = {"null" : "zero", "eins" : "one", "zwei" : "two", "drei" : "three", "vier" : "four"}
en_ger = {} #Declaramos un diccionario vacio que posteriormente se le agregan diccionarios
def EN_DE():
	word = raw_input("Give Me a Word \n")
	#for word in en_de:
	print(en_de.get(word)) #Usamos el parametro get para en caso de no existir la clave no devuelva un error
        #print(en_de.get(word, 'no tengo el valor indicado'))
        
#La siguiente función toma el valor de diferentes diccionarios y los ubica en uno nuevo para luego buscar dentro del nuevo dicc

def EN_GER():
    en_ger.update(farben)
    en_ger.update(zahlen)
    word = raw_input("Give me a word to translate from German\n")
    if en_ger.has_key(word):
        print en_ger.get(word, "Doesn't exist in Dictionary")
    else: print "We havent the definition" 
#    else: 
#        print 'Does not exist,  do you want to add a definition? y/n \n' 
#        x = raw_input()
#        if x == 'y' or 'Y':
#            y = input("Give de word and their equal, example versteh = know \n")
#            en_ger.update(dict(y))
#        else: exit()
#           
    #print en_ger
#Los comentarios anteriores son parte de codigo en progreso para poder añadir claves-valor a un diccionario desde el input

#El Siguiente bloque es una funcion que sirve para agregar items valor-clave a un diccionario
def addvalue(dic,usu,valor):
    if not dic.has_key(usu):
          dic[usu]=valor

#en_ger={}
#addvalue(en_ger,'Banhhoff','Bus Station')
#addvalue(en_ger,'Mutter','Mother')
#print en_ger
#La siguiente funcion toma los valores de diccionarios y cambia de lugar los valores y las claves
#Falta completar la siguiente funcion para cambiar ente valor y clave
#ger_en = {} 
#def GER_EN(x): 
#    for key in x.keys():
#        ger_en[x.keys] = key
#    print ger_en
        #print "%s -> %s"%(key,x[key])
        #print ger_en
        
    


