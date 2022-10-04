# S06-002.py

# Load the data and check the first lines
gear = pd.read_csv("data/GEAR.txt")
gear.head()

# Compute the required sample measures
s = gear.DIAMETER.std()
print("Sample standard deviation s =  {:.4}".format(s))
n = gear.shape[0]
print("Sample size n =  {:4d}".format(n))

# Enter the reference value sigma0 
####  Double check if it is squared!! #######
sigma0_2 = 0.000025

# Compute the chi score
chiScore = (n - 1) * s**2/sigma0_2
print("The chi square score is {:.4}".format(chiScore))

# And the p-value for this two-sided contrast
pvalue = 2 * stats.chi2.sf(chiScore, df = n -1)
print("The p-value is {:.4}".format(pvalue))