import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from functions import *

r = 0.1
K = 10**3
b = 1

tol = 1
h = 1
time_steps = 200
N2star = K*r**(1/b)
N01 = [1, 2, 3, 10]
N02 = [N2star-10, N2star-3, N2star-2, N2star-1, N2star+1, N2star+2, N2star+3, N2star+10]

sols = np.zeros((len(N01), time_steps))
sols2 = np.zeros((len(N02), time_steps))
times = np.zeros((len(N01), time_steps))
times2 = np.zeros((len(N02), time_steps))
approx_sols = np.zeros((len(N01), time_steps))
approx_sols2 = np.zeros((len(N02), time_steps))

# --- 2d --------------------------------------------------------------------------------------------------------------

for n in range(len(N01)):
    for t in range(time_steps):
        if t == 0:
            sols[n, t] = N01[n]
            approx_sols[n, t] = N01[n]
            times[n, t] = 0

        else:
            diff = ((r+1)*sols[n, t-1])/(1+(sols[n, t-1]/K)**b)
            approx_diff = (r + 1) * approx_sols[n, t - 1]

            sols[n, t] = ((r+1)*sols[n, t-1])/(1+(sols[n, t-1]/K)**b)
            approx_sols[n, t] = (r + 1) * approx_sols[n, t - 1]
            times[n, t] = t


times = np.log2(times)
sols = np.log2(sols)
approx_sols = np.log2(approx_sols)


# all
fig = plt.figure()
ax = plt.subplot()
ax.plot(times[0], sols[0], c='tab:blue', linestyle='-')
ax.plot(times[1], sols[1], c='tab:orange', linestyle='-')
ax.plot(times[2], sols[2], c='tab:green', linestyle='-')
ax.plot(times[3], sols[3], c='tab:red', linestyle='-')
ax.plot(times[0], approx_sols[0], c='tab:blue', linestyle='--')
ax.plot(times[1], approx_sols[1], c='tab:orange', linestyle='--')
ax.plot(times[2], approx_sols[2], c='tab:green', linestyle='--')
ax.plot(times[3], approx_sols[3], c='tab:red', linestyle='--')
ax.plot(times[3], np.log2(np.ones(time_steps)+0.001), 'k--')


box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.7, box.height])
plt.legend([r'Exact, $N_0=1$', r'Exact, $N_0=2$', r'Exact, $N_0=3$', r'Exact, $N_0=10$', r'Linearised, $N_0=1$',
            r'Linearised, $N_0=2$', r'Linearised, $N_0=3$', r'Linearised, $N_0=10$', r'Steady-state $N_1^*$'],
          loc='center left', bbox_to_anchor=(1, 0.5), fontsize='small')
ax.set_xlabel(r'log$(t)$')
ax.set_ylabel(r'log$(N_t)$')


plt.xlabel(r'log$(t)$')
plt.ylabel(r'log$(N_t)$')
plt.savefig('graphics/saved_img/all.png')
plt.close()


# --- 2f --------------------------------------------------------------------------------------------------------------
for n in range(len(N02)):
    for t in range(time_steps):
        if t == 0:
            sols2[n, t] = N02[n]
            approx_sols2[n, t] = N02[n]
            times2[n, t] = 0

        else:
            sols2[n, t] = ((r+1)*sols2[n, t-1])/(1+(sols2[n, t-1]/K)**b)
            approx_sols2[n, t] = (r * (1 - b) + 1) / (r + 1) * (approx_sols2[n, t - 1]-N2star)+N2star
            times2[n, t] = t

times2 = np.log2(times2)
sols2 = np.log2(sols2)
approx_sols2 = np.log2(approx_sols2)

# all
fig = plt.figure()
ax = plt.subplot()

ax.plot(times2[0], sols2[0], c='tab:blue', linestyle='-')
ax.plot(times2[1], sols2[1], c='tab:orange', linestyle='-')
ax.plot(times2[2], sols2[2], c='tab:red', linestyle='-')
ax.plot(times2[3], sols2[3], c='tab:green', linestyle='-')
ax.plot(times2[3], sols2[4], c='tab:olive', linestyle='-')
ax.plot(times2[3], sols2[5], c='tab:purple', linestyle='-')
ax.plot(times2[3], sols2[6], c='tab:pink', linestyle='-')
ax.plot(times2[3], sols2[7], c='tab:cyan', linestyle='-')

ax.plot(times2[0], approx_sols2[0], c='tab:blue', linestyle='--')
ax.plot(times2[1], approx_sols2[1], c='tab:orange', linestyle='--')
ax.plot(times2[2], approx_sols2[2], c='tab:red', linestyle='--')
ax.plot(times2[3], approx_sols2[3], c='tab:green', linestyle='--')
ax.plot(times2[3], approx_sols2[4], c='tab:olive', linestyle='--')
ax.plot(times2[3], approx_sols2[5], c='tab:purple', linestyle='--')
ax.plot(times2[3], approx_sols2[6], c='tab:pink', linestyle='--')
ax.plot(times2[3], approx_sols2[7], c='tab:cyan', linestyle='--')

ax.plot(times2[3], np.log2(np.ones(time_steps)*K*r**(1/b)), 'k--')

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.7, box.height])
ax.legend([r'Exact, $N_0=-10$', r'Exact, $N_0=-3$', r'Exact, $N_0=-2$', r'Exact, $N_0=-1$', r'Exact, $N_0=1$',
            r'Exact, $N_0=2$', r'Exact, $N_0=3$', r'Exact, $N_0=10$', r'Linearised, $N_0=-10$', r'Linearised, $N_0=-3$',
            r'Linearised, $N_0=-2$', r'Linearised, $N_0=-1$', r'Linearised, $N_0=1$', r'Linearised, $N_0=2$',
            r'Linearised, $N_0=3$', r'Linearised, $N_0=10$', r'Steady-state $N_2^*$'],
          loc='center left', bbox_to_anchor=(1, 0.5), fontsize='small')
ax.set_xlabel(r'log$(t)$')
ax.set_ylabel(r'log$(N_t)$')

plt.savefig('graphics/saved_img/all2.png')
