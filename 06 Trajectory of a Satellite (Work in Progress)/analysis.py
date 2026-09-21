## Using adaptive RK45 method.
"""
We will build 4th and 5th order RK integrator. Then we compare the error with the tolerance factor and increase/decrease the 'h' as per the requirements.
It will be a continous change in h.
For small trajectories, h will be small and for large trajectories, h will be large enough because acceleration changes slowly for far off distances.
"""


# Package importing
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

# Physical Constants
G = 6.67 * 1e-11
Me = 6 * 1e24 # kg
Re = 6.4 * 1e6 # m
u = 10.95 * 1e3 # m/s

# Initial Conditions
phi = np.radians(37)
theta = np.radians(10)
x_0, y_0 = Re*np.cos(phi), Re*np.sin(phi)
vx, vy = u*np.sin(phi + theta), -u*np.cos(phi + theta)

# Returning state function of the Satellite
def derivatives(state):
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    ax, ay = -G*Me*x/(r**3), -G*Me*y/(r**3)
    return np.array([vx, vy, ax, ay])

# Numerical Analysis
t = 0
h = 1
x_n, y_n, vx_n, vy_n = x_0, y_0, vx, vy
r_list = [Re]
phi_list = [phi]

while True:
    state = np.array([x_n, y_n, vx_n, vy_n])
    # RK1
    k1 = derivatives(state)
    # RK2
    mid_state = state + h*k1/2
    k2 = derivatives(mid_state)
    # RK3
    mid_state = state + h*k2/2
    k3 = derivatives(mid_state)
    # RK4
    final_state = state + h*k3
    k4 = derivatives(final_state)
    k_av = (k1 + 2*k2 + 2*k3 + k4)/6
    
    # Iteration
    state += k_av*h
    x_n, y_n, vx_n, vy_n = state
    r = np.sqrt(x_n**2 + y_n**2)
    phi = np.arctan2(y_n, x_n)
    r_list.append(r)
    phi_list.append(phi)
    t += h
    print(r, phi)
    
    if r > 50*Re or t > 1e6 or r < Re:
        break


fig, ax = plt.subplots(
    figsize=(7, 7),
    subplot_kw={"projection": "polar"}
)
fig.suptitle("Satellite Trajectory")
ax.set_rlim(0, 30*Re)



# Earth image
earth = np.array(Image.open("C:\\Users\\princ\\Desktop\\Programming\\Git-Repos\\computational-physics\\06 Trajectory of a Satellite\\Assets\\Earth.png").convert("RGBA"))

# Polar grid for the Earth
N_r = 200
N_theta = 400

r_edges = np.linspace(0, Re, N_r + 1)
theta_edges = np.linspace(0, 2*np.pi, N_theta + 1)

# Centers of each polar cell
r = (r_edges[:-1] + r_edges[1:]) / 2
theta = (theta_edges[:-1] + theta_edges[1:]) / 2

R, Theta = np.meshgrid(r, theta, indexing="ij")

# Convert polar coordinates to normalized Cartesian coordinates
X = R * np.cos(Theta) / Re
Y = R * np.sin(Theta) / Re

# Convert [-1,1] -> image pixel coordinates
img_h, img_w = earth.shape[:2]

px = ((X + 1) / 2 * (img_w - 1)).astype(int)
py = ((1 - Y) / 2 * (img_h - 1)).astype(int)

# Get corresponding pixels from Earth image
earth_polar = earth[py, px]

# Plot Earth
ax.pcolormesh(
    theta_edges,
    r_edges,
    earth_polar,
    shading="flat"
)


trajectory = ax.plot(phi_list, r_list)



plt.show()