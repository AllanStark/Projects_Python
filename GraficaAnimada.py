#  return 
from __future__ import unicode_literals
# -*- coding: utf-8 -*-
"""
PROGRAMA QUE MUESTRA Y GRAFICA 3 SUBPLOTS 
EL PRIMERO MUESTRA LA FUNCION SENO Y COSENO
EL SEGUNDO MUESTRA LA SUMA DEL SENO Y COSENO
EL TERCERO MUESTRA LA TRANSFORMADA RAPIDA DE FOURIER DE LA SUMA DE SENO Y COSENO
"""
#Importamos las bibliotecas correspondientes para el funcionamiento
#Numpy es la biblioteca numerica de python
#def GraficA()
import numpy as np 			
 #Matplotlib es una de las bibliotecas que permiten realizar animaciones y graficas en python
import matplotlib.pyplot as plt
 #Animation es una de las formas en las que se puede animar un plot, tambien existen FuncArtist entre otras
import matplotlib.animation as animation
 
 #Creamos una figura donde especificamos el numero de subplots que queramos para que se ajuste el frame para su muestreo
fig, ax = plt.subplots(3,figsize=(12,8),facecolor= 'springgreen')
 #Poniendo titulo a la grafica
 #fig.suptitle("Arreglo de funciones", fontsize = 14)
 #Especificamos el tamao y forma del frame o ventana
plt.tight_layout(pad=0.5, w_pad=0.5, h_pad=1.2)
 
 #Asignamos el nombre de cada uno de nuestros subplots y el lugar donde queremos colocarlo
ax1 = fig.add_subplot(311) # Se ordena para 3 subplots 1 columna y en la primera posicion
ax2 = fig.add_subplot(312) # Para la posicion 2
ax3 = fig.add_subplot(313) # Para la posicion 3
 
 #Activando las cuadriculas
ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
 
 # Set titles of subplots
ax1.set_title('Sin y Cos')
ax2.set_title('Sin + Cos')
ax3.set_title('fft (Sin+Cos)')
 
 #Poniendo las etiquetas de los ejes
ax1.set_xlabel("Time(sec)")
 #ax1.set_ylabel("F1(t),F2(t)")
ax2.set_xlabel("Time(sec)")
 #ax2.set_ylabel("F1(t)+F2(t)")
ax3.set_xlabel("Frequency (Hz)")
 #ax3.set_ylabel("|FFT{F1(t)+F2(t)}|")
 
 #Configuracion de los las legendas de las graficas
 #p011, = ax1.plot(x,ysen,'b-', label="Cos")
 #p012, = ax1.plot(x,ycos,'g-', label="Sen")
 #p021, = ax2.plot(x,ysencos,'r-', label="Sen+Cos")
 #Aplicando las etiquetas
 #ax1.legend([p011,p012], [p011.get_label(),p012.get_label()])
 #ax2.legend([p021], [p021.get_label()])
 
ax1.set_ylim([-2,2])	  #Se le asignan los limites al eje y
ax1.set_xlim([0,20])      #Se le especifican los limites los limites al eje x
ax2.set_ylim([-2,2])	  #Se le asignan los limites al eje y
ax2.set_xlim([0,20])      #Se le especifican los limites los limites al eje x
 #ax3.set_ylim([0,1.5])	  #Se le asignan los limites al eje y
 #ax3.set_xlim([0,250])    #Se le especifican los limites los limites al eje x
 
plt.setp(ax2.get_xticklabels(), visible=False) #Este codigo oculta las etiquetas del eje x
plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax3.get_xticklabels(), visible=False) 
 
plt.setp(ax2.get_yticklabels(), visible=False) #Este codigo oculta las etiquetas del eje x
plt.setp(ax1.get_yticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False) 
 
 
x = np.arange(0, 20, 0.01) # Establecemos el rango para el eje x
 
 #Establecemos lo que se va a graficar en los subplots
