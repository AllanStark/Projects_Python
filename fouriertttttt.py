from numpy import *
from matplotlib.pyplot import *

signal = loadtxt("signal.txt", delimiter= ",")
t = signal[:,0]
s = signal[:,1]
N=len(s)
#FFT
ft= fft.fft(s,N)

figure()
plot(t,s)
#plot.show()
savefig("signal.png")


print signal

