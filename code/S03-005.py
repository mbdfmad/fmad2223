# Exercise S03-005

# The theoretical probability is computed as 
# 1 - P(no repeats) = 1 - (10 · 9 · 8 · 7) / 10000)


theoretical_prob = 1 - (10 * 9 * 8 * 7) / 10000
print(theoretical_prob)
print("--"*5, "\n")

# Now we use Python to *enumerate* the elementary events (pins) with repeated digits.
pins = np.array([[a, b, c, d] for a in range(0, 10) \
        for b in range(0, 10) \
        for c in range(0, 10) \
        for d in range(0, 10)])

print("These are the first few pins:")
print(pins[0:4])
print("and these are the last ones:")
print(pins[-4:])
print("--"*5, "\n")

print("We look for the greatest frequency in each pin\n")
digits_max_freq = [np.unique(pin, return_counts=True)[1].max() for pin in pins]
print(pins[550:570])
print("\n")
print(digits_max_freq[550:570])
print("--"*5, "\n")

print("If this is bigger than one, there are repeated digits\n")
pin_has_repeats = [rpt > 1 for rpt in digits_max_freq]
print(pin_has_repeats[550:570])
print("--"*5, "\n")

print("Finally, the probability is")
np.mean(pin_has_repeats)