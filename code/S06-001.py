# S06-001.py

mpg_link = "https://raw.githubusercontent.com/tidyverse/ggplot2/main/data-raw/mpg.csv"
mpg = pd.read_csv(mpg_link)

Tscore, pValue = stats.ttest_1samp(mpg.cty, 
                                   popmean=16,
                                   alternative="greater")

print("The sample size is {:3d}".format(len(mpg)))
print("The sample mean is {:.4}".format(mpg.cty.mean()))
print("The T score is {:.4}".format(Tscore))
print("And the corresponding p-value is {:.4}".format(pValue))