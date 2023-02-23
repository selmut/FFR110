import numpy as np
import matplotlib.pyplot as plt
import math
import scipy as s


generations = 300
R = np.linspace(1, 30, 291)  # 291
eta = np.zeros((generations, len(R)))
alpha = 0.01
eta_0 = 900
for i in range(len(R)):
    eta[0, i] = eta_0
    # eta[1,i]=R[i]*eta_0*np.exp(-alpha*eta_0)
    for n in range(1, generations): # ska det va -1?
        eta[n, i] = R[i]*eta[n-1, i]*np.exp(-alpha*eta[n-1, i])
        '''if n>200:
             plt.scatter(R[i], eta[n])
     print(R[i])'''


# print(eta)
# plt.scatter(R[i], eta[i])


Rplot = np.zeros((300, 291))
for i in range(len(R)):
    Rplot[:, i] = R[i]
plt.xlabel("R")
plt.ylabel('\u03B7')
plt.scatter(Rplot[200:], eta[200:], 1, color='black')
plt.yscale('log')
plt.xscale('log')
# plt.xlim(20,25)
# plt.ylim(0,1000)

plt.show()


for n in range(50):
    for i in range(200, 300):
        plt.scatter(R[n], eta[i, n], 1, color='black')
    # print(n)

Rvals = [5, 10, 13, 23]
farg = ["turquoise", "black", "pink", "purple"]
tau = np.linspace(0, 40, 40)
for i in range(4):
    r = Rvals[i]
    # for t in range(41):
    plt.plot(tau, eta[:40, r*10], 6, label=('R=%.0f' % r), color=farg[i])

plt.xlabel('tau')
plt.ylabel('eta')
plt.legend()

plt.show()

fig, axs = plt.subplots(4, figsize=(8, 14))
# fig.suptitle('nån skit')

Rvals = [5, 10, 13, 23]
farg = ["turquoise", "black", "pink", "purple"]
tau = np.linspace(0, 40, 40)
for i in range(4):
    r = Rvals[i]
    # for t in range(41):
    axs[i].plot(tau, eta[:40, r*10], 6, color=farg[i])
    plt.ylabel('\u03B7')
    axs[i].set_title('R=%.0f' % r)
    axs[i].set_ylabel('\u03B7')
axs[3].set_xlabel('\u03C4')
plt.show()