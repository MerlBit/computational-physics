import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from physics import parse
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import MaxNLocator
from physics import pos



def sci_format(x, pos):
    if abs(x) >= 500:
        exponent = int(np.floor(np.log10(abs(x))))
        coefficient = x / 10**exponent
        return rf"${coefficient:g}\times10^{{{exponent}}}$"
    return f"{x:g}"



# Data
Q, u, g, time, mass, T, H, R, pos_x, pos_y, position_res, vel_x, vel_y, velocity, acc_x, acc_y, acc, E_kin, E_pot, E, L, momentum_x, momentum_y, p_res = parse()


# Figure and grid
fig = plt.figure(figsize=(10, 6), facecolor='paleturquoise')
fig.suptitle("Projectile Motion", weight='bold')

# Axes
gs = fig.add_gridspec(3, 9, wspace=0.6, hspace=0.5)
ax_pos = fig.add_subplot(gs[0,0:2])
ax_vel = fig.add_subplot(gs[0, 2:4])
ax_acc = fig.add_subplot(gs[0, 4:6])
ax_trajectory = fig.add_subplot(gs[1:3, 0:4])
ax_momentum = fig.add_subplot(gs[1, 4:6])
ax_sim = fig.add_subplot(gs[2, 4:6])
ax_energy = fig.add_subplot(gs[2, 6:8])
ax_contour = fig.add_subplot(gs[0:2, 6:8])


## Axes Parameters
axes = [ax_pos, ax_vel, ax_acc, ax_trajectory, ax_energy, ax_momentum, ax_sim, ax_contour]
title = ["Position vs Time", "Velocity vs Time", "Acceleration vs Time", "Trajectory of the Projectile", "Energy vs Time", "Momentum vs Time", "Trajectory", "Contour"]

# Ticks param:
for ax in axes:
    ax.tick_params(
        labelsize=8,
        length=2
    )
    ax.spines["left"].set_position(('data', 0))
    ax.spines["bottom"].set_position(('data', 0))
    ax.yaxis.set_major_formatter(FuncFormatter(sci_format))
    ax.xaxis.set_major_formatter(FuncFormatter(sci_format))

# Title param:
for i in range(len(axes)):
    axes[i].set_title(title[i])





## Plotting Curves

# Position vs time
ax_pos.plot(time, pos_x, label='x')
ax_pos.plot(time, pos_y, label='y')
ax_pos.plot(time, position_res, label='r', color='green')

# Velocity vs time
ax_vel.plot(time, vel_x, label='velocity-x')
ax_vel.plot(time, vel_y, label='velocity-y')
ax_vel.plot(time, velocity, label='speed', color='green')

# Acceleration vs time
ax_acc.plot(time, acc_x, label='acceleration-x')
ax_acc.plot(time, acc_y, label='acceleration-y')
ax_acc.plot(time, acc, label='|acceleration|', color='green')

# Trajectory
ax_trajectory.plot(pos_x, pos_y, label='Trajectory', color='magenta')
ax_trajectory.tick_params(bottom=True, left=True, labelleft=True, labelbottom=True)
if 2*H < R:
    ax_trajectory.set_xlim(-R*0.05, R*1.05)
    # ax_trajectory.set_ylim(-R*0.05, R*0.76)
elif 2*H > R:
    ax_trajectory.set_ylim(-H*0.05, H*1.05)
    # ax_trajectory.set_xlim(-2*H*0.05, 2*H*1.05)
ax_trajectory.yaxis.set_major_formatter(FuncFormatter(sci_format))
ax_trajectory.xaxis.set_major_formatter(FuncFormatter(sci_format))
ax_trajectory.yaxis.set_major_locator(MaxNLocator(5))
ax_trajectory.xaxis.set_major_locator(MaxNLocator(5))

# Spines
ax_trajectory.spines["right"].set_visible(False)
ax_trajectory.spines["top"].set_visible(False)
ax_trajectory.spines["left"].set_position(('data', 0))
ax_trajectory.spines["bottom"].set_position(('data', 0))
ax_trajectory.annotate(
    "Launch Point",
    xy=(0,0),
    xytext=(10, 10),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->"),
    color='green',
    weight='bold'
)
ax_trajectory.annotate(
    f"'H': {H:.2f} m",
    xy=(R/2, H),
    xytext=(10, 10),
    textcoords="offset points",
    arrowprops=dict(arrowstyle='->'),
    color="orange",
    weight='bold'
)
ax_trajectory.annotate(
    f"'R': {R:.2f} m",
    xy=(R, 0),
    xytext=(-100,10),
    textcoords='offset points',
    arrowprops=dict(arrowstyle='->'),
    color="red",
    weight='bold'
)

ax_trajectory.set_aspect('equal', adjustable='datalim')




# Momentum vs time
ax_momentum.plot(time, momentum_x, label='momentum-x')
ax_momentum.plot(time, momentum_y, label='momentum-y')
ax_momentum.plot(time, p_res, label='|momentum|', color='green')

# Energy vs time
ax_energy.plot(time, E_kin, label='Translational Energy - T')
ax_energy.plot(time, E_pot, label='Gravitational Energy - U')
ax_energy.plot(time, E, label='Energy - E = T + U', color='green')

