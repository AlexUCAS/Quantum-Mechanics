   import numpy as np
import matplotlib.pyplot as plt
# Helmholtz free energy of N distinguishable H-O of w, F=-NkT ln(kT/h_bar w)
# entropy, S=Nk(1+ln(kT/h_bar w))
# kT = np.array([1e-2, 0.1, 0.3, 0.5, 0.7, 1, 1.5])  # in the unit of h_bar w
# N = 10
# h_barw = 3  # unit eV
# F = -N * kT * h_barw * np.log(kT)
# k = 1.38e-23
# S = N * k * (1 + np.log(kT))
# plt.plot(kT, S, 'ro')
# plt.xscale('log')
# plt.show()

# # limit of x^(100)e^(-x^(-2)) as x to 0
# x = np.logspace(-30, -18, 30)
# # y = -100 * np.log(x) - (1 / x**2)
# y = x * np.log(x)
# plt.plot(x, y)
# # plt.xscale('log')
# plt.show()

# SSP HW01 Q3 surface plasmon, q**2 c**2 vs w**2, the unit of x- and y-axis is omega_p and omega_p**2 respectively

# import math
# omega1 = np.linspace(0.4, 0.7, 100)
# omega2 = np.linspace(0.72, 50, 100)
# omega = np.append(omega1, [np.linspace(0.7, 0.72, 100), omega2]) # omiga is 'this' times of omega_p
# epsilon = 1 - 1 / omega**2
# q2c2 = omega ** 2 * epsilon / (1 + epsilon)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# # plt.plot(omega, q2c2, 'ro')
# ax.plot(omega, q2c2)
# ax.set_xscale('log')
# # ax.set_xticks(np.arange(0.7, 0.72, step=0.01))
# ax.set_xlabel(r'$\omega /\omega _p$')
# ax.set_ylabel(r'$q^2c^2/\omega _p$')
# ax.title.set_text(r'$q^2c^2$'' vs 'r'$\omega$'' (from 'r'$0.4\omega_p$'' to 'r'$50\omega_p$'')')
# plt.savefig('D:\CMP\HW1Q3_1.jpg')
# fig.clear('True')
# ax = fig.add_subplot(111)
# omega = np.linspace(0.7, 0.72, 100)
# epsilon = 1 - 1 / omega**2
# q2c2 = omega ** 2 * epsilon / (1 + epsilon)
# ax.plot(omega, q2c2)
# ax.set_xlabel(r'$\omega /\omega _p$')
# ax.set_ylabel(r'$q^2c^2/\omega _p$')
# ax.title.set_text('close-up around 'r'$0.71\omega_p$')
# # plt.show()
# plt.savefig('D:\CMP\HW1Q3_2.jpg')

# SSP HW01Q2 y-axis is in sigma_0 unit

# omega_ctau = 1

# fig = plt.figure(figsize=(10, 5))
# ax = fig.add_subplot(121)
# ax1 = fig.add_subplot(122)
# ax.set_xscale('log')
# ax.set_xlabel(r'$\omega \tau$')
# ax.set_ylabel(r'$Re(\sigma_{xx}) /\sigma_0$')
# ax1.set_xscale('log')
# ax1.set_xlabel(r'$\omega \tau$')
# ax1.set_ylabel(r'$Im(\sigma_{xx}) /\sigma_0$')
#
# # def plot(omega_ctau): # plot sigma_xx
# #     omegatau = np.logspace(-4, 4, 100)
# #     sigmaxx = (1 - 1j * omegatau) / ((1 - 1j * omegatau) ** 2 + omega_ctau ** 2)
# #     ax.plot(omegatau, np.real(sigmaxx), label=r'$\omega_c\tau=$' +str(omega_ctau))
# #     ax1.plot(omegatau, np.imag(sigmaxx), label=r'$\omega_c\tau=$' +str(omega_ctau))
# #     ax.legend()
# #     ax1.legend()
# #     return 0
# def plot(omega_ctau): # plot sigma_xy
#     omegatau = np.logspace(-4, 4, 100)
#     sigmaxy = -omega_ctau / ((1 - 1j * omegatau) ** 2 + omega_ctau ** 2)
#     ax.plot(omegatau, np.real(sigmaxy), label=r'$\omega_c\tau=$' +str(omega_ctau))
#     ax1.plot(omegatau, np.imag(sigmaxy), label=r'$\omega_c\tau=$' +str(omega_ctau))
#     ax.legend()
#     ax1.legend()
#     return 0
# plot(1)
# plot(0.1)
# plot(10)
# fig.suptitle('real and imaginary parts of 'r'$\sigma_{xy}$'' for different 'r'$\omega_c \tau$'' values with fixed 'r'$\tau$')
# # plt.show()
#
# plt.savefig('D:\CMP\HW1Q2_xy.jpg')

# CMP HW03Q2 energy plots along fcc [111] up to six time of the lowest energy at L point

