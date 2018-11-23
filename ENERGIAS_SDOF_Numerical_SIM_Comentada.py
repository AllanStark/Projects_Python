# -*- coding: utf-8 -*-
"""
@author: Alan_Torres	
"""
# Se declaran las bibliotecas pertinentes para la programacion
import numpy as np #biblioteca para la soluciones numericas
from numpy.linalg import inv #biblioteca para sacar la inversa de una  matriz
from matplotlib import pyplot as plt #Biblioteca para sacar 
import math #biblioteca para uso de senos y cosenos
from time import* #biblioteca para medir los tiempos de ejecucion
energias_txt = open('energias.txt','w')
vel_desplazamiento_txt = open('vel_desplazamiento.txt', 'w')
fuerza_txt = open('fuerza.txt', 'w')
t1 = clock() #tomamos la medicion del reloj
#Variables
m = 2.0 # Se define la masa
k = 2.0 # Se define la constante elastica
c = 3.0 # Se define la constancia de amortiguamiento #Critical damping = 2 * SQRT(m*k) = 4.0

F0 = 3.0 # Se define la magnitud de la fuerza 
delta_t = 0.0001 # Tiempo de paso entre iteracion
omega = 1.0 # Velocidad angular o frecuencia del movimiento
T= 50 # tamano del vector tiempo
time = np.arange(0.0, T, delta_t) # se define un arreglo para el vector tiempo y el paso entre mediciones

#Estado inicial
# Se definen las variables para la solucion a traves de espacio de estados
y = np.array([0,0]) #[Velocidad, Desplazamiento] Se define un arreglo para ir guardando los valores de la velocidad y desplazamiento 
print ('Y',y)
A = np.array([[m,0],[0,1]]) #Se define el arreglo a que corresponde a la matriz de estado
print ('A',A)
B = np.array([[c,k],[-1,0]]) #Se define el arreglo B que corresponde a la matriz de entrada
print ('B',B)
F = np.array([0.0, 0.0]) # Se define el arreglo F que corresponde a la matriz de transmision directa
print ('F',F)
#Se declaran unos arreglos vacios para ir agregando los valores de salida a la integración númerica
Y = [] # El arreglo Y guarda los valores que se van generando para los parametros de velocidad y aceleración
force = [] # El arreglo force almacena los datos de la fuerza
Kin = [] # El arreglo Kin almacena los datos correspondientes a la energia cinetica
Pot = [] # El arreglo Pot almacena los datos correspondientes a la energia Potencial
Trabajo =[]
Time_execution= []

#Se declara un for para ir evaluando en cada unidad de tiempo el estado del sistema
for t in time:
	if t <= 5:  # Esta sentencia marca hasta que momento se pretende aplicar una vibracion forzada
		F[0] = F0 *math.sin(omega*t) # declaramos una fuerza de entrada la cual es del tipo cosenoidal 
	else:
		F[0] = 0.0#math.tan(F0 *math.cos(omega*t)) # cuando el tiempo pasa de uno se deja de aplicar una fuerza para ver las vibraciones libres

	#F[0] = F0 * np.cos(omega*t)
	y = y + delta_t * inv(A).dot( F - B.dot(y) )# Calculo para guardar las soluciones evaluadas en el tiempo
	Y.append(y[1]) # Se agregan los valores de la matriz calculada en y como la velocidad del sistema
	force.append(F[0]) # se agregan los valores calculados para la fuerza de entrada en el arreglo F[]
	KE = 0.5 * m * y[0]**2 #Se calcula la energia cinetica del sistema
	Kin.append(KE) #se agrega al arreglo Kin los valores evaluados en el tiempo para la energia cinetica
	PE = 0.5 * k * y[1]**2#Se calcula la energia potencial del sistema
	Pot.append(PE) #Se agregan los valores calculados al arreglo para la energia potencial
	#energias_txt.write("\n")
	energias_txt.write(str(KE))#+ ", " + str(PE)+ "\n")
	vel_desplazamiento_txt.write(str(y[0]) + "," + str(y[1]) + "\n")
	fuerza_txt.write(str(F[0]) + "\n")
	#energias_txt.close()
	#energias_txt.write("\n")
			
	#print('Desplazamiento',y[1], 'velocidad',y[0])
	#print('Fuerza', F[0])
	#Trab = F[0]*y[1]
	#Trabajo.append(Trab)
	#print ('Amortiguacion Critica:', np.sqrt((-c**2 + 4*m*k) / (2.0 * m)))
	#print ('m', m, 'k',k ,'c', c)
	#print ('Frecuencia Natural:', np.sqrt(k/m))
#Definimos una condicion para evaluar la dinamica del sistema a traves de las energias potencial y cinetica
	if t % 1 <= 0.01:
			print ('Energia Total:', KE+PE, 'Energia Cinetica:', KE, 'Energia Potencial:', PE)
			#energias_txt.write("\n")
			#energias_txt.write(",".join(str(KE) for t in time))
			#energias_txt.write("\n")
			#print ('Trabajo:', Trabajo)
t2 = clock() #Se Hace una segunda llamada al reloj
#Creamos una variable para guardar los pasos de tiempo y agregar los valores de los calculos
t = [i for i in time] # Se evalua la variable i para cada valor de tiempo
Time_execution.append(t2-t1)
print 'tiempo de ejecucion', Time_execution
# t2 = clock()
#print 'tiempo de ejecucion', t2-t1
plt.plot(t,Y) #Graficamos los valores del desplazamiento en cada unidad de tiempo
plt.plot(t, force) # Graficamos los valores de la fuerza aplicada en cada momento de tiempo
plt.plot(t, Kin) # Graficamos los valores de la energia cinetica para cada momento de tiempo
plt.plot(t, Pot) #graficamos los valores de la energia potencial para cada momento de tiempo
plt.grid(True) # graficamos las celdas
plt.legend(['Desplazamiento', 'Fuerza', 'Energia Cinetica', 'Energia Potencial'], loc= 'upper right') # aplicamos las etiquetas de los valores
plt.title('DESPLAZAMIENTO Y ENERGIA') # Agregamos titulo a la grafica
plt.xlabel('tiempo en s')
#print ('Amortiguacion Critica:', np.sqrt((-c**2 + 4*m*k) / (2.0 * m)))
#print ('Frecuencia Natural:', np.sqrt(k/m))
print ('tiempo de ejecucion', t2-t1)
plt.show()
