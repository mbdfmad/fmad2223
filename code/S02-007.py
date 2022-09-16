# The (sorted) table of cumulative relative frequencies is:
cumRelFreq = train_accidents['CarsDer'].value_counts(
	normalize = True).sort_index()
# And the one corresponding to 10 is:
print(cumRelFreq[10])
