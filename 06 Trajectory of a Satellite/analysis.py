## Using adaptive RK45 method.
"""
We will build 4th and 5th order RK integrator. Then we compare the error with the tolerance factor and increase/decrease the 'h' as per the requirements.
It will be a continous change in h.
For small trajectories, h will be small and for large trajectories, h will be large enough because acceleration changes slowly for far off distances.
"""


# Package importing
import numpy as np
import matplotlib.pyplot as plt



# Physical Constants
G = 6.67 * 1e-11
Me = 6 * 1e24 # kg
Re = 6.4 * 1e6 # m
u = 7.95 * 1e3 # m/s

# Initial Conditions
phi = np.radians(180)
theta = np.radians(0)
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
    
    if r > 20*Re or t > 1e4 or r < Re:
        break


fig, ax = plt.subplots(
    figsize=(7, 7),
    subplot_kw={"projection": "polar"}
)
ax.set_ylim(10*Re)


earth = ax.plot(np.linspace(0, 2*np.pi, 20), np.full(20, Re))
trajectory = ax.plot(phi_list, r_list)



plt.show()