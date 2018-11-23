import matplotlib.pyplot as plt
import numpy as np


#Pasando y regresando funciones
def composeq(f,g):
		def h(x):
			return f(g(x))
		return h
		
def f1(x):
	return 2*x
	
def f2(x):
	return np.sin(x)
	
	
	
#Curryng
def curried_pow(x):
		def h(y):
			return pow(x,y)
	return h
	
