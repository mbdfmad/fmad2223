# Exercise S03-001

sns.set(rc={'figure.figsize':(8, 8)})

# Create the population
rng = np.random.default_rng(2022) # seed for reproducibility
N = 100000
x = np.concatenate((1.5 * rng.normal(loc = -2, size = N), rng.normal(loc = 0.5, size = N)))
Population2 = pd.DataFrame({'x':x})

# Plot the population density
plot0 = plt.figure(0)
plot0 = Population2.plot.density(color='orange')

# Take a large number of size 20 samples with replacement
n = 20 
n_samples = 20000 # take a large number of samples

# and compute the sample means (in a DataFrame with the mean from each sample)
sample_means = pd.DataFrame([Population2.sample(n, replace=True).mean() for item in range(n_samples)], 
                            columns=['x'])

# Now we plot the density curve for all these sample means.
plot1 = plt.figure(1)
sample_means.plot.density()
Population2.x.plot.density()
plt.axvline(x = Population2.x.mean(), linewidth = 2, linestyle='--')
getPlot = plt.xlim((-15, 10))