# Exercise S03-004

# Initialize the random seed generator for reproducibility
rng = np.random.default_rng(2022) 

# We will choose a large number of values x in [0, 1] 

N = 100000

x = rng.random(size = N)
print(x[0:20])
print("-" * 30, "\n")

# Is x in the interval [1/3, 2/3]
x_in_A = (x >= 1/3) & (x <= 2/3)
print(x_in_A[0:20])
print("-" * 30, "\n")

# And to find the relative frequency of booleans we take the mean:
print("The relative frequency (or proportion) of x between 1/3 and 2/3 is ",  x_in_A.mean())