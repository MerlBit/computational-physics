# 🌊 Quantum Wave Packet — Infinite Square Well

A Python-based visualization of a **localized quantum wave packet** constructed by superposing multiple stationary states of a one-dimensional infinite square well.

The project demonstrates how a localized quantum state can be constructed from a Gaussian distribution of energy eigenstates and visualizes both the resulting wave function and its probability distribution.

---

## 📌 Overview

In quantum mechanics, a particle confined inside a one-dimensional infinite potential well has discrete stationary states:

$$
\phi_n(x)=\sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)
$$

where:

- $L$ is the width of the well.
- $n$ is the quantum number.
- $\phi_n(x)$ is the $n$-th stationary-state eigenfunction.

A localized quantum state can be constructed by taking a superposition of these eigenstates:

$$
\Psi(x)=\sum_n c_n\phi_n(x)
$$

where $c_n$ determines the contribution of each eigenstate.

The probability density is:

$$
P(x)=|\Psi(x)|^2
$$

---

## 🧠 Wave Packet Construction

The coefficients are chosen using a Gaussian distribution centered around a selected quantum number $n_0$, together with a position-dependent sign/phase factor:

$$
c_n =
\frac{
e^{-\frac{(n-n_0)^2}{2\sigma^2}}
\sin\left(\frac{n\pi x_0}{L}\right)
}{
\sqrt{
\sum_{m=1}^{N}
e^{-\frac{(m-n_0)^2}{\sigma^2}}
\sin^2\left(\frac{m\pi x_0}{L}\right)
}
}
$$

where:

- $n_0$ → central quantum number
- $\sigma$ → width of the Gaussian distribution in quantum-number space
- $x_0$ → desired approximate position of the wave packet
- $L$ → width of the infinite potential well
- $N$ → highest quantum number included in the superposition

The normalization ensures:

$$
\sum_n |c_n|^2=1
$$

and, because the eigenfunctions are orthonormal:

$$
\int_0^L |\Psi(x)|^2\,dx=1
$$

---

## 📊 Visualization

The program generates a figure containing three main visualizations:

### 1. Wave Function

The resulting superposition:

$$
\Psi(x)=\sum_n c_n\phi_n(x)
$$

shows the localized oscillatory structure produced by the interference of multiple stationary states.

### 2. Probability Distribution

The probability density:

$$
P(x)=|\Psi(x)|^2
$$

represents the probability density of finding the particle at position $x$.

### 3. Gaussian Coefficient Distribution

The coefficients $c_n$ show the contribution of each stationary state to the wave packet.

The distribution is centered around $n_0$.

### 4. Information Panel

The visualization also displays:

- Wave-function equations
- Coefficient equation
- Current parameter values
- Number of eigenstates
- Normalization conditions

The numerical parameter values in the information panel are generated dynamically from the Python variables.

---

## ⚙️ Parameters

The main parameters can be modified directly in the Python script:

```python
L = 5

x = np.linspace(0, L, 200)
n_list = np.arange(1, 100, 1)

n0 = 35
x0 = L/2
sigma = 2