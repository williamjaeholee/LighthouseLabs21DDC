"""
Challenge 20; Difficulty: Medium; Points: 10 (03/08/2021)

Day 19: Scatterplots

Play around with the scatterplot and test out different correlations between the numerical categories in the dataset. Then, help Dot by answering these questions:

1. What kind of correlation is there between the weight and avg_rating?

2. What is the correlation coefficient between the two columns?

"""

# ------------------------------------------------------------------------------------------------------------------------------------

# Solution

# 1. What kind of correlation is there between the weight and avg_rating?

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('boardgames.csv')

plt.figure()
plt.scatter(x=df['avg_rating'].head(1500), y=df['weight'].head(1500))
plt.show()

# Output

# Scatterplot that shows positive correlation.

# 2. What is the correlation coefficient between the two columns?

print(round(df['avg_rating'].corr(df['weight']), 4))

# Output

0.5472
