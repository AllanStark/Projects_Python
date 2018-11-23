# -*- coding: cp1252 -*-g
from __future__ import unicode_literals
#convierte texto ingresado en pantalla a codico morse
#Creando una funcion que contiene if como forma de ordenar las palabras
def morse(caracter):
    if caracter == 'a' or caracter == 'A':
        codigo = '.-'
    if caracter == 'b' or caracter == 'B':
        codigo = '-...'
    if caracter == 'c' or caracter == 'C':
        codigo = '-.-.'
    if caracter == 'd' or caracter == 'D':
        codigo = '-..'
    if caracter == 'e' or caracter == 'E':
        codigo = '.'
    if caracter == 'f' or caracter == 'F':
        codigo = '..-.'
    if caracter == 'g' or caracter == 'G':
        codigo = '--.'
    if caracter == 'h' or caracter == 'H':
        codigo = '....'
    if caracter == 'i' or caracter == 'I':
        codigo = '..'
    if caracter == 'j' or caracter == 'J':
        codigo = '.---'
    if caracter == 'k' or caracter == 'K':
        codigo = '-.-'
    if caracter == 'l' or caracter == 'L':
        codigo = '.-..'
    if caracter == 'm' or caracter == 'M':
        codigo = '--'
    if caracter == 'n' or caracter == 'N':
        codigo = '-.'
    if caracter == 'ñ' or caracter == 'Ñ':
        codigo = '--.--'
    if caracter == 'o' or caracter == 'O':
        codigo = '---'
    if caracter == 'p' or caracter == 'P':
        codigo = '.--.'
    if caracter == 'q' or caracter == 'Q':
        codigo = '--.-'
    if caracter == 'r' or caracter == 'R':
        codigo = '.-.'
    if caracter == 's' or caracter == 'S':
        codigo = '...'
    if caracter == 't' or caracter == 'T':
        codigo = '_'
    if caracter == 'u' or caracter == 'U':
        codigo = '..-'
    if caracter == 'v' or caracter == 'V':
        codigo = '...-'
    if caracter == 'w' or caracter == 'W':
        codigo = '.--'
    if caracter == 'x' or caracter == 'X':
        codigo = '-..-'
    if caracter == 'y' or caracter == 'Y':
        codigo = '-.--'
    if caracter == 'z' or caracter == 'Z':
        codigo = '--..'
    if caracter == '0':
        codigo = '-----'
    if caracter == '1':
        codigo = '.----'
    if caracter == '2':
        codigo = '..---'
    if caracter == '3':
        codigo = '...--'
    if caracter == '4':
        codigo = '....-'
    if caracter == '5':
        codigo = '.....'
    if caracter == '6':
        codigo = '-....'
    if caracter == '7':
        codigo = '--...'
    if caracter == '8':
        codigo = '---..'
    if caracter == '9':
        codigo = '----.'
    if caracter == '.':
        codigo = '.-.-.-'
    if caracter == ',':
        codigo = '--..--'
    if caracter == '?':
        codigo = '..--..'
    if caracter == '!':
        codigo = '-.-.--'
    if caracter == ' ':
        codigo = ' '
    return codigo
#------------------------------------------
 
print 'COVERSOR TEXTO->MORSE'
print '---------------------\n'
texto = raw_input('> ')   #Se define una entrada para ser convertida en morse
 
for letra in texto: #Hace un recorrido de letras en el parametro introducido
    print morse(letra) #Imprime el equivalente de cada letra en morse
 
# raw_input()