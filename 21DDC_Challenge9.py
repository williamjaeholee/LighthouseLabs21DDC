"""
Challenge 9; Difficulty: Easy; Points: 5 (02/25/2021)

Day 9: pandas data cleaning & filling NaNs

Fill out the missing values in the monthly milk production column with the median, and fill out the number of cows column using the ffill method.

After filling in the missing values with our new data, answer these questions for Dot, so they can figure out the value of having a cow year-round:

What is the average for monthly milk production?
What is the standard deviation for monthly milk production?
What is the average number of cows used?

"""

# Solution

import pandas as pd
df = pd.read_csv('milk_2.csv')

milk_median = df['Monthly milk production: pounds per cow'].median()

df['Monthly milk production: pounds per cow']=df['Monthly milk production: pounds per cow'].fillna(value = milk_median)
df['Number of Cows'] = df['Number of Cows'].ffill(axis=0)
df.isnull().sum(axis=0)

# What is the average for monthly milk production?

print("Q1: " + str(round(df['Monthly milk production: pounds per cow'].mean(), 4)))

# Output

Q1: 748.0536

# What is the standard deviation for monthly milk production?

print("Q2: " + str(round(df['Monthly milk production: pounds per cow'].std(), 4)))

# Output

Q2: 93.6478

# What is the average number of cows used?

print("Q3: " + str(round(df['Number of Cows'].mean(), 4)))

# Output

Q3: 49.8988
