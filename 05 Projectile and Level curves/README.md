# Projectile Motion Simulator 🚀

A computational physics project that simulates and visualizes projectile motion using Python.

The project combines analytical mechanics, numerical differentiation, energy and momentum analysis, and animated data visualization into a single interactive dashboard.

---

## 📌 Features

- Projectile trajectory simulation
- Position, velocity and acceleration analysis
- Momentum and energy calculations
- Numerical verification of acceleration
- Conservation of mechanical energy visualization
- Lagrangian analysis
- Animated projectile trajectory
- Animated contour maps of physical quantities
- Scientific notation formatting for large values
- Dedicated simulation dashboard with multiple plots

---

## ⚙️ Physics

For a projectile launched with initial speed \(u\) at angle \(\theta\):

### Position

\[
x(t)=u\cos\theta\,t
\]

\[
y(t)=u\sin\theta\,t-\frac{1}{2}gt^2
\]

### Velocity

\[
v_x=u\cos\theta
\]

\[
v_y=u\sin\theta-gt
\]

### Acceleration

\[
a_x=0,\qquad a_y=-g
\]

### Maximum Height

\[
H=\frac{u^2\sin^2\theta}{2g}
\]

### Range

\[
R=\frac{u^2\sin(2\theta)}{g}
\]

### Time of Flight

\[
T=\frac{2u\sin\theta}{g}
\]

### Energy

\[
K=\frac12mv^2
\]

\[
U=mgy
\]

\[
E=K+U
\]

### Lagrangian

\[
L=K-U
\]

---

## 📊 Visualizations

The simulator generates a multi-panel dashboard containing:

- **Position vs Time**
- **Velocity vs Time**
- **Acceleration vs Time**
- **Projectile Trajectory**
- **Momentum vs Time**
- **Energy vs Time**
- **Animated Projectile**
- **Animated Contour Maps**

The contour panel cycles through different physical representations, including kinetic energy, potential energy, mechanical energy, Lagrangian, and range.

---

## 🗂️ Project Structure

```text
Projectile-Motion/
│
├── main.py
├── plotting.py
├── physics.py
├── utils.py
└── README.md