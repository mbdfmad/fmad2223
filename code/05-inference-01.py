import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as scp
import seaborn as sns

#sns.set(rc={'figure.figsize':(12, 8.5)})
sns.set()

# Initialize the random number generator
rng = np.random.default_rng(2022)


x = rng.normal(size = (20, 30))

x_mins = np.array([np.apply_along_axis(func1d = np.min, axis=1, arr=x), np.arange(20)]).T
x_maxs = np.array([np.apply_along_axis(func1d = np.max, axis=1, arr=x), np.arange(20)]).T
x_means = np.array([np.apply_along_axis(func1d = np.mean, axis=1, arr=x), np.arange(20)]).T
#print(x_means)

x_ranges = np.zeros((20, 2, 2))
x_ranges[:, 0, :] = x_mins
x_ranges[:, 1, :] = x_maxs
#print(x_ranges)
#print(x_ranges[:, :, 0])

x_points = np.zeros((600, 2))

x_points[:, 0] = x.flatten()
x_points[:, 1] = np.repeat(np.arange(20), 30)
x_points

sns.set(rc={'figure.figsize':(20, 8)})
from matplotlib.collections import LineCollection
line_segments = LineCollection(x_ranges, linewidths=2, linestyle='solid')
fig, ax = plt.subplots()
ax.set_xlim(x_mins[:, 0].min()-1, x_maxs[:, 0].max() + 1)
ax.set_ylim(-1, 21)
ax.add_collection(line_segments)
ax.set_title('The plot shows 20 random samples from the same population')
plt.scatter(x = x_points[:,0], y=x_points[:, 1], marker="D", c="blue", s=25)
plt.scatter(x = x_means[:,0], y=x_means[:, 1], marker="x", c="red", s=100)
x1, y1 = [0, 0], [-1, 21]
plt.plot(x1, y1, "--r")
plt.yticks(range(20)) 
plt.show()        
x_points[:, 0].mean()
