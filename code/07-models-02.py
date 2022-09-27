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

X = np.concatenate((X0, X0, X0))
Y = np.concatenate((Y1, Y2, Y3))

F = np.repeat(['Y1', 'Y2', 'Y3'], repeats=[n, n, n])

XY = pd.DataFrame({'X' : X, 'Y' : Y, 'F' : F})

g = sns.relplot(data=XY, x="X", y="Y", col="F", kind="scatter", facet_kws=dict(sharey=False))

for (row_key, col_key),ax in g.axes_dict.items():
    ax.set_title(f"Y{col_key}")

plt.show()

X0Y1 = pd.DataFrame({'X' : X0, 'Y' : Y1})
X0Y2 = pd.DataFrame({'X' : X0, 'Y' : Y2})
X0Y3 = pd.DataFrame({'X' : X0, 'Y' : Y3})

X0Y1.to_csv("./data/07_simple_linear_regression_01.csv", index=False)
X0Y2.to_csv("./data/07_simple_linear_regression_02.csv", index=False)
X0Y3.to_csv("./data/07_simple_linear_regression_03.csv", index=False)
