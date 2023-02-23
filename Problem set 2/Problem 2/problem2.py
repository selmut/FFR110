import matplotlib.pyplot as plt

from functions import *
import numpy as np

L = 128
a = 3
b = 8
Du = 1
Dv_arr = [2.3, 3, 5, 9]
T = 1000#0
h = 0.01

ustar = a
vstar = b/a

rand = np.random.randint(0, 10, size=(L+2, L+2))*0.01
grid_u = np.ones((L+2, L+2, T))*ustar
grid_v = np.ones((L+2, L+2, T))*vstar
grid_u[:, :, 0] += rand*ustar
grid_v[:, :, 0] += +rand*vstar

for Dv in Dv_arr:
    rows, cols, time = np.shape(grid_u)
    print('\nDv: ', Dv)

    for t in range(T-1):
        if t % 100 == 0:
            print('Time step: ', t)

        for row in range(rows-1):
            for col in range(cols-1):
                ddiff_u = ddiff_eqn(grid_u[row-1, col, t], grid_u[row+1, col, t], grid_u[row, col-1, t],
                                    grid_u[row, col+1, t], grid_u[row, col, t])
                ddiff_v = ddiff_eqn(grid_v[row-1, col, t], grid_v[row+1, col, t], grid_v[row, col-1, t],
                                    grid_v[row, col+1, t], grid_v[row, col, t])

                diff_u = diff_u_eqn(a, b, grid_u[row, col, t], grid_v[row, col, t], Du, ddiff_u)
                diff_v = diff_v_eqn(b, grid_u[row, col, t], grid_v[row, col, t], Dv, ddiff_v)

                grid_u[row, col, t+1] = euler_fwd(grid_u[row, col, t], diff_u, h)
                grid_v[row, col, t+1] = euler_fwd(grid_v[row, col, t], diff_v, h)
    print('Min: ', np.min(grid_u[:128, :128, -1]))
    print('Max: ', np.max(grid_u[:128, :128, -1]))

    fig, (ax1, ax2) = plt.subplots(1, 2)
    map1 = ax1.imshow(grid_u[:128, :128, 999], cmap='summer', vmin=0, vmax=15)
    map2 = ax2.imshow(grid_u[:128, :128, -1], cmap='summer', vmin=0, vmax=15)
    fig.colorbar(map1, ax=ax1)
    fig.colorbar(map2, ax=ax2)
    ax1.title.set_text(r'$T=1000$')
    ax2.title.set_text(r'$T=10\,000$')
    fig.savefig('graphics/heatmap' + str(Dv) + '.png')



