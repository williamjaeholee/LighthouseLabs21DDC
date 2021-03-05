"""
Challenge 16; Difficulty: Easy; Points: 5 (03/04/2021)

Day 16: Descriptive Statistics with Boxplots

Create a boxplot to answer the following questions:

1. How many books have over 4000 pages?

Note: Do not use a filter, use a boxplot.

2. What are the average ratings for books that have over 4000 pages?

Note: You can use a filter for question 2.

"""

# ------------------------------------------------------------------------------------------------------------------------------------

# Solution

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books.csv")
df.describe()

# 1. How many books have over 4000 pages?

plt.figure()
plt.boxplot(df['num_pages'])
plt.show()

# Output: A boxplot

# Answer: the two outliers over 4000 on the boxplot.

# 2. What are the average ratings for books that have over 4000 pages?

PagesOver4000 = df['num_pages'] > 4000
PagesOver4000Filtered = df[df['num_pages'] > 4000]

PagesOver4000Filtered['average_rating']

# Output

6497    4.70
6802    4.45
Name: average_rating, dtype: float64
        
# Answer: 4.70, 4.45
