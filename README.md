# Pendulum Simulation

A simple double-pendulum physics simulation and animation implemented in Python.

This repository contains a single script that numerically integrates the Lagrangian equations for a double pendulum and renders an animated visualization using Matplotlib.

**Contents**
- `Pendulum_simulation.py` — main simulation script (animation produced in a Matplotlib window).
- `LICENSE` — MIT License.

## Features

- Numerical simulation of a double pendulum using an explicit Euler integrator.
- Real-time Matplotlib animation showing rods, bobs, and trails.
- Easy-to-edit simulation parameters (masses, lengths, initial angles, timesteps).

## Requirements

- Python 3.8+
- numpy
- matplotlib

Install the Python dependencies (recommended inside a virtual environment):

```bash
python -m venv .venv
source .venv/bin/activate    # on Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install numpy matplotlib
```

You can also create a `requirements.txt` with:

```
numpy
matplotlib
```

and install with `pip install -r requirements.txt`.

## Usage

Run the simulation from the project root:

```bash
python Pendulum_simulation.py
```

This opens a Matplotlib window that plays the animation. Close the window to stop the program.

### Adjusting simulation parameters

Open `Pendulum_simulation.py` and edit the variables near the top of the file to change the simulation:

- `M1`, `M2` — masses of the two bobs
- `R1`, `R2` — rod lengths
- `theta1`, `theta2` — initial angles (radians or use `np.deg2rad()`)
- `time_stamps` / `dt` — total simulation time and timestep

Increasing the number of timesteps makes the simulation smoother but slower. The script currently uses an explicit Euler integrator; for long simulations you may want to switch to a more stable integrator (e.g., Runge–Kutta) for accuracy.


## License

See the `LICENSE` file for license details.

---

Enjoy experimenting with the double pendulum! If you'd like, I can:

- add a `requirements.txt` file, or
- add command-line arguments and save the animated output to MP4/GIF.

Send me which option you'd like next.