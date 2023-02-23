import matplotlib.pyplot as plt
from functions import *

rho = 0.5
q = 8
L = 100

u1_star = -(1-q)/2+np.sqrt((1-q)**2/4-q*(1/rho-1))
u2_star = -(1-q)/2-np.sqrt((1-q)**2/4-q*(1/rho-1))

T = 1000
h = 0.001

xi_arr = np.linspace(0, L, num=L+1)
xi0_arr = np.array([20, 50, 50])
u0_arr = np.array([u1_star, u2_star, 1.1*u2_star])

sols = np.zeros((len(xi0_arr), len(xi_arr), T))
diffs = np.zeros((len(xi0_arr), len(xi_arr), T))
times = np.zeros(T)

for i in range(len(xi0_arr)):
    xi0 = xi0_arr[i]
    u0 = u0_arr[i]

    initial_sol = np.zeros(T)
    initial_diff = np.zeros(T)
    initial_sol[0] = ramp(0, xi0, u0)

    # compute initial val for xi=0
    for t in range(T-1):
        diff = diff_eqn(rho, q, initial_sol[t], 0)

        initial_diff[t+1] = diff
        initial_sol[t+1] = euler_fwd(initial_sol[t], diff, h)

    sols[i, 0, :] = initial_sol
    diffs[i, 0, :] = initial_diff

    initial_size = ramp(xi_arr[1:], xi0, u0)
    sols[i, 1:, 0] = initial_size

    times[0] = 0
    for t in range(T-1):
        for j in range(len(xi_arr)-2):
            xi_idx = j + 1
            ddiff = ddiff_eqn(sols[i, xi_idx-1, t], sols[i, xi_idx+1, t], sols[i, xi_idx, t])
            diff = diff_eqn(rho, q, sols[i, xi_idx-1, t], ddiff)

            sols[i, xi_idx, t+1] = euler_fwd(sols[i, xi_idx-1, t], diff, h)
            diffs[i, xi_idx, t+1] = diff
            times[t+1] = (t+1)*h


sol1 = sols[0, :, :]
sol2 = sols[1, :, :]
sol3 = sols[2, :, :]

diff1 = diffs[0, :, :]
diff2 = diffs[1, :, :]
diff3 = diffs[2, :, :]


# 1
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# left panel
ax1.plot(xi_arr, sol1[:, 10], c='tab:blue')
ax1.plot(xi_arr, sol1[:, 20], c='tab:blue')
ax1.plot(xi_arr, sol1[:, 30], c='tab:blue')

ax1.set_xlabel(r'$\xi$')
ax1.set_ylabel(r'$u(\xi)$')

# right panel
for t in range(T):
    ax2.plot(sol1[:, t], diff1[:, t], c='tab:blue', lw=0.5)

ax2.plot(u1_star, 0, 'ko')
ax2.plot(0, 0, 'ko')

ax2.set_xlabel(r'$u(\xi)$')
ax2.set_ylabel(r'$\frac{du(\xi,\,\tau)}{d\xi}$')
fig.savefig('graphics/travelling_waves1.png')

# 2
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# left panel
ax1.plot(xi_arr, sol2[:, 10], c='tab:orange')
ax1.plot(xi_arr, sol2[:, 20], c='tab:orange')
ax1.plot(xi_arr, sol2[:, 30], c='tab:orange')

ax1.set_xlabel(r'$\xi$')
ax1.set_ylabel(r'$u(\xi)$')

# right panel
for t in range(T):
    ax2.plot(sol2[:, t], diff1[:, t], c='tab:orange', lw=0.5)

ax2.plot(u2_star, 0, 'ko')
ax2.plot(0, 0, 'ko')

ax2.set_xlabel(r'$u(\xi)$')
ax2.set_ylabel(r'$\frac{du(\xi,\,\tau)}{d\xi}$')
fig.savefig('graphics/travelling_waves2.png')

# 3
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# left panel
ax1.plot(xi_arr, sol3[:, 10], c='tab:red')
ax1.plot(xi_arr, sol3[:, 20], c='tab:red')
ax1.plot(xi_arr, sol3[:, 30], c='tab:red')

ax1.set_xlabel(r'$\xi$')
ax1.set_ylabel(r'$u(\xi)$')

# right panel
for t in range(T):
    ax2.plot(sol3[:, t], diff1[:, t], c='tab:red', lw=0.5)

ax2.plot(u2_star*1.1, 0, 'ko')
ax2.plot(0, 0, 'ko')

ax2.set_xlabel(r'$u(\xi)$')
ax2.set_ylabel(r'$\frac{du(\xi,\,\tau)}{d\xi}$')
fig.savefig('graphics/travelling_waves3.png')

print(diffs)