line, = ax1.plot(x, np.sin(x),'r-', lw=2.0) #Se grafica x y el seno de x
line1, = ax1.plot(x, np.cos(2*x),'g-', lw=2.0) #Se grafica x y el seno de 2x
line2, = ax2.plot(x,np.sin(x) + np.cos(2*x),'y-', lw=2.0) #Se grafica la suma del seno de x y el coseno de 2x
suma = (np.sin(x) + np.cos(2*x))	#Se establece suma como la suma de las funciones
 
Y  = np.fft.fft(suma)  #Establecemos a Y como la seal a graficar y convertir como la transformada de fourier
freq = np.fft.fftfreq(len(suma), d=0.01) # Le asignamos el nombre de freq a los valores de la suma y utilizando len para medir el tamao de la misma
Y = np.abs(Y) #Obtenemos los valores absolutos de la suma y se los asignamos a Y
line3, = ax3.plot(freq, Y) #Establecemos el plot que se va a graficas que es x=freq y el eje y = Y
 
#Establecemos la funcion de la animacion
def animate(i):
 
#Hacemos un ajuste de if para establecer cada cuanto cambia el tamao de las funciones
	if i<300: 	
 		line.set_ydata(np.sin(x + i/0.01))  #Actualizamos los valores de la funcion del seno
 		line1.set_ydata(np.cos(2*x + i/0.01))  #Actualizamos los valores de la funcion coseno
 		line2.set_ydata(np.sin(x + i/0.01)+np.cos(2*x + i/0.01))  #Actualizamos los datos de la funcion seno + coseno
 		line3.set_ydata(np.fft.fft(np.sin(x + i/0.01) + np.cos(2*x + i/0.01)))  #Actualizamos los datos de la funcion fft
 		return line, line1, line2, line3,
 
 	if i>299 and i<600:
 		line.set_ydata(np.sin(x + i/0.01)) 
 		line1.set_ydata(np.sin(4*x + i/0.01))  
 		line2.set_ydata(np.sin(x + i/0.01)+np.cos(4*x + i/0.01)) 
 		line3.set_ydata(np.fft.fft(np.sin(x + i/0.01) + np.sin(4*x + i/0.01))) 
 		return line, line1, line2, line3,
 
 	if i>599 and i<900:
 		line.set_ydata(np.sin(x + i/0.01))  
 		line1.set_ydata(np.cos(8*x + i/0.01))  
 		line2.set_ydata(np.sin(x + i/0.01)+np.cos(8*x + i/0.01))  
 		line3.set_ydata(np.fft.fft(np.sin(x + i/15) + np.cos(8*x + i/0.01)))  
 		return line, line1, line2, line3,
 
 	if i>899 and i<1200:
 		line.set_ydata(np.sin(x + i/0.01)) 
 		line1.set_ydata(1) 
 		line2.set_ydata(np.sin(x + i/0.01)+1)  
 		line3.set_ydata(np.fft.fft(np.sin(x + i/0.01) + 1))  
 		return line, line1, line2, line3,
 		#El signo antes de la variable i ajusta el sentido que van a tener las graficas para este caso
 		#El valor de la division i/0.01, entre mas pequeo sea el dividendo mayor es la velocidad de muestreo
 		#Para los valores que se muestran no se puede cambiar el valor para fft por la variable suma porque altera el resultado de la grafica
 
 #La Funcion init establece los valores donde se inicializan los datos
def init():
     line.set_ydata(np.ma.array(x, mask=True))
     line1.set_ydata(np.ma.array(x, mask=True))
     line2.set_ydata(np.ma.array(x, mask=True))
     line3.set_ydata(np.ma.array(x, mask=True))
     return line, line1, line2, line3, 
#Le asignamos el nombre de ani a la funcion animation que nos permite hacer la animacion con sus respectivos parametros
ani = animation.FuncAnimation(fig, animate, np.arange(1, 1200), init_func=init, interval=25, blit=True, repeat=True, repeat_delay=2000)
 #Muestra la grafica 
plt.show()
 #En caso de que quisieramos guardar la grafica sin embargo se necesitan los codecs correspondientes como ffmpeg o mencoder
 #anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])