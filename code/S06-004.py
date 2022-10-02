# S06-004.py

m = 20
counts_bonf, freqs_bonf = np.unique(np.sum(pValues < 0.05 / m, axis=0), return_counts=True)
print(counts_bonf)
print(freqs_bonf)
print(freqs_bonf / 10000)