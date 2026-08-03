from matplotlib import pyplot as plt
import numpy as np
import physics as phys


def trajectoryPlotting(x, y, H, R):
    plt.plot(x, y)
    plt.gca().set_aspect("equal", adjustable="box")
    
    # Essentials:
    plt.title("Trajectory of a Projectile")
    plt.xlabel("Horizontal displacement")
    plt.ylabel("Vertical displacement")

    # Graph & Windows
    plt.grid(True)
    z = 2*H
    if z > R:
        plt.xlim(-z*0.05, z*1.1)
        plt.ylim(-H*0.05, H*1.1)
        plt.xticks(np.arange(0, z*1.1, (10**(phys.sig_fig(z*1.1)))))
        plt.yticks(np.arange(0, z*1.1, (10**(phys.sig_fig(z*1.1)))))
    elif 0 < z < R:
        plt.xlim(-R*0.05, R*1.1)
        plt.ylim(-R*0.05, R*0.76)
        plt.xticks(np.arange(0, R*1.1, (10**(phys.sig_fig(R*1.1)))))
        plt.yticks(np.arange(0, R*1.1, (10**(phys.sig_fig(R*1.1)))))
    else:
        print("\n\n\n\n\nLoL\n\n\n\n\n")
        

    plt.show()
