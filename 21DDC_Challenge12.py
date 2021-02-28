"""
Challenge 12; Difficulty: Hard; Points: 20 (02/28/2021)

Day 12: pandas data filtering

Examining the numbers, Dot understands that the prices of both conventional and organic avocados rise and fall frequently. No matter how they grow the avocados, they don't want to sell them for less than $2.

Looking at recent years, Dot needs you to help them find: in which year or years did both conventional and organic avocados have had average prices above $2?

## SQL to pandas Converter Link: https://sql2pandas.pythonanywhere.com/ ##
## Will help understand pandas query functions for those with SQL experience ##

"""

# Solution

import pandas as pd

df = pd.read_csv('avocado.csv', index_col = 0)
df.head()

df.groupby(['year', 'type'])['AveragePrice'].max() > 2

# Output

year  type        
2015  conventional    False
      organic          True
2016  conventional     True
      organic          True
2017  conventional     True
      organic          True
2018  conventional    False
      organic          True
Name: AveragePrice, dtype: bool
            
# Answer: 2016 & 2017
