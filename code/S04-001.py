## Exercise S04-001

# Total number of dice rolls
N = 1000000

# Initialize the random number generator
rng = np.random.default_rng(2022)

# Here we generate the N dice rolls. Note that high = 7
dice = rng.integers(low = 1, high = 7, size=N )

# Let us see the first rolls of the dice
print("First rolls: ", dice[:30])

# We have seen how to do this with a pandas dataFrame. 
# But dice is a NumPy array, so we first convert it:
X = pd.DataFrame(dice, columns=["value"])

# and now we use the pandas method we know:

# absolute frequencies
AbsFreq_X = X['value'].value_counts().rename_axis('AbsFreq').sort_index()
print("\n", "--"*5, "\n")
print("Absolute frequencies:\n")
print(AbsFreq_X)

# relative frequencies
RelFreq_X = X['value'].value_counts(normalize=True).rename_axis(
    'RelFreq').sort_index()
print("\n", "--"*5, "\n")
print("Relative frequencies:\n")
print(RelFreq_X)

# If you need to use NumPy methods you can do this:
print("\n", "--"*5, "\n")
n = np.unique(dice).size
print("Number n of unique X values = ", n)

# absolute frequencies
abs_freq_np = np.array(np.unique(dice, return_counts=True)).T
print("\n", "--"*5, "\n")
print("Absolute frequencies with NumPy:\n")
print(abs_freq_np)

# relative frequencies
rel_freq_np = stats.relfreq(dice, numbins=n).frequency
print("\n", "--"*5, "\n")
print("Relative frequencies with NumPy and Scipy:\n")
print(rel_freq_np.reshape((6, 1)))

