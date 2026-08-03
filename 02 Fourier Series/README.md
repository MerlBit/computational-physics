# Fourier Series Visualizer 📈

An interactive Python project that visualizes the Fourier series approximation of periodic functions.

This project was built while studying **Chapter 5 (Oscillations)** from *Classical Mechanics* by **John R. Taylor** as part of my Computational Physics learning journey.

---

## Features

- Interactive slider to control the number of Fourier terms (N)
- Real-time Fourier series reconstruction
- Original function plotted for comparison
- Smooth visualization of convergence
- Clean and responsive Matplotlib interface

---

## Implemented Waveforms

- ✅ Staircase Pulse Wave
- ✅ Diagonal (Triangular) Pulse Wave

More waveforms will be added in future updates.

---

## Physics Background

Any periodic function satisfying suitable conditions can be represented as a sum of sine and cosine functions:

\[
f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos(nx)+b_n\sin(nx)\right)
\]

The Fourier coefficients are derived analytically and then implemented computationally to reconstruct the original waveform.

This project demonstrates how increasing the number of harmonics improves the approximation.

---

## Technologies Used

- Python 3
- NumPy
- Matplotlib
- Matplotlib Widgets (Slider)

---

## Preview

### Staircase Pulse Wave

*(Insert Screenshot Here)*

---

### Diagonal Pulse Wave

*(Insert Screenshot Here)*

---

## How to Run

Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
```

Install the required libraries

```bash
pip install numpy matplotlib
```

Run any visualization

```bash
python staircase-pulse-wave.py
```

or

```bash
python diagonal-pulse-wave.py
```

---

## Future Improvements

- [ ] Square Wave
- [ ] Sawtooth Wave
- [ ] Triangle Wave
- [ ] User-defined periodic functions
- [ ] Fourier Transform visualization
- [ ] Animation mode
- [ ] Error vs Number of Fourier Terms
- [ ] Gibbs Phenomenon demonstration

---

## Motivation

Rather than only deriving equations on paper, I wanted to **see** Fourier series in action.

This project is part of my long-term goal of learning **Computational Physics** by implementing the mathematics behind classical and modern physics using Python.

Every project in this series begins with the underlying physics, followed by the mathematical derivation, and finally a computational implementation.

---

## References

- John R. Taylor — *Classical Mechanics*
- NumPy Documentation
- Matplotlib Documentation

---

⭐ If you found this project interesting, feel free to star the repository!
