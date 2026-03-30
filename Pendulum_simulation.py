'''
A simulation of doubled pendulum system using the solved Langrangian equations.
The simulation uses the euler method for evaluation of physical parameters.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# physics constants
g = 9.8

# simulation constants
M1 = 7
M2 = 8
R1 = 25
R2 = 35
theta1 = np.deg2rad(100)
theta2 = np.deg2rad(50)
theta1_dot = 0
theta2_dot = 0

time_stamps, dt = np.linspace(0, 300, 30000, retstep=True)

# Visualization parameters
X1 = []
Y1 = []
X2 = []
Y2 = []
# max_trail_length = 200

for t in time_stamps:
    x1 = R1*np.sin(theta1)
    y1 = -R1*np.cos(theta1)
    X1.append(x1)
    Y1.append(y1)
    X2.append(x1 + R2*np.sin(theta2))
    Y2.append(y1 - R2*np.cos(theta2))

    alpha = (M1 + M2)*R1**2
    beta = M2*R1*R2*np.cos(theta1 - theta2)
    gamma = -(M1 + M2)*g*R1*np.sin(theta1) - M2*R1*R2*theta2_dot**2*np.sin(theta1- theta2)

    eta = M2*R1*R2*np.cos(theta1- theta2)
    psi = M2*R2**2
    phi = -M2*R2*g*np.sin(theta2) + M2*R2*R1*theta1_dot**2*np.sin(theta1 - theta2)

    theta1_d_dot = (psi*gamma - beta*phi)/(psi*alpha + beta*eta)
    theta2_d_dot = (phi - eta*theta1_d_dot)/psi

    theta1_dot += theta1_d_dot*dt
    theta2_dot += theta2_d_dot*dt

    theta1 += theta1_dot*dt
    theta2 += theta2_dot*dt

   
X1 = np.array(X1)
Y1 = np.array(Y1)
X2 = np.array(X2)
Y2 = np.array(Y2)

# visualization
fig, ax = plt.subplots(figsize=(6,6))
fig.set_facecolor('black')
ax.set_facecolor('black')

# axis parameters
limit = R1 + R2 + 2
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit*2, limit/2)
ax.set_aspect('equal')

fixed_bar, = ax.plot([-limit/2, 0, limit/2], [0, 0, 0], '-o', linewidth=5, markersize=0, color='black')
rod1, = ax.plot([0, X1[0]], [0, Y1[0]], '-o', linewidth=1, markersize=2, color='#292d2dd1')
rod2, = ax.plot([X1[0], X2[0]], [Y1[0], Y2[2]], '-o', linewidth=1, markersize=2, zorder=1, color='#292d2dd1')
bob1, = ax.plot([X1[0]], [Y1[0]], '.', markersize=((M1*60)/(M1+M2)), zorder=2, color='#292d2dd1')
bob2, = ax.plot([X2[0]], [Y2[0]], '.', markersize=((M2*60)/(M1+M2)), color="#292d2dd1")
trail1, = ax.plot([], [], '-o', linewidth=1, markersize=0, color="#a0ffa8", zorder=-1)
trail2, = ax.plot([], [], '-o', linewidth=1, markersize=0, color="#bdfffd", zorder=-1)
# trail = ax.scatter([X2[0]], [Y2[0]], marker='.', s=15, facecolor='#05fac1')
# trail_history_x = []
# trail_history_y = []
# all_alpha_values = list(np.linspace(0, 1, max_trail_length))
# dynamic_alpha_values = []

# animation
def update(frame):
    # trail_history_x.append(X2[frame])
    # trail_history_y.append(Y2[frame])
    # if (len(dynamic_alpha_values) <= max_trail_length):
        # dynamic_alpha_values.append(all_alpha_values[frame])


    # if(len(trail_history_x) > max_trail_length):
    #     trail_history_x.pop(0)
    #     trail_history_y.pop(0)

    rod1.set_data([0, X1[frame]], [0, Y1[frame]])
    rod2.set_data([X1[frame], X2[frame]], [Y1[frame], Y2[frame]])
    bob1.set_data([X1[frame]], [Y1[frame]])
    bob2.set_data([X2[frame]], [Y2[frame]])
    trail1.set_data(X1[:frame], Y1[:frame])
    trail2.set_data([X2[:frame]], Y2[:frame])
    # trail.set_offsets(np.c_[trail_history_x, trail_history_y])
    # trail.set_alpha(dynamic_alpha_values)

    return rod1, bob1, rod2, bob2, trail1, trail2

ani = animation.FuncAnimation(
    fig=fig,
    frames=len(X1),
    func=update,
    interval=dt*100,
    blit=True,
    repeat=False,
)

plt.title(f'Double Pendulum')
plt.show()
