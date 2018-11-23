# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import hashlib
 
def md5(String):
    return hashlib.md5(String).hexdigest()
 
def sha1(String):
    return hashlib.sha1(String).hexdigest()
 
def sha224(String):
    return hashlib.sha224(String).hexdigest()
 
def sha256(String):
    return hashlib.sha256(String).hexdigest()
 
def sha384(String):
    return hashlib.sha384(String).hexdigest()
 
def sha512(String):
    return hashlib.sha512(String).hexdigest()
 
print '''
    === String Encode ===
    1 - md5
    2 - sha1
    3 - sha224
    4 - sha256
    5 - sha384
    6 - sha 512
    =====================
    '''
 
while True:
    String = raw_input('Ingrese la cadena de texto a convertir > ')
    opcion = input('Elija una opcion > ')
    if opcion == 1:
        print 'Su cadena cifrada es > %s' % md5(String)
    elif opcion == 2:
        print 'Su cadena cifrada es > %s' % sha1(String)
    elif opcion == 3:
        print 'Su cadena cifrada es > %s' % sha224(String)
    elif opcion == 4:
        print 'Su cadena cifrada es > %s' % sha256(String)
    elif opcion == 5:
        print 'Su cadena cifrada es > %s' % sha384(String)
    elif opcion == 6:
        print 'Su cadena cifrada es > %s' % sha512(String)