import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n_df = pd.read_csv('n_data.csv')
times_df = pd.read_csv('times.csv')

n = n_df.to_numpy()
times = times_df.to_numpy()

plt.figure()
plt.plot(times, n[100, :])
plt.show()
