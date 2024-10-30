# -*- coding: utf-8 -*-
"""Data Visualization (Animated Plot).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11qOdg72BSpfU8fGdEipBHSGtYglP2-Jj
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(x, np.sin(x))

# Update function for animation
def update(frame):
    line.set_ydata(np.sin(x + frame/10.0))
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, blit=True)
plt.title('Animated Sine Wave')
plt.show()

