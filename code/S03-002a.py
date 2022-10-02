# Exercise S03-002a

# Exercise S03-002a

# Initialize the random seed generator for reproducibility
rng = np.random.default_rng(2022) 

# total number of games
N = 100000

# We generate the N games as a NumPy array of N rows and 4 columns.
# Each row represents a game, each column the roll of a single dice.
game1 = rng.integers(low = 1, high = 7, size = (N, 4))


# These are the first few games
print(game1[0:10, :])
print("-" * 30, "\n")

# Next we check every dice roll to see if we got a six
game1_is_6 = (game1 == 6)
# The first part of the output of this step is
print(game1_is_6[0:10, :])
print("-" * 30, "\n")

# Now we count the number of appearances of six in each row/game
game1_number_of_6 = game1_is_6.sum(axis=1)
# Compare with the previous step to check that the count is ok
print(game1_number_of_6[0:10])
print("-" * 30, "\n")

# And now we can see if the game is win or lose (0 appearances of 6) 
game1_win = game1_number_of_6 > 0 
print(game1_win[0:10])
print("-" * 30, "\n")

# We can finally get the relative frequencies of win and lose at this game
table = np.array(np.unique(game1_win, return_counts=True))
relfreqLose = table[1, 0] / N
relfreqWin = table[1, 1] / N
print("The relative frequency of winning the first game is ", relfreqWin)
print("while 2 / 3 = ", 0.6666, " approx.")