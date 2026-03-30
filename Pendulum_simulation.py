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
R1 = 65
R2 = 35
theta1 = np.deg2rad(100)
theta2 = np.deg2rad(110)
theta1_dot = 0
theta2_dot = 0

time_stamps, dt = np.linspace(0, 100, 10000, retstep=True)

# Visualization parameters
X1 = []
Y1 = []
X2 = []
Y2 = []
TH1 = []
TH2 = []
# max_trail_length = 200

for t in time_stamps:
    x1 = R1*np.sin(theta1)
    y1 = -R1*np.cos(theta1)
    X1.append(x1)
    Y1.append(y1)
    X2.append(x1 + R2*np.sin(theta2))
    Y2.append(y1 - R2*np.cos(theta2))
    TH1.append(theta1)
    TH2.append(theta2)

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
TH1 = np.array(TH1)
TH2 = np.array(TH2)

# visualization
fig, (ax_pendulum, ax_theta) = plt.subplots(1, 2, gridspec_kw={'wspace':0.5, 'hspace':0})
fig.set_facecolor('black')
ax_pendulum.set_facecolor('black')
ax_theta.set_facecolor('black')

# axis parameters
limit = R1 + R2 + 2
ax_pendulum.set_xlim(-limit, limit)
ax_pendulum.set_ylim(-limit, limit)
ax_pendulum.set_aspect('equal')

# theta axis parameters
theta_lim = max(np.abs(TH2)) + 5
ax_theta.set_xlim(-theta_lim, theta_lim)
ax_theta.set_ylim(-theta_lim, theta_lim)
ax_theta.set_aspect('equal')
ax_theta.tick_params(axis='x', color="#545c5cd1")
ax_theta.tick_params(axis='y', color='#545c5cd1')
ax_theta.tick_params(labelcolor='#545c5cd1')
ax_theta.grid(True, color='#545c5cd1')
ax_theta.set_xlabel("Theta_1", color='#545c5cd1')
ax_theta.set_ylabel("Theta_2", color='#545c5cd1')

fixed_bar, = ax_pendulum.plot([-limit/2, 0, limit/2], [0, 0, 0], '-o', linewidth=5, markersize=0, color='black')
rod1, = ax_pendulum.plot([0, X1[0]], [0, Y1[0]], '-o', linewidth=1, markersize=2, color='#292d2dd1')
rod2, = ax_pendulum.plot([X1[0], X2[0]], [Y1[0], Y2[2]], '-o', linewidth=1, markersize=2, zorder=1, color='#292d2dd1')
bob1, = ax_pendulum.plot([X1[0]], [Y1[0]], '.', markersize=((M1*60)/(M1+M2)), zorder=2, color='#292d2dd1')
bob2, = ax_pendulum.plot([X2[0]], [Y2[0]], '.', markersize=((M2*60)/(M1+M2)), color="#292d2dd1")
trail1, = ax_pendulum.plot([], [], '-o', linewidth=1, markersize=0, color="#a0ffa8", zorder=-1)
trail2, = ax_pendulum.plot([], [], '-o', linewidth=1, markersize=0, color="#bdfffd", zorder=-1)
# trail = ax_pendulum.scatter([X2[0]], [Y2[0]], marker='.', s=15, facecolor='#05fac1')
# trail_history_x = []
# trail_history_y = []
# all_alpha_values = list(np.linspace(0, 1, max_trail_length))
# dynamic_alpha_values = []

# theta1, theta2 plot
thetas, = ax_theta.plot([], [], '-o', linewidth=2, markersize=0)

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

    thetas.set_data(TH1[:frame], TH2[:frame])

    return rod1, bob1, rod2, bob2, trail1, trail2, thetas

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