# all the possible reciprocal vectros
# k_r_set = np.array([[0, 0, 0], [1, 1, 1], [-1, -1, -1], [1, 1, -1], [-1, -1, 1], [2, 0, 0], [-2, 0, 0]])
# k = np.linspace(-1, 1, 100)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# for i in k_r_set:
#     e = ((k + 2 * i[0]) ** 2 + (k + 2 * i[1]) ** 2 + (k + 2 * i[2]) ** 2) / 3
#     ax.plot(k, e, c='b')
# ax.set_xlim([-1, 1])
# ax.set_ylim([0, 6])
# ax.set_xlabel(r'Bloch wave vector $k$ along [111] direction', fontsize=11)
# ax.set_ylabel(r'$\epsilon \cdot \frac{2ma^2}{3\pi^2 \hbar^2}$', fontsize=15)
# ax.annotate(r'$\Gamma$', xy=(0.516, 0.127), xycoords='figure fraction', fontsize=17)
# ax.annotate('L', xy=(0.879, 0.127), xycoords='figure fraction', fontsize=17)
# ax.annotate('(L)', xy=(0.126, 0.127), xycoords='figure fraction', fontsize=17)
# plt.savefig('D:\CMP\HW3Q2.jpg')
# plt.show()

# CMP HW0303 plots B.Z.s for 2d square lattice
# kx = np.linspace(-4, 4, 100)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# x = np.linspace(-4, 4, 5)
# y = np.linspace(-4, 4, 5)
# xx, yy = np.meshgrid(x, y)
# ax.plot(xx, yy, 'ko')
# print(xx)
# print(yy)
# for i in x:
#     for j in y:
#         if i == 0 and j ==0:
#             print('reached the origin')
#         else:
#             if j==0:
#                 ax.plot(i * np.ones(100) / 2, kx, c='b')
#             if i==0:
#                 ax.plot(kx, j * np.ones(100) / 2, c='b')
#             if i!=0 and j!=0:
#                 ax.plot(kx, j / 2 - (kx - i / 2) * i / j, c='b')
#                 print('i=', i)
#                 print('j=', j)
# ax.set_ylim([-2.5, 2.5])
# ax.set_xlim([-2.5, 2.5])
# x_f = 1.2 * np.linspace(-1, 1, 100)
# ax.plot(x_f, np.sqrt(1.2**2 - x_f**2), 'g')
# ax.plot(x_f, - np.sqrt(1.2**2 - x_f**2), 'g')
# # plt.show()
# plt.savefig('D:\CMP\HW3Q3_4.jpg')

# # CMP Midterm_1 Q1 Fermi surface and reciprocal rectangular lattice vector
# kx = np.linspace(-2, 2, 100)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# x = np.linspace(-2, 2, 5)
# y = np.linspace(-2, 2, 5) / np.sqrt(2)
# xx, yy = np.meshgrid(x, y)
# ax.plot(xx, yy, 'ko')
# print(xx)
# print(yy)
# for i in x:
#     for j in y:
#         if i == 0 and j ==0:
#             print('reached the origin')
#         else:
#             if j==0:
#                 ax.plot(i * np.ones(100) / 2, kx, c='b')
#                 print('i=', i, 'j=', j)
#             if i==0:
#                 ax.plot(kx, j * np.ones(100) / 2, c='b')
#             if i!=0 and j!=0:
#                 ax.plot(kx, j / 2 - (kx - i / 2) * i / j, c='b')
#                 # print('i=', i)
#                 # print('j=', j)
# ax.set_ylim([-0.6, 0.6])
# ax.set_xlim([-0.75, 0.75])
# k_f = 1 / (np.power(2, 1/4) * np.sqrt(np.pi))
# x_f = k_f * np.linspace(-1, 1, 100)
# ax.plot(x_f, np.sqrt(k_f**2 - x_f**2), 'g')
# ax.plot(x_f, - np.sqrt(k_f**2 - x_f**2), 'g')
# ax.set_xlabel(r'$\frac{a}{2\pi}k_x$')
# ax.set_ylabel(r'$\frac{a}{2\pi}k_y$')
# ax.annotate(r'$k_x=\frac{\pi}{a}$' + '\n' + r'$k_y=\frac{-\pi}{\sqrt{2}a}$', xy=(0.782, 0.175), xycoords='figure fraction', fontsize=13)
# ax.annotate(r'$k_x=\frac{-\pi}{a}$' + '\n' + r'$k_y=\frac{-\pi}{\sqrt{2}a}$', xy=(0.137, 0.175), xycoords='figure fraction', fontsize=13)
# ax.annotate(r'$k_x=\frac{-\pi}{a}$' + '\n' + r'$k_y=\frac{\pi}{\sqrt{2}a}$', xy=(0.137, 0.758), xycoords='figure fraction', fontsize=13)
# ax.annotate(r'$k_x=\frac{\pi}{a}$' + '\n' + r'$k_y=\frac{\pi}{\sqrt{2}a}$', xy=(0.782, 0.758), xycoords='figure fraction', fontsize=13)
# # plt.show()
# plt.savefig('D:\CMP\mid1_Q1.jpg')

