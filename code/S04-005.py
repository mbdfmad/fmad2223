## Exercise S04-005

## (a)

print("-" * 30, "\n\n", "(a)\n")
print("Empirical mean from sample = ", X.mean())
print("Theoretical mean = ", (a + b)/2)

print("Empirical variance from sample = ", X.var())
print("Theoretical mean = ", (b - a)**2/12)

## (b) 
print("-" * 30, "\n\n", "(b)\n")

# Let us generate a numpy (N x 2) array of uniformly random points (x, y) 
# in [-1, 1]x[-1, 1]
N = 10000000
a = -1
b =  1
XY = np.random.default_rng(2022).uniform(low = a, high = b, size = (N, 2))
print("These are the first random points in the square:")
print(XY[0:10])

# Let us see how many of these are closer than 1 to the origin.
# XY_dist will be a boolean array with the answers to the distance condition.
XY_dist = XY[:, 0]**2 +  XY[:, 1]**2 < 1

print("Booleans to check the distance condition:")
print(XY_dist[0:10])

print("The number of points inside the circle of radius 1 is:")
print(XY_dist.sum())


# (c) Plot the first points.
print("-" * 30, "\n\n", "(c)\n")
print("See the plot below")

n = 5000
first_n = XY[0:n]
# Which are inside the circle?
first_n_in = (first_n[:, 0]**2 +  first_n[:, 1]**2 < 1)

# Use this to select them
first_dist = first_n[first_n_in]

# And now first plot all the points 
fig, ax = plt.subplots()
sns.set(rc={'figure.figsize':(6, 6)})
ax.set_aspect('equal')
plt.scatter(x = XY[0:n, 0], y = XY[0:n, 1], s = 2, alpha = 0.5)
# and then plot those inside
getPlot = plt.scatter(x = first_dist[0:n, 0], y = first_dist[0:n, 1], s = 2, color = "red")

# (d) Approximate pi
print("-" * 30, "\n\n", "(d)\n")

# The fraction of points inside the circle is the same quotient as
# (area circle) / (area square) = pi / 4
# Thus we only need to multiply that quotient times 4:
print("The approximate value of pi is:")
print(4 * XY_dist.sum() / N )
print("And that is pretty cool, right?")
