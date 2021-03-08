"""
Challenge 19; Difficulty: Easy; Points: 5 (03/07/2021)

Day 19: Histograms with Matplotlib

1. What type of distribution does the column avg_time have?

2. Do games that have a great avg_rating have longer play times?

Note: For question 2, filter out games that have are above the avg_rating of 9.0.

##Stretch##

As an optional bonus question, try answering:

1. What type of distribution does weight have?

2. What happens to the median and mean of a skewed distribution?

"""

# ------------------------------------------------------------------------------------------------------------------------------------

# Solution

# 1. What type of distribution does the column avg_time have?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('boardgames.csv')

plt.figure()
plt.hist(df['avg_time'], bins = 75) #Play around with the bin sizes when plotting your histogram
plt.show()

# Output

# Histogram displayed with a right-skewed distribution

# 2. Do games that have a great avg_rating have longer play times?

# Note: For question 2, filter out games that have are above the avg_rating of 9.0.

above9 = df['avg_rating'] > 9.0
above9Filtered = df[above9]

plt.figure()
plt.hist(above9Filtered['avg_time'], bins = 10, range=(0, 600)) #Play around with the bin sizes when plotting your histogram
plt.show()

# Output

# Histogram showing that the higher the average rating, the longer the average time
