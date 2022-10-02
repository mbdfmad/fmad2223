## Exercise S04-003


# (a) Import the framingham data set
framingham_url = "https://raw.githubusercontent.com/mbdfmad/fmad2122/main/data/framingham.csv"
framingham = pd.read_csv(framingham_url)
framingham.columns

# (b) Compute the probability
p = framingham['prevalentHyp'].value_counts(normalize=True)[1]
print("(b) The probability that a randomly chosen patient has prevalentHyp == 1 equals p = ", p)

# (c) The X variable is a B(7, p) binomial variable, taking all the values from 0 to 7

# (d) To make a sample we use:
n = 7
prevalentHyp_sample = framingham['prevalentHyp'].sample(n, replace=True, random_state=2022)

print("-" * 50, "\n")
print("(c) A seven sample is of prevalentHyp values is: ")
print(prevalentHyp_sample)
print("The number of hypertensive patients in the sample is (the sum):")
print(prevalentHyp_sample.sum())

# (e) Now we iterate this process using the size parameter:
N = 50000
np_prevHyp = np.array(framingham['prevalentHyp'])

rng = np.random.default_rng(seed = 2022)
X_samples = rng.choice(np_prevHyp, size = (N, 7), replace = True)

print("-" * 50, "\n")
print("The first elements in X_samples are (a sample per row)")
print(X_samples[0:12])

print("and the number of hypertensive patients in each sample is")
num_hyp_X_sample = X_samples.sum(axis = 1)
print(num_hyp_X_sample)

print("The relative frequencies of each possible number of hypertensive patients is")
num_hyp_X_sample_pd =  pd.DataFrame(num_hyp_X_sample, columns=["numb_hypten"])
relFreqs = num_hyp_X_sample_pd.value_counts(normalize = True).sort_index()
print(relFreqs)

# (f) Plot the relative frequencies.
print("-" * 50, "\n")
print("(f) The bar plot of the relative frequencies is:")
sns.set()
fig, ax = plt.subplots(1, 1)
num_hyp_X_sample_pd.value_counts(normalize = True).sort_index().plot.bar(
    rot=0, 
    xlabel='Number of hypertensive patients in sample', 
    ylabel ='Relative Frequency')
getPlot = plt.xticks(np.arange(8), np.arange(8)) 