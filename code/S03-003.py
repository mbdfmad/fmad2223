# Exercise S03-003

# Initialize the random seed generator for reproducibility
rng = np.random.default_rng(2022) 

# number of people in the room
n = 150

# We will repeat the experiment a large number of times 
# Think of N different rooms, each with n people in it

N = 10000

max_coincidence = np.array([], dtype = np.int64)
for i in range(N):
    room = rng.integers(low = 1, high = 367, size = n)
    day, brthd_count = np.unique(room, return_counts=True)
    max_coincidence = np.append(max_coincidence, brthd_count.max())
    coincide_2 = max_coincidence > 1
    

print("With ", n, " people in the room the relative frequency of two or more birthdays \
coincidence is: ", coincide_2.mean())