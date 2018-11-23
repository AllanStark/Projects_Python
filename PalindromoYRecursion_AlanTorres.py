# -*- coding: utf-8 -*-
from __future__ import unicode_literals

'''
El siguiente programa realiza la tarea de verificar cadenas de texto para saber si es un palindromo.
Se utilizan metodos como recursión, expresiones regulares entre otros.
'''
import re #Biblioteca Para las expresiones regulares
import unicodedata # Biblioteca para poder cambiar tipos de formato.

def normaliza(s): #Declaramos una función que usando expresiones regulares busque las letras de la a-z y que elimine las demas
	lista=[] #se declara una lista vacia donde se cargará la cadena despúes del filtro
	for c in s: #un arreglo que busca en cada cáracter(c) de la cadena(s)
		if re.search(r'[A-Za-z]',c):#condición que descarta los caracteres ajenos a la expresión regular
			lista.append(c.encode('ascii'))#Agregamos los valores encontrados a la lista y usamos un encoder para eliminar el error que añade una u
	lista=''.join(lista) #unimos todos los cáracteres como una cadena
	return lista.lower()#regresamos la lista filtrada pasandola a minusculas

def elimina_tildes(s): #Declaramos una función para buscar los caracteres que tengan similares o encode(ej: Ñ=n,ä=a) y remplazarlos  
   new=''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))#Utilizamos el unicode data para filtrar los caracteres
   return normaliza(new) #Regresamos la cadena filtrada por esta y la otra función

# print(elimina_tildes('la MmaAScarená  ï■{|¤¢æ¶ƒïüÇäÑ'))# Linea para probar el filtrado de las funciones


# Se declara una función para descubrir si una cadena es palindromo
def Palindromo(string):
# 	#se define la condicion inicial
	string = elimina_tildes(string)#declaramos la cadena filtrada
	if len(string) <= 1: #Condición para ser una cadena
		return True
	else:#Sigue la parte recursiva  
		return string[0] == string[-1] and Palindromo(string[1:-1]) #Checamos la primera y ultima letra en cada iteracion

print(Palindromo('Ligar es ser Ágil')) #Probando el programa.







