import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import scipy as scp
import seaborn as sns
import scipy.stats as stats
import sklearn as sk

sns.set(rc={'figure.figsize':(16, 8.5)})

XY = pd.read_csv("../data/07_simple_linear_regression_01.csv")
X = XY.X.values.reshape(len(XY), 1)
Y = XY.Y.values

from sklearn.linear_model import LinearRegression
modelXY = LinearRegression(fit_intercept=True)
XY_fit = modelXY.fit(X, Y)

b1 = XY_fit.coef_[0]
b0 = XY_fit.intercept_


print("The regression line is y = {:.6} + {:.6} x".format(b0, b1))

X_new = np.linspace(X.min(), X.max()).reshape(-1, 1)
Y_new = XY_fit.predict(X_new)

plt.plot(X, Y, 'ro')
plt.plot(X_new, Y_new)