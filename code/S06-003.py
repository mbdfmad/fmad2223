# S06-003.py

data = np.array(np.random.default_rng(2022).normal(loc = 0, scale = 1, size = (50, 20, 10000)))

def ttest_pvalue(sample, mu0, sl, hyp):
    Tscore, pValue = stats.ttest_1samp(sample, 
                                   popmean=popmean,
                                   alternative="greater")

Tscores, pValues = stats.ttest_1samp(data, popmean = 0, axis = 0, alternative='two-sided')

counts, freqs = np.unique(np.sum(pValues < 0.05, axis=0), return_counts=True)

width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(counts - width/2, freqs/10000, width, label='Simulation')
rects2 = ax.bar(np.arange(8) + width/2, stats.binom.pmf(np.arange(8), 20, 0.05), width, label='Binomial')
ax.set_title('Relative frequencies of number of type I errors vs binomial predicted probabilities')
ax.legend()