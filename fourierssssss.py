"""import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
n = 2 ** 6  # Nmero de intervalos
f = 400.0  # Hz
dt = 1 / (f * 16)  # Espaciado, 16 puntos por perodo
t = np.linspace(0, (n - 1) * dt, n)  # Intervalo de tiempo en segundos
y = np.sin(2 * pi * f * t) - 0.5 * np.sin(2 * pi * 2 * f * t)  # Senal
plt.plot(t, y)
plt.plot(t, y, 'ko')
plt.xlabel('Tiempo (s)')
plt.ylabel('$y(t)$')"""
from scipy.fftpack import fft, fftfreq
Y = fft(y) / n  # Normalizada
frq = fftfreq(n, dt)  # Recuperamos las frecuencias
plt.vlines(frq, 0, Y.imag)  # Representamos la parte imaginaria
plt.annotate(s=u'f = 400 Hz', xy=(400.0, -0.5), xytext=(400.0 + 1000.0, -0.5 - 0.35), arrowprops=dict(arrowstyle = "->"))
plt.annotate(s=u'f = -400 Hz', xy=(-400.0, 0.5), xytext=(-400.0 - 2000.0, 0.5 + 0.15), arrowprops=dict(arrowstyle = "->"))
plt.annotate(s=u'f = 800 Hz', xy=(800.0, 0.25), xytext=(800.0 + 600.0, 0.25 + 0.35), arrowprops=dict(arrowstyle = "->"))
plt.annotate(s=u'f = -800 Hz', xy=(-800.0, -0.25), xytext=(-800.0 - 1000.0, -0.25 - 0.35), arrowprops=dict(arrowstyle = "->"))
plt.ylim(-1, 1)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Im($Y$)')
plt.show()