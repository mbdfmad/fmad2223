import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import scipy as scp
import seaborn as sns
import scipy.stats as stats


sns.set(rc={'figure.figsize':(16, 8.5)})

XY = pd.read_csv("../data/07_simple_linear_regression_01.csv").to_numpy()
X = XY[:, 0].reshape(-1, 1)
Y = XY[:, 1]

import sklearn as sk
modelXY = sk.linear_model.LinearRegression(fit_intercept=True)
XY_fit = modelXY.fit(X, Y)
a = XY_fit.coef_[0]
b = XY_fit.intercept_

X_new = np.linspace(X.min(), X.max()).reshape(-1, 1)
Y_new = XY_fit.predict(X_new)

plt.plot(X, Y, 'ro')
plt.plot(X_new, Y_new)

