
# Load the data set
auto2 = pd.read_stata('data/auto2.dta')
auto2.head()

# Compute the necessary sample values
n = len(auto2["gear_ratio"])
barX = auto2["gear_ratio"].mean()
s = auto2["gear_ratio"].std()

# Critical point computation with the Student's t:
cl = 0.95
alpha = 1 - cl
crit_point = stats.t.isf(alpha/2, df = n - 1, loc = 0, scale = 1)

# Formula for the confidence interval
conf_int = barX + np.array([-1, 1]) * crit_point * s / np.sqrt(n)
print("The confidence interval is [{:.4}, {:.4}]".format(conf_int[0], conf_int[1]))