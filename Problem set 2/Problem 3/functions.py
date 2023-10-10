import numpy as np


def euler_fwd(old, diff, h):
    return old+diff*h


def diff_eqn(omega, K, N, theta, thetas):
    theta_sum = np.sum([np.sin(thetas[j]-theta) for j in range(len(thetas))])
    return omega + (K/N)*theta_sum


def return_r(N, thetas):
    cos_sum = np.sum(np.cos(thetas))
    sin_sum = np.sum(np.sin(thetas))

    return 1/N*np.sqrt(cos_sum**2+sin_sum**2)

