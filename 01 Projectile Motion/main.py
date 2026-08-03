import physics as phys
import plotting as plott
import numpy as np

def program():
    print("Projectile Graph:")
    while True:
        try:
            speed = float(input("Enter speed ( m/s^2 ): "))
            theta = np.radians(float(input("Enter the angle of projection ( in Degrees ): ")))
            x, y, H, R = phys.trajectory(speed, theta)
            plott.trajectoryPlotting(x, y, H, R)
            break
        except ValueError:
            print(f"Enter numbers")
            continue
    
program()
