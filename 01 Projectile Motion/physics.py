import numpy as np
import math 

# Constants:
g = 9.81 # m/s^2


# Mathematical Function:
def sig_fig(r):
    return math.floor(np.log10(r))



# Trajectory Limits:
def time_of_flight(u, theta_rad):
    return ((2 * u * np.sin(theta_rad)) / g)
def horizontal_range(u, theta_rad):
    return (((u**2) * np.sin(2*theta_rad)) / g) 
def maximum_height(u, theta_rad):
    return (((u * np.sin(theta_rad))**2) / (2 * g))

# Trajectory:
def trajectory(u, theta_rad):
    t = np.linspace(0, time_of_flight(u, theta_rad), 100)
    x = (u * np.cos(theta_rad)) * t
    y = (u * np.sin(theta_rad)) * t - (0.5 * g * (t**2))
    H = maximum_height(u, theta_rad)
    R = horizontal_range(u, theta_rad)
    return x, y, H, R
