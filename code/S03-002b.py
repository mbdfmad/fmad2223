# Exercise S03-002b

# Initialize the random seed generator for reproducibility
rng = np.random.default_rng(2022) 

# total number of games
N = 100000

# We generate the 24 * N games as a NumPy array of N rows and 24 columns.
# Each row represents a game, each column the roll of two dice.
# Rolling two dice results are coded from 1 to 36, with 36 is a double 6.
game2 = rng.integers(low = 1, high = 37, size = (N, 24))

# These are the first few games
print(game2[0:10, :])
print("-" * 30, "\n")

# Next we check every dice roll to see if we got a six
game2_is_36 = (game2 == 36)
# The first part of the output of this step is
print(game2_is_36[0:10, :])
print("-" * 30, "\n")

# Now we count the number of appearances of six in each row/game
game2_number_of_36 = game2_is_36.sum(axis=1)
# Compare with the previous step to check that the count is ok
print(game2_number_of_36[0:10])
print("-" * 30, "\n")

# And now we can see if the game is win or lose (0 appearances of 6) 
game2_win = game2_number_of_36 > 0 
print(game2_win[0:10])
print("-" * 30, "\n")

# We can finally get the relative frequencies of win and lose at this game
table = np.array(np.unique(game2_win, return_counts=True))
relfreqLose = table[1, 0] / N
relfreqWin = table[1, 1] / N
print("The relative frequency of winning the second game is ", relfreqWin)
print("while 2 / 3 = ", 0.6666, " approx.")