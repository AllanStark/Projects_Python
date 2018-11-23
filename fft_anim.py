# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:46:08 2016

@author: elikz
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
plt.tight_layout(pad=0.5, w_pad=0.5, h_pad=1.2)
ax1 = fig.add_subplot(311)
ax1.set_ylim([-2,2])
ax1.set_xlim([0,10])
ax2 = fig.add_subplot(312, sharex=ax1, sharey=ax1)
ax3 = fig.add_subplot(313, sharex=ax1, sharey=ax1)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax3.get_xticklabels(), visible=False)


x = np.arange(0, 20, 0.01)

line, = ax1.plot(x, np.sin(x))
line1, = ax1.plot(x, np.cos(x))
line2, = ax2.plot(x, np.sin(x) + np.cos(x))
sp = np.fft.fft(np.sin(x) + np.cos(x))
freq = np.fft.fftfreq(sp.shape[-1])
line3, = ax3.plot(x, freq)

def animate(i):
    line.set_ydata(np.sin(x + i/20))  # update the data
    line1.set_ydata(np.cos(x + i/20))  # update the data
    line2.set_ydata(np.sin(x + i/20)+np.cos(x + i/20))  # update the data
    line3.set_ydata(np.fft.fft(np.sin(x+i/20) + np.cos(x+i/20)))  # update the data
    return line, line1, line2, line3,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    line1.set_ydata(np.ma.array(x, mask=True))
    line2.set_ydata(np.ma.array(x, mask=True))
    line3.set_ydata(np.ma.array(x, mask=True))
    return line, line1, line2, line3,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
                              interval=25, blit=True, repeat=True)

plt.show()