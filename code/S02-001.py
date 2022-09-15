# To see the shape of the DataFrame
print("shape of the DataFrame = \n", movies.shape)

# And to select the column 'Genre' with loc for 2010 movies:
print("\nGenre for 2010 movies: \n", 
	movies.loc[movies.Year == 2010, 'Genre'])

# The type of object is:
print("\nType of a column object:\n",
	type(movies.loc[movies.Year == 2010, 'Genre']))
