import matplotlib.pyplot as plt
import numpy as np
from functions import *

delay_steps = 50
time_steps = 500
h = 0.1
T_arr = np.linspace(0.1, 5, num=delay_steps)
t_arr = np.linspace(0, 49, num=time_steps)
A = 20
K = 100
r = 0.1
N0 = 50


all_sols = np.zeros((delay_steps, time_steps))

for i in range(delay_steps):
    N = np.zeros(time_steps)

    for j in range(time_steps):
        T = T_arr[i]
        t = t_arr[j]

        if t-T <= 0:
            N[j] = N0
        else:
            diff = allee(r, N, i, j, K, A)
            N[j] = eulerFWD(N[j-1], diff, h)

    all_sols[i] = N

plt.plot(t_arr, all_sols[30])
plt.show()

