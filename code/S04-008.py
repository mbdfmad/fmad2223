## Exercise S04-008

## (a)

print("-" * 30, "\n\n", "(a)\n")

mu = 40
sigma = 3.6

a_1 = mu - sigma
b_1 = mu + sigma

a_2 = mu - 2 * sigma
b_2 = mu + 2 * sigma

a_3 = mu - 3 * sigma
b_3 = mu + 3 * sigma

print("The probability of the interval up to one sigma away from the mean is:")
print(
stats.norm.cdf(b_1, loc = mu, scale = sigma) - stats.norm.cdf(a_1, loc = mu, scale = sigma))

print("The probability of the interval up to two sigmas away from the mean is:")
print(
stats.norm.cdf(b_2, loc = mu, scale = sigma) - stats.norm.cdf(a_2, loc = mu, scale = sigma))

print("The probability of the interval up to three sigmas away from the mean is:")
print(
stats.norm.cdf(b_3, loc = mu, scale = sigma) - stats.norm.cdf(a_3, loc = mu, scale = sigma))

## (b)

print("-" * 30, "\n\n", "(b)\n")

mu = 123
sigma = 17
X = 168

Z_score = (X - mu) / sigma
print("The Z value corresponding to ", X, " from N(", mu,",", sigma, ") is:", 
      np.round(Z_score, decimals = 3))
print("Use the 68-95-99 rule to think how often you expect values like this.")

