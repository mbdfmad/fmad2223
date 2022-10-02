## Exercise S04-009

## (a)

np.random.seed(2022)
N = 3000

# Let us generate both normal samples
mu1 = -3
sigma1 = 1
X1 = stats.norm(loc = mu1, scale = sigma1).rvs(size = N)

mu2 = 2
sigma2 = 1/2022
X2 = stats.norm(loc = mu2, scale = sigma2).rvs(size = N)


## (b)
print("-" * 30, "\n\n", "(b)\n")

# As they are NumPy arrays the combination is simple:
X3 = 3 * X1 + 4 * X2

mu3 = 3 * mu1 + 4 * mu2
sigma3 = np.sqrt(3**2 * sigma1 **2 + 4**2 * sigma2 **2)
print("The theoretical parameters of the linear combination X3 are:")
print("mu3 = ", mu3)
print("sigma3 = ", sigma3)

## (c)
print("-" * 30, "\n\n", "(b)\n")

print(" The empirical sample of the linear combination has ")
print("mean = ", X3.mean())
print("standard deviation = ", X3.std())

## (d)
print("-" * 30, "\n\n", "(d)\n")

print("See pictures below")
# We can plot the empirical density curve of X3  with
fig, ax = plt.subplots(1, 1)
sns.kdeplot(X3, linewidth=2, color = "red")

# And then we add the theoretical density to the plot using pdf and plotting
# the values of pdf for a set of nodes across the range of the variable
x = np.linspace(-10, 10, 200)
ax.plot(x, stats.norm(loc = mu3, scale = sigma3).pdf(x), lw=5, color = "blue", alpha = 0.3)
plt.xlim(left=-10, right=10)
getPlot = ax.set_title("(d) Empirical density in red, theoretical in blue")

## (e)
print("-" * 30, "\n\n", "(e)\n")

fig, ax = plt.subplots(1, 1)

# The mixture can be easily obtained with hstack
X4 = np.concatenate((X1, X2))
# And the plot of the mixture density is
sns.kdeplot(X4, linewidth=2, color = "red")
getPlot = ax.set_title("Empirical density of the mixture of normals")

