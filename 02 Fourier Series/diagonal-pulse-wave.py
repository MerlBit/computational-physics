import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider



# Constants

N = 2
t = np.linspace(-4, 10, 100)
a_not = 0.5




# Fourier Series

f = np.full_like(t, a_not)
for n in range(1, N+1):
    k = 1/(np.pi * n)
    a_n = (
        (k**2) - (
            k*np.sin(n*np.pi) + (k**2)*np.cos(n*np.pi)
        )
    )
    f += 2*(a_n)*(np.cos(n*t*np.pi))

# Plotting
fig, axs = plt.subplots(figsize=(6, 3), facecolor="lightskyblue")
plt.subplots_adjust(bottom=0.25) # Room for the Slider
fig.suptitle("Diagonal Pulse Wave", weight="bold")
axs.axis('equal')

# Labellings
axs.set_xlabel("Time --> ", weight="bold")
axs.set_ylabel("Displacement --> ", weight="bold")

# Origin Axis
axs.spines['left'].set_position('zero')
axs.spines['bottom'].set_position('zero')
axs.spines['top'].set_color('none')
axs.spines['right'].set_color('none')

# Arrowheads
axs.plot(1, 0, ">k", transform=axs.get_yaxis_transform(), clip_on=False)
axs.plot(0, 1, "^k", transform=axs.get_xaxis_transform(), clip_on=False)



# Slider
line, = axs.plot(t, f, color='indigo')
slider_ax = plt.axes([0.2, 0.1, 0.6, 0.03])

n_slider = Slider(
    ax=slider_ax,
    label='Fourier Tick Parameter',
    valmin=0,
    valmax=20,
    valstep=1,
    valinit=N
)

def update(val):
    N = int(n_slider.val)
    f = np.full_like(t, a_not)
    for n in range(1, N+1):
        k = 1/(np.pi * n)
        a_n = (
            (k**2) - (
                k*np.sin(n*np.pi) + (k**2)*np.cos(n*np.pi)
            )
        )
        f += 2*(a_n)*(np.cos(n*t*np.pi))
    line.set_ydata(f)
    fig.canvas.draw_idle()

n_slider.on_changed(update)



plt.show()