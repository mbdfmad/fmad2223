# Exercise S05-003.py

# dataURL = ""
#data = pd.read_csv("")
data0 = np.array([0.04, 0.05, 0.03, 0.06, 0.04, 0.06, 0.07, 0.03, 0.06, 0.02])
data = pd.DataFrame({'x': data0})

# Compute the necessary sample values
n = data.x.size
dof = n - 1

barX = data.x.mean()
s = data.x.std()

# Critical point computation with the Student's t:
cl = 0.95
alpha = 1 - cl
crit_point = stats.t.isf(alpha/2, df = n - 1, loc = 0, scale = 1)

# Formula for the confidence interval
conf_int = barX + np.array([-1, 1]) * crit_point * s / np.sqrt(n)
print("The confidence interval is [{:.4}, {:.4}]".format(conf_int[0], conf_int[1]))