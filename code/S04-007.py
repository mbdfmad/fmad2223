## Exercise S04-007

# Let us generate a numpy (N x 2) array of normal random points (x, y) 
# in [-1, 1]x[-1, 1]
N2 = 10000
a = -1
b =  1
XY2 = np.random.default_rng(2022).normal(loc = 0, scale = 1, size = (N, 2))
n = N2
first_n = XY[0:n]

# First plot the first N2 uniform points 
fig, ax = plt.subplots()
sns.set(rc={'figure.figsize':(6, 6)})
ax.set_aspect('equal')
plt.scatter(x = XY[0:n, 0], y = XY[0:n, 1], s = 2, alpha = 0.5)
# then plot the random normal points
getPlot = plt.scatter(x = XY2[0:n, 0], y = XY2[0:n, 1], s = 2, color = "red", alpha = 0.2)