# Contour
ax_contour.tick_params(
    labelleft=False,
    labelbottom=False,
    left=False,
    bottom=False
)

vx = np.linspace(0, u, 100)
vy = np.linspace(0, u, 100)
if 2*H < R:
    x = np.linspace(0, R, 100)
    y = np.linspace(0, R, 100)
elif 2*H > R:
    x = np.linspace(0, 2*H, 100)
    y = np.linspace(0, 2*H, 100)

Vx, Vy = np.meshgrid(vx, vy)
X, Y = np.meshgrid(x, y)

KE = 0.5 * mass * (Vx**2 + Vy**2)
PE = mass * g * Y

# Mechanical energy and Lagrangian use a consistent (y, v_y) state space.
vy_state = np.linspace(min(vel_y), max(vel_y), 100)
y_state = np.linspace(0, max(pos_y), 100)
Y_state, VY_state = np.meshgrid(y_state, vy_state)
vx_fixed = u * np.cos(Q)

TE = (
    0.5 * mass * (vx_fixed**2 + VY_state**2)
    + mass * g * Y_state
)

Lag = (
    0.5 * mass * (vx_fixed**2 + VY_state**2)
    - mass * g * Y_state
)

# Range map: use speed v (not v²) as the vertical coordinate.
speed_grid = np.linspace(0, u, 100)
theta = np.linspace(0, np.pi / 2, 100)
THETA, SPEED = np.meshgrid(theta, speed_grid)
rng = SPEED**2 * np.sin(2 * THETA) / g

maps = [
    ("Kinetic Energy", Vx, Vy, KE, "plasma", "velocity-X", "velocity-Y"),
    ("Potential Energy", X, Y, PE, "viridis", "position-X", "position-Y"),
    ("Mechanical Energy", Y_state, VY_state, TE, "inferno", "position-Y", "velocity-Y"),
    ("Lagrangian", Y_state, VY_state, Lag, "magma", "position-Y", "velocity-Y"),
    ("Range", THETA, SPEED, rng, "cividis", "THETA", "speed")
]

fig.text(
    0.91, 0.76,
    "CONTOUR MAPS",
    ha="center",
    va="center",
    fontsize=11,
    weight="bold"
)

fig.text(
    0.91, 0.50,
    "KINETIC ENERGY\n"
    r"$K=\frac{1}{2}m(v_x^2+v_y^2)$" "\n"
    "Axes: $v_x$ × $v_y$\n\n"

    "POTENTIAL ENERGY\n"
    r"$U=mgy$" "\n"
    "Axes: $x$ × $y$\n\n"

    "MECHANICAL ENERGY\n"
    r"$E=K+U$" "\n"
    "Axes: $y$ × $v_y$\n\n"

    "LAGRANGIAN\n"
    r"$L=K-U$" "\n"
    "Axes: $y$ × $v_y$\n\n"

    "RANGE\n"
    r"$R=\frac{v^2\sin(2\theta)}{g}$" "\n"
    "Axes: $\\theta$ × $v$",
    ha="center",
    va="center",
    fontsize=8
)

# Simulation
ax_sim.plot(pos_x, pos_y)
ax_sim.set_aspect('equal', adjustable='datalim')
if 2*H < R:
    ax_sim.set_xlim(-R*0.05, R*1.05)
    # ax_sim.set_ylim(-R*0.05, R*0.76)
elif 2*H > R:
    # ax_sim.set_xlim(-2*H*0.05, 2*H*1.05)
    ax_sim.set_ylim(-H*0.05, H*1.05)



# Animated projectile marker
traj, = ax_sim.plot(
    [],
    [],
    color="blue",
    markersize=6,
    linewidth=2,
    marker="o"
)

frames_per_map = 200       # 200 × 10 ms = 2 sec
total_frames = frames_per_map * len(maps)

contour = None

def init():
    x, y, _ = pos(0, Q)
    traj.set_data([x], [y])
    return traj,

previous_map = -1

def update(frame):
    global contour, previous_map

    # -----------------
    # Projectile
    # -----------------
    projectile_frame = frame % len(time)

    x, y, _ = pos(time[projectile_frame], Q)
    traj.set_data([x], [y])

    # -----------------
    # Contour
    # -----------------
    map_index = frame // frames_per_map

    if map_index != previous_map:

        title, X, Y, Z, co_map, xlabel, ylabel = maps[map_index]

        if contour is not None:
            contour.remove()

        contour = ax_contour.contourf(
            X, Y, Z,
            levels=20,
            cmap=co_map
        )

        ax_contour.set_title(title)
        ax_contour.set_xlabel(xlabel)
        ax_contour.set_ylabel(ylabel)
        
        ax_contour.set_xlim(X.min(), X.max())
        ax_contour.set_ylim(Y.min(), Y.max())

        previous_map = map_index
        fig.canvas.draw_idle() # Force re-draw canvas

    return traj, contour


ani = FuncAnimation(
    fig,
    update,
    frames=total_frames,
    init_func=init,
    interval=10,
    blit=True
)
