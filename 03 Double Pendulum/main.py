import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
import math






# Physics
roof_x = np.linspace(-10, 10, 2)
roof_y = np.full_like(roof_x, 10)
trail_x = deque(maxlen=20)
trail_y = deque(maxlen=20)

theta1_max = np.radians(float(input("Enter theta1 (in degrees): ")))
theta2_max = np.radians(float(input("Enter theta2 (in degrees): ")))
length1 = float(input("Enter length of the rod-1 (in m): "))
length2 = float(input("Enter length of the rod-2 (in m):"))
phi1 = 0
phi2 = 0


# Plotting
fig, ax = plt.subplots(figsize=(10, 6), facecolor='paleturquoise')
ax.set_title("Double Pendulum", color='darkslategray', weight='bold', fontsize=18)
ax.set_aspect('equal')
ax.set_xlim(-30, 30)
ax.set_ylim(-60, 20)
ax.set_xticks([])
ax.set_yticks([])


# Initial Plotting
roof, = ax.plot(
    roof_x,
    roof_y,
    linewidth=5,
    color='black'
)
rod1, = ax.plot(
    [],
    [],
    color='brown',
    linewidth=4,
    linestyle='-'
)
bob1, = ax.plot(
    [],
    [],
    color='red',
    markersize=13,
    linewidth=2,
    marker='o'
)
rod2, = ax.plot(
    [],
    [],
    color='brown',
    linewidth=4,
    linestyle='-'
)
bob2, = ax.plot(
    [],
    [],
    color='green',
    marker='o',
    markersize=13,
    linewidth=2
)
trail, = ax.plot(
    [],
    [],
    color='lightgrey',
    linestyle='--',
    linewidth=3,
)


# Animation attributes
def init():
    global trail_len
    b1_x = length1*np.sin(theta1_max)
    b1_y = 10 - length1*np.cos(theta1_max)
    bob1.set_data([b1_x], [b1_y])
    
    r1_x = np.linspace(0, b1_x, 2)
    r1_y = np.linspace(10, 10 - b1_y, 2)
    rod1.set_data(r1_x, r1_y)
    
    b2_x = b1_x + length2*np.sin(theta2_max)
    b2_y = b1_y - length2*np.cos(theta2_max)
    bob2.set_data([b2_x], [b2_y])
    
    r2_x = np.linspace(b1_x, b2_x, 2)
    r2_y = np.linspace(b1_y, b2_y, 2)
    rod2.set_data(r2_x, r2_y)
    
    trail_x.append(b2_x)
    trail_y.append(b2_y)
    trail.set_data(trail_x, trail_y)

    
    return bob1, rod1, bob2, rod2, trail
def update(frame):
    global phi1
    global phi2
    global trail_x
    global trail_y
    theta1 = theta1_max*np.cos(frame + phi1)
    
    b1_x = length1*np.sin(theta1)
    b1_y = 10 - length1*np.cos(theta1)
    bob1.set_data([b1_x], [b1_y])
    
    r1_x = np.linspace(0, length1*np.sin(theta1), 3)
    r1_y = np.linspace(10, 10 - length1*np.cos(theta1), 3)
    rod1.set_data(r1_x, r1_y)
    
    
    theta2 = theta2_max*np.cos(frame + phi2)

    b2_x = b1_x + length2*np.sin(theta2)
    b2_y = b1_y - length2*np.cos(theta2)
    bob2.set_data([b2_x], [b2_y])
    
    r2_x = np.linspace(b1_x, b2_x, 2)
    r2_y = np.linspace(b1_y, b2_y, 2)
    rod2.set_data(r2_x, r2_y)
    
    
    phi1 += 0.10
    phi2 += math.sqrt(0.0200)
    trail_x.append(b2_x)
    trail_y.append(b2_y)
    trail.set_data(trail_x, trail_y)
    
    
    return bob1, rod1, bob2, rod2, trail


# Animation
ani = FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, -6*np.pi, 500),
    init_func=init,
    interval=20,
    blit=True
)





plt.show()