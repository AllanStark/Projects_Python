import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111)
# You can initialize this with whatever
im = ax.imshow(np.random.rand(6, 10), cmap='bone_r', interpolation='nearest')


def animate(i):
    aux = np.zeros(60)
    aux[i] = 1
    image_clock = np.reshape(aux, (6, 10))
    im.set_array(image_clock)

ani = animation.FuncAnimation(fig, animate, frames=60, interval=1000)
#ani.save('clock.mp4', fps=1.0, dpi=200)
plt.show()