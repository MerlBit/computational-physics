### Creating a Definite Energy Quantum Wave Function



# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt



# Constants
L = 5

# Physical Variables
x = np.linspace(0, L, 200)
n_list = np.arange(1, 100, 1)

# Guassian Distribution
n0 = 24
x0 = L/2
sigma = 5
coefficients = (
    np.exp(-(n_list-n0)**2/(2*sigma**2))
    * np.sin(n_list*np.pi*x0/L)
)
coefficients /= np.sqrt(np.sum(coefficients**2))




# Defining the wave
waves = []
y = np.zeros(len(x))

# Superimposing the waves
for n, c in zip(n_list, coefficients):
    # c = np.exp(-(n - n0)**2 / (2*sigma**2))
    wave = c * np.sqrt(2/L) * np.sin(n*np.pi*x/L)
    y += wave
    waves.append(wave)




# Defining the figure and axes
fig = plt.figure(figsize=(10, 6), facecolor="#ccccff")
# ax1 = fig.add_subplot((), facecolor="#c4ddc2")
msc = [
    ['Wave Function', 'Wave Function', 'Info'],
    ['Probability Distribution Curve', 'Probability Distribution Curve', 'Coefficient']
]
axs = fig.subplot_mosaic(msc)
axs['Wave Function'].sharex(
    axs['Probability Distribution Curve']
)





## Formating the axes 'Wave Function'
font1 = {'family':'serif','color':"#6440c8",'size':20}
font2 = {'family':'serif','color':'darkred','size':15}

# Labelling
axs['Wave Function'].set_title("Definite-Energy Quantum Wave Function", fontdict=font1)
axs['Wave Function'].set_xlabel("x-Position", fontdict=font2, size=10)
axs['Wave Function'].xaxis.set_label_coords(0.5, 0.05)
axs['Wave Function'].set_ylabel("Wave Function", fontdict=font2)
axs['Wave Function'].yaxis.set_label_coords(-0.02, 0.5)
axs['Wave Function'].set_facecolor('#faebd7')

# Spines/Axis
axs['Wave Function'].spines['left'].set_position(('data', 0.0))
axs['Wave Function'].spines['bottom'].set_position(('data', 0.0))
axs['Wave Function'].spines['top'].set_color('none')
axs['Wave Function'].spines['right'].set_color('none')

# Ticks/Range of Axis
axs['Wave Function'].tick_params(
    axis='x',
    which='both',
    bottom=False,
    labelbottom=False
)
axs['Wave Function'].set_aspect('equal', adjustable='datalim')

# Plotting
axs['Wave Function'].plot(x, y, label='position of particle', color='#0e2f44')



## Formatiing the axes 'Probibility Distribution Curve'
# Labelling
axs['Probability Distribution Curve'].set_title("Probabilistic Distribution Curve", fontdict=font1)
axs['Probability Distribution Curve'].set_xlabel("x-Position", fontdict=font2, size=10)
axs['Probability Distribution Curve'].xaxis.set_label_coords(0.5, -0.04)
axs['Probability Distribution Curve'].set_ylabel("Probabilistic Function", fontdict=font2)
axs['Probability Distribution Curve'].yaxis.set_label_coords(-0.02, 0.5)
axs['Probability Distribution Curve'].set_facecolor('#faebd7')

# Spines/Axis
axs['Probability Distribution Curve'].spines['left'].set_position(('data', 0.0))
axs['Probability Distribution Curve'].spines['bottom'].set_position(('data', 0.0))
axs['Probability Distribution Curve'].spines['top'].set_color('none')
axs['Probability Distribution Curve'].spines['right'].set_color('none')

# Ticks/Range of Axis
axs['Probability Distribution Curve'].set_xlim(-2, L + 2)
axs['Probability Distribution Curve'].set_xticks(np.arange(2, L, int(L/5)))
axs['Probability Distribution Curve'].set_aspect('equal', adjustable='datalim')

# Plotting
axs['Probability Distribution Curve'].plot(x, y**2)





## Formatting the axes 'Coefficient'
# Labelling
axs['Coefficient'].set_title(f"Guassian Coefficient - \n 'Centered at {n0}'", fontdict=font1, size=12)
axs['Coefficient'].set_xlabel("nth Wave", fontdict=font2, size=10)
axs['Coefficient'].xaxis.set_label_coords(0.5, -0.1)
axs['Coefficient'].set_ylabel("Coefficient", fontdict=font2, size=12)
axs['Coefficient'].yaxis.set_label_coords(-0.09, 0.5)
axs['Coefficient'].set_facecolor('#faebd7')

# Spines/Axis
axs['Coefficient'].spines['left'].set_position(('data', 0.0))
axs['Coefficient'].spines['bottom'].set_position(('data', 0.0))
axs['Coefficient'].spines['top'].set_color('none')
axs['Coefficient'].spines['right'].set_color('none')

# Ticks/Range of Axis
axs['Coefficient'].set_xlim(-2, len(n_list) + 2)
axs['Coefficient'].tick_params(
    axis='y',
    labelsize=4
)





## Writting down the info of the function

# Left Column
info_left = (
    r"$\mathbf{Wave\ Function}$" "\n\n"
    r"$\phi_n(x)=\sqrt{\frac{2}{L}}"
    r"\sin\left(\frac{n\pi x}{L}\right)$" "\n\n"
    r"$\Psi(x)=\sum_n c_n\phi_n(x)$" "\n\n"
    r"$P(x)=|\Psi(x)|^2$"
)

axs['Info'].text(
    0.04, 0.95,
    info_left,
    transform=axs['Info'].transAxes,
    fontsize=8.5,
    color="#fee83f",
    va='top',
    ha='left'
)


# Right Column
n_max = n_list[-1]

coefficient_formula = (
    r"$c_n=\frac{"
    r"e^{-\frac{(n-n_0)^2}{2\sigma^2}}"
    r"\sin\left(\frac{n\pi x_0}{L}\right)"
    r"}{"
    r"\sqrt{\sum_{m=1}^{" + str(n_max) + r"}"
    r"e^{-\frac{(m-n_0)^2}{\sigma^2}}"
    r"\sin^2\left(\frac{m\pi x_0}{L}\right)"
    r"}}$"
)

info_right = (
    r"$\mathbf{Coefficient}$" "\n\n"
    + coefficient_formula + "\n\n"
    r"$\mathbf{Parameters}$" "\n"
    + rf"$L={L}$" + "\n"
    + rf"$x_0={x0:.2f}$" + "\n"
    + rf"$n_0={n0},\quad \sigma={sigma}$" + "\n"
    + rf"$n=1,\ldots,{n_max}$" + "\n\n"
    r"$\sum_n|c_n|^2=1$" "\n"
    r"$\int_0^L|\Psi(x)|^2dx=1$"
)

axs['Info'].text(
    0.52, 0.95,
    info_right,
    transform=axs['Info'].transAxes,
    fontsize=7.5,
    color='#fee83f',
    va='top',
    ha='left'
)


# Info Formatting
axs['Info'].set_xticks([])
axs['Info'].set_yticks([])

for spine in axs['Info'].spines.values():
    spine.set_color('none')

axs['Info'].set_facecolor("#000000")

# Plotting
axs['Coefficient'].plot(n_list, coefficients)


plt.show()