import numpy as np
import pandas as pd

alpha = 20
beta = 10

r0 = alpha/beta
N = 100
n0 = N*(1-beta/alpha)

dt = 0.01
T_max = 10

nRuns = 500  # 2000

times = np.linspace(0, int(T_max/dt), num=int(T_max/dt)+1)*dt
n = np.zeros((nRuns, int(T_max/dt)))
n[:, 0] = n0

for m in range(nRuns):
    idx_old = 0
    t = 0

    if m % 100 == 0:
        print(f'Run nr: {m}')

    while t < T_max-1:
        bn = alpha * n[m, idx_old] * (1 - n[m, idx_old] / N)
        dn = beta * n[m, idx_old]

        if bn == 0:
            tb = 0
        else:
            tb = np.random.exponential(1/bn)
        if dn == 0:
            td = 0
        else:
            td = np.random.exponential(1/dn)

        t += np.minimum(tb, td)
        idx = int(np.floor(t/dt))

        n[m, idx_old:idx] = n[m, idx_old]

        if tb > td:
            n[m, idx] = n[m, idx_old] + 1
        else:
            n[m, idx] = n[m, idx_old] - 1

        idx_old = np.copy(idx)




pd.DataFrame(n).to_csv('n_data.csv', header=False, index=False)
pd.DataFrame(times).to_csv('times.csv', header=False, index=False)
