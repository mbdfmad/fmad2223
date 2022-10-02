## Exercise S04-001


# We create a NumPy array representing the table of values 
# and probabilities of X. Note the T to transpose
X = np.array([np.arange(1, 7), [1/6 for i in np.arange(0, 6)]]).T
print(X)

# Now we apply the definition of mean
mu_X = (X[:, 0] * X[:, 1]).sum()

# and of variance
var_X = ((X[:, 0] - mu_X)**2 * X[:, 1]).sum()

# Finally we print the results
print("mu_X = ", mu_X)
print("var_X = ", var_X)