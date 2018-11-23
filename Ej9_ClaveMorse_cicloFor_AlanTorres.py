# -*- coding: utf-8 -*-
from __future__ import unicode_literals


#x = input("Palabra a convertir en morse")
#Programa para mostrar la clave morse de una palabra
#import sys

morse = {
"A" : ".-", 
"B" : "-...", 
"C" : "-.-.", 
"D" : "-..", 
"E" : ".", 
"F" : "..-.", 
"G" : "--.", 
"H" : "....", 
"I" : "..", 
"J" : ".---", 
"K" : "-.-", 
"L" : ".-..", 
"M" : "--", 
"N" : "-.", 
"O" : "---", 
"P" : ".--.", 
"Q" : "--.-", 
"R" : ".-.", 
"S" : "...", 
"T" : "-", 
"U" : "..-", 
"V" : "...-", 
"W" : ".--", 
"X" : "-..-", 
"Y" : "-.--", 
"Z" : "--..", 
"0" : "-----", 
"1" : ".----", 
"2" : "..---", 
"3" : "...--", 
"4" : "....-", 
"5" : ".....", 
"6" : "-....", 
"7" : "--...", 
"8" : "---..", 
"9" : "----.", 
"." : ".-.-.-", 
"," : "--..--",
" " : "_"
}
def convierte_ascii(c):
   """Convierte c a una cadena que únicamente contiene
   caracteres ASCII.
   
   Convierte caracteres con acento, diéresis o tilde al
   carácter simple correspondiente. Elimina cualquier otro
   carácter que no sea ASCII.
   """
   return (unicodedata.normalize('NFD', c.decode('utf8'))
           .encode('ascii', 'ignore'))
def convierte_morse(mensaje):
   """Convierte mensaje a una cadena de símbolos morse.
   
   Las letras se delimitan entre sí con un espacio. Las
   palabras se delimitan con cuatro espacios.
   """
   resultado = []
   for c in convierte_ascii(mensaje).upper():
       if c in codigo:
           resultado.append(codigo[c])
       elif c == ' ':
           resultado.append('  ')
   return ' '.join(resultado) ##El parametro join concatena las diversas cadenas

# def claveMorse():
# 	palabra = raw_input("Dame una palabra o letra""\n").upper()
# 	for i in palabra:
#              #print ' '.join(morse[i])
# 		print i,"en morse", morse[i]



