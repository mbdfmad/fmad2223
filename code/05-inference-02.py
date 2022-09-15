import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import scipy as scp
import seaborn as sns
import scipy.stats as stats

sns.set(rc={'figure.figsize':(8, 8)})

# Initialize the random number generator
rng = np.random.default_rng(2022)

# Sample size
n = 30

# Create a numpy array where each sample is a row
x = rng.normal(size = (100, n))

# Find the critical point
cl = 0.95
alpha = 1 - cl
crit_point = stats.t.isf(alpha/2, df = n - 1, loc = 0, scale = 1)

#print("Critical point for the normal = ", crit_point)

# Find the mean and standard deviation of each sample
x_means = np.apply_along_axis(func1d = np.mean, axis=1, arr=x)
x_sd = np.apply_along_axis(func1d = np.std, axis=1, arr=x)

# And the ends of the confidence intervals
ci_a = x_means - crit_point * x_sd / np.sqrt(n)
ci_b = x_means + crit_point * x_sd / np.sqrt(n)

#print("barX =", x_means[0])
#print("s =", x_sd[0])
#print(ci_a[0])
#print(ci_b[0])

# The left_end and right_end arrays are used 
# to plot the horizontal segment representing 
# each confidence interval. See the MatploLib docs
# about plotting with LineCollection
# 
left_end = np.array([ci_a, np.arange(100)]).T
right_end = np.array([ci_b, np.arange(100)]).T

segments = np.zeros((100, 2, 2))
segments[:, 0, :] = left_end
segments[:, 1, :] = right_end

# cint_ok is an array of booleans that checks if the conf. intervals
# contain the true population mean or not
cint_ok = (left_end[:, 0] < 0) & (right_end[:, 0] > 0)

# Plot the explanatory legend  over the graph.
print('The plot shows 100 confidence intervals (95% conf. level)\
 from random samples of the same population')
print('In this case ', cint_ok.sum(), " of these intervals\
 contain the true mean.")

# We use cint_ok to assign colors to the intervals
cint_colors = np.where((left_end[:, 0] < 0) & 
         (right_end[:, 0] > 0),
         "blue",
         "red")
cint_colors = [matplotlib.colors.to_rgba(col) for col in cint_colors]

# The actual plotting begins here
sns.set(rc={'figure.figsize':(20, 8)})
from matplotlib.collections import LineCollection

# LineCollection used to plot the horizontal segments corresponding to
# each confidence interval
line_segments = LineCollection(segments, linewidths=2, linestyle='solid', colors = cint_colors)
fig, ax = plt.subplots()

# The range of the axis is set
ax.set_xlim(left_end[:, 0].min()-10, right_end[:, 0].max() + 10)
ax.set_ylim(-1, 101)

ax.add_collection(line_segments)
# And we plot a vertical dashed segment representing the true mean
x1, y1 = [0, 0], [-10, 110]
plt.plot(x1, y1, "--r")
plt.yticks([]) 

plt.show()        
