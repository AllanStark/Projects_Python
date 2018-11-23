from numpy import *
from matplotlib.pyplot import *

signal=loadtxt("signal.txt",delimiter=",")

t=signal[:,0]
s=signal[:,1]
N=len(s)

#Fast Fourier Transform
ft=fft.fft(s,N)

#ft: Vector de amplitudes de las componentes
M=(N-1)/2
T=t[-1]

print M
def signal_teo(t):
    serie=ft[0]
    for k in xrange(1,8):
        w=2*pi*k/T
        serie+=2*ft[k]*exp(1j*w*t)
    serie=serie/N
    return serie

figure()
plot(t,s,'ko',markersize=2)
plot(t,signal_teo(t),'b-')
savefig("signal.png")

