# Exercise S05-002.py

# Recalling the code from the previous exercise:

# Load the data set
data = pd.read_csv("data/05-Conf_Interval_LargeSample.csv")

# Compute the std
s = data.x.std()
print("Sample standard deviation: {:.4}".format(s))

# Critical point computation with the Student's t:
cl = 0.95
alpha = 1 - cl
crit_point = stats.t.isf(alpha/2, df = n - 1, loc = 0, scale = 1)

# Desired precision

delta = 0.001

min_sample_size = np.ceil((crit_point * s / delta)**2) 
print("The minimum sample size is at least n = ", min_sample_size.astype(int), 
      "(but possibly bigger).")