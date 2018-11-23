# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Created on Wed Sep 07 00:16:53 2016
Programa que por medio de funciones trabaja para realizar operaciones con fracciones


@author: Sorek
"""
def sumafr(x,y,w,z):
            nom1 = int(x)
            den1 = int(y)
            nom2 = int(w)
            den2 = int(z)
            comunden = den1 * den2
            primerv = ((comunden / den1) * nom1)
            segunv = ((comunden / den2) * nom2)
            suma = primerv + segunv
            return suma,'/',comunden
def restafr(x,y,w,z):
            nom1 = int(x)
            den1 = int(y)
            nom2 = int(w)
            den2 = int(z)
            comunden = den1 * den2
            primerv = ((comunden / den1) * nom1)
            segunv = ((comunden / den2) * nom2)
            resta = primerv - segunv
            return resta,'/',comunden
def mulfr(a,b,c,d):
            comunnum = a * c
            comunden = b * d
            return comunnum,comunden
def divfr(a,b,c,d):
      '''

      Function: divfr

      Summary: Funcion que realiza la division de fracciones

      Examples: divfr(1,2,3,4) regresa, 2,3

      Attributes: 

            @param (a):Numerador1

            @param (b):Denominador1

            @param (c):Numerador2

            @param (d):Denominador2

      Returns: comunnum, comundenom

      '''

      nom1 = int(a)
      den1 = int(b)
      nom2 = int(c)
      den2 = int(d)
      numerador = a * d 
      denominador = b * c
      return numerador, denominador

def invfr(a,b):
      return b,a

def negfr(a,b):
      return -a,-b


            


