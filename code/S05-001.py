# Exercise S05-001.py

data = pd.read_csv("data/05-Conf_Interval_LargeSample.csv")

# Compute the necessary sample values
n = data.x.size
print("Sample size = ", n)
barX = data.x.mean()
print("Sample mean = {:.4}".format(barX))
s = data.x.std()
print("Sample standard deviation = {:.4}".format(s))

# Critical point computation with the Student's t:
cl = 0.95
alpha = 1 - cl
crit_point = stats.norm.isf(alpha/2, loc = 0, scale = 1)
print("The critical point is {:.4}".format(crit_point))

# Formula for the confidence interval
conf_int = barX + np.array([-1, 1]) * crit_point * s / np.sqrt(n)
print("The confidence interval is [{:.4}, {:.4}]".format(conf_int[0], conf_int[1]))