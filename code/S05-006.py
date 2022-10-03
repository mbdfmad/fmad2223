# S05-006

# Load the data set
auto2 = pd.read_stata('data/auto2.dta')
auto2.head()

# Compute the necessary sample values
n = len(auto2["gear_ratio"])
s = auto2["gear_ratio"].std()

# Critical point computation with the Student's t:
cl = 0.95
alpha = 1 - cl
crit_point_left = stats.chi2.isf(alpha/2, df = n - 1)
crit_point_right = stats.chi2.ppf(alpha/2, df = n - 1)

# Formula for the confidence interval
conf_int = (n - 1) * s**2 / np.array([crit_point_left, crit_point_right])
print("The confidence interval is [{:.4}, {:.4}]".format(conf_int[0], conf_int[1]))