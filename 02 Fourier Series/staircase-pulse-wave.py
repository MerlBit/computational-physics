import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider



# Physics
N = 100
a_not = 0
t = np.linspace(-5, 15, 100)
f = np.full_like(t, a_not)
for n in range(1, N+1):
    k = 1/(n*np.pi)
    a_n = k*np.sin(n*np.pi)
    b_n = (k**2)*np.sin(n*np.pi) - k*np.cos(n*np.pi) 
    f += 2*((a_n)*(np.cos(n*np.pi*t)) + (b_n)*(np.sin(n*np.pi*t)))
    


# Plotting
fig, ax = plt.subplots(figsize=(6,3), facecolor="paleturquoise")
fig.suptitle("Staircase Pulse Wave", weight="bold")
ax.axis("equal")



# Axis
ax.spines['left'].set_position("zero")
ax.spines['bottom'].set_position("zero")
ax.spines['top'].set_color(None)
ax.spines['right'].set_color(None)
ax.set_box_aspect(1/4)
plt.subplots_adjust(bottom=0.4)

# Labellings
ax.set_xlabel("Time --> ", weight="bold")
ax.set_ylabel("Displacement --> ", weight="bold")


# Arrowheads
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)



# Slider
line, = ax.plot(t, f, color='indigo', label='Approximation')
slider_ax = plt.axes([0.2, 0.1, 0.6, 0.03])


n_slider = Slider(
    ax=slider_ax,
    label="Fourier Tick Parameter",
    valmin=0,
    valmax=50,
    valstep=1,
    valinit=N,
    track_color='pink'
)

def update(val):
    N = int(n_slider.val)
    f = np.full_like(t, a_not)
    for n in range(1, N+1):
        k = 1/(n*np.pi)
        a_n = k*np.sin(n*np.pi)
        b_n = (k**2)*np.sin(n*np.pi) - k*np.cos(n*np.pi) 
        f += 2*((a_n)*(np.cos(n*np.pi*t)) + (b_n)*(np.sin(n*np.pi*t)))
    line.set_ydata(f)
    fig.canvas.draw_idle()

n_slider.on_changed(update)
    




ax.plot(t, f, color='lightgreen') # Reference Graph Plotting
n_slider.set_val(2)

plt.show()