# Read the file with sep=comma and index=True
X.to_csv("data/EDA_data_saving.csv", sep=",", index=True)

# Now let us see the changes by using a terminal command
# to get the first 12 lines of the csv file.
!head -n 12 "data/EDA_data_saving.csv" 
