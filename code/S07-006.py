# S07-006

movies = pd.read_csv('data/movies.csv', sep=",", header=0)
movies.describe()
movies.rename(columns= {'Audience score %':'Audience', 'Rotten Tomatoes %':'Rotten'},inplace=True)
movies.describe()
movies.isna().sum()
movies_fit = sm.OLS(movies.Profitability, sm.add_constant(movies[["Audience", "Rotten"]])).fit()
movies_fit.summary()	