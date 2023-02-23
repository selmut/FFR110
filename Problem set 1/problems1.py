import numpy as np
import matplotlib.pyplot as plt

A = 20
K = 100
r = 0.1
N_0 = 50
T = 1.1
T_arr = np.linspace(0.1, 5, num=50)
dt = 0.01
totalTime = 500

t = []
Ndot = []

nTimesteps = int(totalTime / dt)
N = np.empty(nTimesteps)

for i in range(nTimesteps):
    N[i] = N_0
    t.append(i * dt)

Tind = int(T/dt)

for i in range(nTimesteps-1):
    NdotTemp = r * N[i] * (1 - N[i-Tind] / K) * (N[i] / A - 1)
    Ndot.append(NdotTemp)
    N[i+1] = (NdotTemp*dt+N[i])


fig = plt.figure()
plt.plot(t, N)
plt.xlabel("t")
plt.ylabel("N")
plt.title("T=%.1f" % T)
plt.savefig('graphics/saved_img/oscillations_T'+str(T)+'.png')


NCut = N[:len(N)-Tind]
NTCut = N[Tind:]

fig = plt.figure()
plt.plot(NTCut, NCut)
plt.xlabel("N(t-T)")
plt.ylabel("N(t)")
plt.title("T=%.1f" % T)
plt.savefig('graphics/saved_img/cycle_T'+str(T)+'.png')


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))
fig.suptitle("T=%.1f" % T)

ax1.plot(t, N)
ax1.set_xlabel('t')
ax1.set_ylabel('N')
ax2.set_xlabel("N(t-T)")
ax2.set_ylabel("N(t)")
ax2.plot(NTCut, NCut)




