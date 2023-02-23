import matplotlib.pyplot as plt
import numpy as np
from functions import *

delay_steps = 50
time_steps = 5000
T_arr = np.linspace(0.1, 5, num=delay_steps)
t_arr = np.linspace(0, time_steps, num=time_steps)
h = 0.1
A = 20
K = 100
r = 0.1
N0 = 50

all_sols = np.zeros((delay_steps, time_steps))

for i in range(delay_steps):
    N = np.zeros(time_steps)

    for j in range(0, time_steps):
        T = T_arr[i]
        t = t_arr[j]

        if t-T <= 0:
            N[j] = N0
        else:
            diff = allee(r, N, i, j, K, A)
            N[j] = eulerFWD(N[j-1], diff, h)

    all_sols[i] = N


clear_dir('graphics/img')
for T in range(delay_steps):
    plt.figure()
    plt.plot(t_arr[100:1000], all_sols[T, 100:1000])
    plt.xlabel('t')
    plt.ylabel('N(t)')
    plt.title('T='+str(round(T_arr[T], 2)))
    plt.savefig('graphics/img/T'+str(round(T_arr[T], 2))+'.png')
    plt.close()


'''clear_dir('graphics/img')
for T in range(delay_steps):
    plt.figure()
    plt.plot(all_sols[T, T+100:time_steps], all_sols[T, 100:(time_steps-T)])
    plt.xlabel('N(t)')
    plt.ylabel('N(t-T)')
    plt.title('T='+str(round(T_arr[T], 2)))
    plt.savefig('graphics/img/T'+str(round(T_arr[T], 2))+'.png')
    plt.close()'''



