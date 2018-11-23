import numpy as np
import matplotlib.pyplot as plt
from scipy import fft
from scipy import *

def senal1_gen():
    Fs = 1000                         # sampling rate
    Ts = 1.0/Fs                      # sampling interval
    t = np.arange(0,1,Ts)            # time vector
    ff = 6                           # frequency of the signal
    y1 = np.sin(2 * np.pi * ff * t)
    y2 = 0*t
    y=y1+y2
    return y

def senal2_gen():
    Fs = 1000                         # sampling rate
    Ts = 1.0/Fs                      # sampling interval
    t = np.arange(0,1,Ts)            # time vector
    ff = 6                           # frequency of the signal
    y1 = 0*t #np.sin(2 * np.pi * ff * t)
    y2 = 0*t #(1/2)*np.sin(2 * np.pi * 10*ff * t)
    y=y1+y2
    return y

def senal_comb(y1,y2,n):
    

    return y

y1=senal1_gen()
y2=senal2_gen()

y=y1+y2

def myfft(senal):
    n2=int(len(senal)/2)
    f = np.fft.fft(senal)/n2              # fft computing and normalization
    f = f[range(n2)]
    refft = abs(f)
    return refft

y = senal_gen()
Y = myfft(y)

plt.subplot(2,1,1)
plt.plot(t,y,'k-')
plt.xlabel('time')
plt.ylabel('amplitude')

plt.subplot(2,1,2)
plt.plot(freq, Y, 'r-')
plt.xlabel('freq (Hz)')
plt.ylabel('|Y(freq)|')

plt.show()      

n = len(y)                       # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
freq = frq[range(int(n/2))]           # one side frequency range

