import numpy as np
from utils import resultant


# Parameters
mass = 2.0       # kg
g = 9.81          # m/s^2
u = 2000.0       # m/s
Q = np.radians(33)  # launch angle
N = 200

# Analytical trajectory results
T = (2 * u * np.sin(Q)) / g
H = (u * np.sin(Q))**2 / (2 * g)
R = (u**2 * np.sin(2 * Q)) / g

# Time step for numerical differentiation
t = 0.0
DEL_T = float(T / N)

# Data storage
pos_x, pos_y, position_res = [], [], []
vel_x, vel_y, velocity = [], [], []
acc_x, acc_y, acc = [], [], []
E_kin, E_pot, E, L = [], [], [], []
momentum_x, momentum_y, p_res = [], [], []
time = []


def pos(t, Q):
    """Return x-position, y-position and radial position at time t."""
    x = float(u * np.cos(Q) * t)
    y = float(u * np.sin(Q) * t - 0.5 * g * t**2)
    r = resultant(x, y)
    return x, y, r


def vel(t, Q):
    """Return x-velocity, y-velocity and speed at time t."""
    v_x = float(u * np.cos(Q))
    v_y = float(u * np.sin(Q) - g * t)
    speed = resultant(v_x, v_y)
    return v_x, v_y, speed


def acceleration(z):
    """Numerically differentiate velocity to obtain acceleration."""
    vx_f, vy_f, _ = vel(z + DEL_T, Q)
    vx_i, vy_i, _ = vel(z, Q)
    a_x = (vx_f - vx_i) / DEL_T
    a_y = (vy_f - vy_i) / DEL_T
    a = resultant(a_x, a_y)
    return a_x, a_y, a


def energy(vel_x, vel_y, pos_y):
    """Return kinetic and gravitational potential energy."""
    kin = 0.5 * mass * resultant(vel_x, vel_y)**2
    pot = mass * g * pos_y
    return kin, pot


def momentum(vel_x, vel_y):
    """Return x-momentum, y-momentum and momentum magnitude."""
    p_x = mass * vel_x
    p_y = mass * vel_y
    p = resultant(p_x, p_y)
    return p_x, p_y, p


# Numerical analysis
for _ in range(N + 1):
    time.append(t)

    x, y, r = pos(t, Q)
    pos_x.append(x)
    pos_y.append(y)
    position_res.append(r)

    v_x, v_y, speed = vel(t, Q)
    vel_x.append(v_x)
    vel_y.append(v_y)
    velocity.append(speed)

    a_x, a_y, a = acceleration(t)
    acc_x.append(a_x)
    acc_y.append(a_y)
    acc.append(a)

    kin, pot = energy(v_x, v_y, y)
    E_kin.append(kin)
    E_pot.append(pot)
    E.append(kin + pot)
    L.append(kin - pot)

    p_x, p_y, p = momentum(v_x, v_y)
    momentum_x.append(p_x)
    momentum_y.append(p_y)
    p_res.append(p)

    t += DEL_T


def parse():
    """Return all simulation parameters and calculated data."""
    return (
        Q, u, g, time, mass, T, H, R,
        pos_x, pos_y, position_res,
        vel_x, vel_y, velocity,
        acc_x, acc_y, acc,
        E_kin, E_pot, E, L,
        momentum_x, momentum_y, p_res
    )


if __name__ == "__main__":
    print(f"Time of Flight: {T}")
    print(f"Maximum Height achieved: {H}")
    print(f"Transverse Range of Motion: {R}")
    print(f"Maximum Potential Energy: {mass * g * H}")
    print(f"Maximum Kinetic Energy: {E_kin[0]}")
