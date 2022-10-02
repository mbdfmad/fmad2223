## Exercise S04-004

print("Recall that the probability that a randomly chosen patient has prevalentHyp == 1 equals p ≈",
      np.round(p, decimals=4))
print("The X variable is a B(7,", np.round(p, decimals=4), ") binomial variable.")
print("Its theoretical table of probabilities is ")
x = np.arange(start = 0, stop = n + 1)
probs_x = stats.binom.pmf(x, n, p)
binom_probs = pd.DataFrame({"num_hypten": x.astype(int), "binomial_probs": probs_x})
print(binom_probs)
print("\n And the empirical relative frequencies that we obtained before are:")
print(relFreqs)

