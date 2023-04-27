import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



t = np.linspace(0,4*np.pi,1000)
x = np.sin(t)

trail_length = 100
def get_chunks(i):
    t_chunk = t[i-trail_length:i]
    x_chunk = x[i-trail_length:i]
    return t_chunk, x_chunk

trail_length = 100
alphas = np.linspace(0, 1, trail_length-1)

class UpdateDist:
    def __init__(self, ax, prob=0.5):
        self.success = 0
        self.prob = prob
        self.line = [ax.plot([], [], color='red', alpha=alpha)[0] for alpha in alphas]
        self.ax = ax

        # Set up plot parameters
        self.ax.set_xlim(0, 4*np.pi)
        self.ax.set_ylim(-1.1, 1.1)
        self.ax.grid(True)


    def __call__(self, i):
        for j, alpha in enumerate(alphas):
            self.line[j].set_data(t[i-trail_length+j:i-trail_length+j+2], x[i-trail_length+j:i-trail_length+j+2])
        
        return self.line


fig, ax = plt.subplots()
ud = UpdateDist(ax, prob=0.7)
anim = FuncAnimation(fig, ud, frames=1000, interval=20, blit=True)
plt.show()