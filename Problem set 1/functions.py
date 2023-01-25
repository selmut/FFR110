import numpy as np
import matplotlib.pyplot as plt
import glob
import os


def eulerFWD(old, diff, h):
    return old + diff * h


def allee(r, N, i, j, K, A):
    return r*N[j-1]*(1-N[j-1-i]/K)*(N[j-1]/A-1)


def clear_dir(directory):
    files = glob.glob(directory+'/*.png')
    for f in files:
        os.remove(f)
