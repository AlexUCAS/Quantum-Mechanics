#  The initial wave function is Ax(a-x) at infinite square wall (length a). The program shows how the absolute value of
#  wave function evolves with time

#  time part exp(-i E_n t) / h_bar = (-i n^2 pi^2 h_bar t) / (2m a^2), choose electron mass and a = 1e-10m, we have
#  period of time is (1/n^2) * 5.51e-17s

import numpy as np
from numpy import pi, power
import matplotlib.pyplot as plt
import matplotlib.animation as animation

nf = 30
fig, ax = plt.subplots()
x = np.linspace(0, 1, 101) * 1e-10
n = np.linspace(1, nf, nf)
Psi2 = np.zeros(101)
line, = ax.plot(x, Psi2 * 1e-5)
Cn = 4 * power(15, 0.5) * (1 - power(-1, n)) / (n ** 3 * pi ** 3)


def init():  # only required for blitting to give a clean slate.
    line.set_ydata(np.nan * np.ones(101))
    return line,


def animate(i):
    t = i * 2 * pi / 200
    Tfactor = np.exp(-1j * n ** 2 * t)
    nx = np.tile(x, (nf, 1)) * np.tile(n, (101, 1)).transpose()
    Eigenstate = power(2e10, 0.5) * np.sin(pi * nx * 1e10)
    CnTfactor = np.tile(Cn * Tfactor, (101, 1)).transpose()
    Psi = np.abs((Eigenstate * CnTfactor).sum(0))
    line.set_ydata(Psi * 1e-5)
    print(Psi)
    return line,


ani = animation.FuncAnimation(fig, animate, init_func=init, interval=50, blit=True)
plt.ylim(0, 1.5)
# plt.show()
writer = animation.FFMpegWriter(
    fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani.save("E:\physics\quantum mechanics\Programs\movie.mp4", writer=writer)
