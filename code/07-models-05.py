import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import scipy as scp
import seaborn as sns
import scipy.stats as stats


sns.set(rc={'figure.figsize':(16, 8.5)})

rng = np.random.default_rng(2022)
n = 100

X0 = rng.uniform(size = n)

Y1 = 3 + 2 * X0 + 0.3 * rng.normal(size = n)
Y2 = X0 * (1 - X0) + 0.01 * rng.normal(size = n)
Y3 = 2 * rng.normal(size = n)

from sklearn.linear_model import LinearRegression
modelXY = LinearRegression(fit_intercept=True)

X0 = X0[:, np.newaxis]

X0_new = np.linspace(0, 1, num= 100)
X0_new = X0_new[:, np.newaxis]

XY1_fit = modelXY.fit(X0, Y1)
Y1_new = XY1_fit.predict(X0_new)
plt.plot(X0, Y1, 'ro')
plt.plot(X0_new, Y1_new)
plt.show()


XY2_fit = modelXY.fit(X0, Y2)
Y2_new = XY2_fit.predict(X0_new)
plt.plot(X0, Y2, 'ro')
plt.plot(X0_new, Y2_new)
plt.show()

XY3_fit = modelXY.fit(X0, Y3)
Y3_new = XY3_fit.predict(X0_new)
plt.plot(X0, Y3, 'ro')
plt.plot(X0_new, Y3_new)
plt.show()

