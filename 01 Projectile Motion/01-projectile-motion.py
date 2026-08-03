import math
import numpy as np
from matplotlib import pyplot as plt

g = 9.81 # Acceleration due to gravity (m/s^2)


def round_sig(x):
    if x == 0:
        return 0
    return round(x, -int(math.floor(math.log10(abs(x)))))  # Taking logarithmic values






def time_of_flight(u, theta_rad):
    return 2 * u * np.sin(theta_rad) / g

def maximum_height(u, theta_rad):
    return (u * np.sin(theta_rad))**2 / (2*g)

def horizontal_range(u, theta_rad):
    return ((u**2) * np.sin(2*theta_rad)) / g

def trajectory(u, theta_rad):
    T = time_of_flight(u, theta_rad)
    t = np.linspace(0, T, 100)
    x = u * np.cos(theta_rad) * t
    y = (u * np.sin(theta_rad) * t) - (0.5 * g * (t**2))
    # return (
    #     f"Time of flight: {time_of_flight(u, theta_rad):.2f} s\n"
    #     f"Horizontal range: {horizontal_range(u, theta_rad):.2f} m"  # It gets the value upto 2 decimal places
    # )
    return x, y
    

speed = float(input("Initial Speed: "))
theta = np.radians(float(input("Angle of projection: ")))

H = maximum_height(speed, theta)
R = horizontal_range(speed, theta)

print(H)
print(R)
x, y = trajectory(speed, theta)


if 2*H > R:
    # plt.figure(figsize=(H*2.01,H*1.01)) # It's about the windows size
    plt.xlim(-H*0.02, H*2.1) # Where does the graph starts?
    plt.xticks(np.arange(0, H*2.01, round_sig(H/5))) # How does grid behave
    plt.ylim(-H*0.01, H*1.1)
    plt.yticks(np.arange(0, H*1.01, round_sig(H/5)))
else:
    # plt.figure(figsize=(R*1.01,R*0.76))
    plt.xlim(-R*0.01, R*1.1)
    plt.xticks(np.arange(0, R*1.01, round_sig(R/5)))
    plt.ylim(-R*0.01, R*0.76)
    plt.yticks(np.arange(0, R*0.76, round_sig(R/5)))
    
plt.plot(x, y)
plt.gca().set_aspect("equal", adjustable="box") 


plt.xlabel("Horizontal displacement")
plt.ylabel("Vertical displacement")
plt.title("Projectile's Trajectory")
plt.grid(True)

plt.show()