# # CMP bonus HW tight binding on graphene
# x1 = np.linspace(0, 1, 100)
# e1 = np.sqrt(3 + 2 * np.cos(4 * np.pi * x1 / 3) + 4 * np.cos(2 * np.pi * x1 / 3)) # Gamma-K
# x2 = np.linspace(-1, 0, 100)
# e2 = np.sqrt(3 + 2 * np.cos(4 * np.pi * x2 / 3) + 4 * np.cos(2 * np.pi * x2 / 3)) # K-Gamma
# x3 = np.linspace(0, 1, 100)
# e3 = np.sqrt(5 + 4 * np.cos(np.pi * x3))
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# # Gamma-K
# ax.plot(x1, e1, c='b')
# ax.plot(x1, -e1, c='b')
# # K-Gamma
# ax.plot(x1+1, e2, c='b')
# ax.plot(x1+1, -e2, c='b')
# # Gamma-M
# ax.plot(x1+2, e3, c='b')
# ax.plot(x1+2, -e3, c='b')
# ax.tick_params(axis='x', which='both', labelbottom=False)
# ax.set_xticks([1, 2])
# ax.set_xlim([0, 3])
# ax.annotate(r'$\Gamma$', xy=(0.12, 0.053), xycoords='figure fraction', fontsize=18)
# ax.annotate(r'$K(K^{\prime})$', xy=(0.35, 0.053), xycoords='figure fraction', fontsize=18)
# ax.annotate(r'$\Gamma$', xy=(0.63, 0.053), xycoords='figure fraction', fontsize=18)
# ax.annotate(r'$M$', xy=(0.88, 0.053), xycoords='figure fraction', fontsize=18)
# ax.set_ylabel(r'$\frac{\epsilon}{\gamma}$', fontsize=22, rotation=0)
# # plt.show()
# plt.savefig('D:\CMP\Bonus1D.jpg')

# # 2D disersion
# from mpl_toolkits import mplot3d
# x = np.linspace(-1, 1, 100)
# y = np.linspace(-1, 1, 100)
# xx, yy = np.meshgrid(x, y)
# theta1 = 4 * np.pi * (np.sqrt(3) * xx + yy) / (3 * np.sqrt(3)) # a1 dot k
# theta2 = 4 * np.pi * (np.sqrt(3) * xx - yy) / (3 * np.sqrt(3)) # a2 dot k
# theta3 = 8 * np.pi * yy / (3 * np.sqrt(3)) # (a1 - a2) dot k
# e = np.sqrt(3 + 2 * np.cos(theta1) + 2 * np.cos(theta2) + 2 * np.cos(theta3))
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.plot_surface(xx, yy, e)
# ax.plot_surface(xx, yy, -e)
# ax.set_xlabel(r'$\frac{9a}{8\pi}k_x$', fontsize=15)
# ax.set_ylabel(r'$\frac{9a}{8\pi}k_y$', fontsize=15, labelpad=10)
# ax.set_zlabel(r'$\frac{\epsilon}{\gamma}$', fontsize=26)
# # ax.yaxis._axinfo['label']['space factor'] = -5
# ax.xaxis.set_rotate_label(False)
# ax.yaxis.set_rotate_label(False)
# ax.zaxis.set_rotate_label(False)
# # plt.show()
# plt.savefig('D:\CMP\Bonus2D.jpg')

# CMP HW04Q2 period of DOS of 2d Landau level with k_z free electron
# chaning w_c, fix E
E = 1000
g_e_vector = np.ones(10000)
h_barw_vector = np.linspace(0.806, 0.81, 10000)
ratio_vector = E / h_barw_vector
for i in range(10000):
    ratio = ratio_vector[i]
    niu = np.arange(0, np.floor(ratio - 0.5) + 1, 1)
    g_e_vector[i] = (h_barw_vector[i] / np.sqrt(E - h_barw_vector[i] * (niu + 0.5))).sum()
    # g_e_vector[i] = (1 / np.sqrt(E - h_barw_vector[i] * (niu + 0.5))).sum()

# ratio_vector = np.linspace(1001, 1010, 1000)
# h_barw = 1
# E = ratio_vector * h_barw
# g_e_vector = np.ones(len(ratio_vector))
# for i in range(len(ratio_vector)):
#     ratio = ratio_vector[i]
#     niu = np.arange(0, np.floor(ratio - 0.5) + 1, 1)
#     g_e_vector[i] = (h_barw / np.sqrt(E[i] - h_barw * (niu + 0.5))).sum()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(ratio_vector, g_e_vector)
ax.set_xlabel(r'$\frac{E}{\hbar\omega}$', fontsize=15, labelpad=-2)
# ax.set_xlim([1001, 1010])
ax.set_ylabel(r'$g(E)\frac{\sqrt{2}\pi^2\hbar^3}{m^{\frac{3}{2}}}(\sqrt{meV})$', fontsize=18, labelpad=-2)
plt.grid()
# plt.show()
plt.savefig('D:\CMP\HW04Q2supp.jpg')





