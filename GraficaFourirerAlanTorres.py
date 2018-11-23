# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
PROGRAMA QUE MUESTRA Y GRAFICA 3 SUBPLOTS 
EL PRIMERO MUESTRA LA FUNCION SENO Y COSENO
EL SEGUNDO MUESTRA LA SUMA DEL SENO Y COSENO
EL TERCERO MUESTRA LA TRANSFORMADA RAPIDA DE FOURIER DE LA SUMA DE SENO Y COSENO
"""
#Importamos las bibliotecas correspondientes para el funcionamiento
#Numpy es la biblioteca numerica de python
import numpy as np 			
#Matplotlib es una de las bibliotecas que permiten realizar animaciones y graficas en python
import matplotlib.pyplot as plt
#Animation es una de las formas en las que se puede animar un plot, tambien existen FuncArtist entre otras
import matplotlib.animation as animation
from scipy import fft

#Creamos una figura donde especificamos el numero de subplots que queramos para que se ajuste el frame para su muestreo
fig, ax = plt.subplots(3,figsize=(12,8),facecolor= 'springgreen')
#Poniendo titulo a la grafica
#fig.suptitle("Arreglo de funciones", fontsize = 14)
#Especificamos el tamaño y forma del frame o ventana
# plt.tight_layout(pad=0.5, w_pad=0.5, h_pad=1.2) # Para poner un menor marco de la figura, es decir, menor distancia entre la grafica y el contorno

#Asignamos el nombre de cada uno de nuestros subplots y el lugar donde queremos colocarlo
ax1 = fig.add_subplot(311) # Se ordena para 3 subplots 1 columna y en la primera posicion
ax2 = fig.add_subplot(312) # Para la posicion 2
ax3 = fig.add_subplot(313) # Para la posicion 3

#Activando las cuadriculas
ax1.grid(True)
ax2.grid(True)
ax3.grid(True)

# Set titles of subplots
ax1.set_title('Sin y Pulse')
ax2.set_title('Sin + Pulse')
ax3.set_title('fft (Sin+Pulse)')

#Poniendo las etiquetas de los ejes
ax1.set_xlabel("Time(sec)")
#ax1.set_ylabel("F1(t),F2(t)")
ax2.set_xlabel("Time(sec)")
#ax2.set_ylabel("F1(t)+F2(t)")
ax3.set_xlabel("Frequency (Hz)")
#ax3.set_ylabel("|FFT{F1(t)+F2(t)}|")

# ax1.set_ylim([-2,2])	  #Se le asignan los limites al eje y
# ax1.set_xlim([0,2])      #Se le especifican los limites los limites al eje x
# ax2.set_ylim([-2,2])	  #Se le asignan los limites al eje y
# ax2.set_xlim([0,2])      #Se le especifican los limites los limites al eje x
# ax3.set_ylim([0,1.5])	  #Se le asignan los limites al eje y
# ax3.set_xlim([0,250])    #Se le especifican los limites los limites al eje x

# plt.setp(ax2.get_xticklabels(), visible=False) #Este codigo oculta las etiquetas del eje x
# plt.setp(ax1.get_xticklabels(), visible=False)
# plt.setp(ax3.get_xticklabels(), visible=False) 

# plt.setp(ax2.get_yticklabels(), visible=False) #Este codigo oculta las etiquetas del eje x
# plt.setp(ax1.get_yticklabels(), visible=False)
# plt.setp(ax3.get_yticklabels(), visible=False) 

#Definiendo una funcion para la señal seno
# def sen(signal_data):
#     '''Genera la función seno con las especificaciones dadas por el
#     arreglo signal_data. Regresa una lista de dos listas. La primera
#     contiene los datos del eje X y la segunda el eje Y.  El arreglo
#     signal_data es de la forma: [ti,tf,fm,frec] donde: ti=tiempo
#     inicial, tf=tiempo final, fm=frecuencia de muestreo, amp=amplitud
#     de la señal, frec=frecuencia de la señal, fase= fase.
#     '''
#     # la siguiente es una manera de asignar varias variables a la vez
#     ti,tf,fm,amp,frec,fase = signal_data 

#     pm = 1.0/fm                  # pm=periodo de muestreo
#     t = np.arange(ti,tf,pm)      # time vector (eje X)
#     arg = 2 * np.pi * frec * t + fase # argumento del seno
#     y = amp*np.sin(arg) # eje Y
#     return [t,y] 

# def pulso(signal_data):
#     '''Genera la función seno con las especificaciones dadas por el
#     arreglo signal_data. Regresa una lista de dos listas. La primera
#     contiene los datos del eje X y la segunda el eje Y.  El arreglo
#     signal_data es de la forma: [ti,tf,fm,frec] donde: ti=tiempo
#     inicial, tf=tiempo final, fm=frecuencia de muestreo, amp=amplitud
#     de la señal, frec=frecuencia de la señal, fase= fase.
#     '''
#     # la siguiente es una manera de asignar varias variables a la vez
#     ti,tf,fm,amp,frec,fase = signal_data 
#     pm = 1.0/fm                  # pm=periodo de muestreo
#     t = np.arange(ti,tf,pm)      # time vector (eje X)
#     t = np.arange(ti,tf,pm)      # time vector (eje X)
#     arg = 2 * np.pi * frec * t + fase # argumento del seno
#     pulso_amp1 =  np.sign(np.sin(arg)) # pulso unitario el signo(seno) 
#     y = amp*pulso_amp1
#     return [t,y]


# def combfunc(f1,f2,t_index):
#     '''Recibe dos funciones y devuelve otra que es la combinación de las
#     dos. f1 y f2 son listas con dos elementos que también son
#     listas. El primer elemento contiene el eje X y el segundo el eje
#     Y. La función de resultado f3 es igual a f1 Si t<t_index y f3 es
#     igual a f2 en otro caso.

#     '''
#     t_range = range(len(f1[0])) #Tamaño del eje X 
#     y=[] # y empieza como una lista vacía
#     for i in t_range:          #va a recorrer el eje X
#         if (f1[0][i]<t_index): # si t<t_index
#             y.append(f1[1][i])    # hacer que y=f1[1]
#         else:                  # En caso contrario
#             y.append(f2[1][i])    # hacer que y=f2[1]
#     f3=[f1[0],y]
#     return f3


# # Establece los datos del eje X
# t_ini = 0   #tiempo inicial
# t_fin = 10   #tiempo final
# f_mu  = 100 #frecuencia de muestreo

# # Establece los datos de la senal 
# amplitud = 2 #Amplitud de la senoide
# frecuencia = 2# frecuencia de la senoide

# # tres fases  para tres señales distintas
# fase = 2*((2*np.pi/3))

# # Empaca los datos           
# data1=[t_ini,t_fin, f_mu, amplitud, frecuencia, fase]
# data2=[t_ini,t_fin, f_mu, amplitud/2, frecuencia, fase]
           
# # genera dos funciones
# f1=sen(data1)
# f2=pulso(data2) 

# # genera tres funciones a partir de combinar las dos anteriores
# fa=combfunc(f1,f2,0.25) # t_index = 0.25
# fb=combfunc(f1,f2,0.5)  # t_index = 0.5
# fc=combfunc(f1,f2,0.75) # t_index = 0.75

# # grafica las tres funciones           
# plt.plot(fa[0],fa[1])
# plt.plot(fb[0],fb[1])
# plt.plot(fc[0],fc[1])
# plt.show()
