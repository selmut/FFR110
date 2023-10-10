import numpy as np
import matplotlib.pyplot as plt
from functions import *

h = 0.01
T = 10000

N = [20, 100, 300]
K = 10

x = np.linspace(-4, 4, num=101)

r = np.zeros((len(N), T))
time = np.zeros(T)

for n in range(len(N)):
    print('\nN: ', N[n])
    thetas = np.zeros((N[n], T))
    thetas[:, 0] = np.random.uniform(-np.pi / 2, np.pi / 2, size=N[n])

    r[n, 0] = return_r(N[n], thetas[:, 0])
    time[0] = 0
    omega = np.random.standard_cauchy(N[n])  # return_omega(g, x, N[n])

    for t in range(T-1):
        if t % 100 == 0:
            print('Time step: ', t)
        for i in range(N[n]):
            diff = diff_eqn(omega[i], K, N[n], thetas[i, t], thetas[:, t])
            thetas[i, t+1] = euler_fwd(thetas[i, t], diff, h)

        r[n, t+1] = return_r(N[n], thetas[:, t+1])
        time[t+1] = (t+1)*h


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(25, 5))
ax1.plot(time, r[0, :], linewidth=0.5)
ax1.title.set_text('N=20')
ax1.set_xlabel('t')
ax1.set_ylabel('r(t)')

ax2.plot(time, r[1, :], linewidth=0.5)
ax2.title.set_text('N=100')
ax2.set_xlabel('t')
ax2.set_ylabel('r(t)')

ax3.plot(time, r[2, :], linewidth=0.5)
ax3.title.set_text('N=300')
ax3.set_xlabel('t')
ax3.set_ylabel('r(t)')

plt.savefig('graphics/order_param.png', bbox_inches='tight')



