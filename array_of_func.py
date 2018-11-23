
""" Este archivo ilustra algunas ideas de la programación funcional incorporada en python """

import numpy as np
import matplotlib.pyplot as plt


t1 = np.arange(0.0, 10.0, 0.1) #eje x en algunas funciones 

# grafica varias funciones
plt.plot(t1,t1)
plt.plot(t1,0.1*t1*t1)
plt.plot(t1,10*np.sin(2*t1))
plt.show()


def rct(t):    #recta
    f=pow(t,1)
    return f

def prbl(t):    #parabola
    f=pow(t,2)
    return f

def cbc(t):     #cubica
    f=pow(t,3)
    return f

funcarray=[rct,prbl,cbc]  #arreglo de funciones

# grafica cada uno de los elementos del arreglo
plt.plot(t1,funcarray[0](t1))
plt.plot(t1,funcarray[1](t1))
plt.plot(t1,funcarray[2](t1))
plt.show()



def graficar(funcarr,trange):
    """Grafica una serie de funciones especificadas en funcarr en el
rango especificado por trange.  funcarr es una lista de funciones y
trange es un arregro de tres elementos [tmin,tmax,tstep]

    """
    tmin,tmax,tstep=trange
    t=np.arange(tmin,tmax,tstep)
    for i in range(len(funcarr)):
        plt.plot(t,funcarr[i](t))
    plt.show()
    return

funcarray=[rct,prbl,cbc]
tr=[0,10,0.1]        
graficar(funcarray,tr)



def potencia(a): # recibe a regresa t^a
    def f(t):
        return pow(t,a)
    return f

# genera un arreglo de t^a, a=0.2, 0.5, 1
farr=[potencia(0.2),potencia(0.5),potencia(1)]
graficar(farr,tr)

def farrpot(parrange):
    """recibe un rango y genera t^a, con a valores en prange
    prange es una lista de tres elementos [amin, amax, astep]
    """
    amin,amax,astep=parrange
    a=np.arange(amin,amax,astep)
    f=[]
    for i in range(len(a)):
        f.append(potencia(a[i]))
    return f

par=[0,1,0.2]          #establece un rango de parametros
funcarray=farrpot(par) #genera un arreglo de funciones t^a
graficar(funcarray,tr) # grafica el arreglo

def osc(frec): # recibe f y regresa b sin(2 pi f t) 
    b=1
    def f(t):
        return b*np.sin(2*np.pi*frec*t)
    return f

def farrosc(parrange):
    """recibe un rango y genera t^a, con a valores en prange
    prange es una lista de tres elementos [amin, amax, astep]
    """
    amin,amax,astep=parrange
    a=np.arange(amin,amax,astep)
    f=[]
    for i in range(len(a)):
        f.append(osc(a[i]))
    return f

par=[0,1,0.2]          #establece un rango de parametros
funcarray=farrosc(par) #genera un arreglo de funciones t^a
graficar(funcarray,tr) # grafica el arreglo

def farrpar(fpar,parrange):
    amin,amax,astep=parrange
    a=np.arange(amin,amax,astep)
    f=[]
    for i in range(len(a)):
        f.append(fpar(a[i]))
    return f


par=[0,1,0.2]          #establece un rango de parametros

funcarray=farrpar(potencia,par) #genera un arreglo de funciones t^a
graficar(funcarray,tr) # grafica el arreglo

funcarray=farrpar(osc,par) #genera un arreglo de funciones sin(2 pi f t)
graficar(funcarray,tr) # grafica el arreglo



