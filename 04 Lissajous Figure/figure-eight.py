import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# import time
# last = time.perf_counter()



# Physics
def X(t):
    return 10*np.sin(2*t)

def Y(t):
    return 10*np.sin(t)



# Plotting
fig, ax = plt.subplots(figsize=(8,5), facecolor='lightskyblue')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_aspect('equal')

# Initial line
line, = ax.plot(
    [],
    [],
    color='red',
    marker='o',
    linewidth=2,
    markersize=8
)

trail, = ax.plot(
    [],
    [],
    color='lightgrey',
    linestyle='--',
    linewidth=3,
)


# Animations
def init():
    line.set_data([0], [0])
    trail.set_data([0], [0])
    return line, trail,

def update(frame):
    # global last
    # now = time.perf_counter()
    # print(f"{1/(now-last):.1f} FPS")
    # last = now

    x = X(frame)
    y = Y(frame)
    line.set_data([x], [y])
    
    k = np.linspace(frame-2, frame, 20)
    trail.set_data(X(k), Y(k))
    return line, trail


ani = FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 5*np.pi, 600),
    init_func=init,
    interval=10,
    blit=True
)


plt.show()