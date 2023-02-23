import numpy as np


def ramp(xi, xi0, u0):
    return u0/(1+np.exp(xi-xi0))


def ddiff_eqn(prev, new, current):
    return new+prev-2*current


def euler_fwd(old, diff, h):
    return old+diff*h


def diff_eqn(rho, q, old, ddiff):
    return rho*old*(1-old/q)-old/(old+1)+ddiff

