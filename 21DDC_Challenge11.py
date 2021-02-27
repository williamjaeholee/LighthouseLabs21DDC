"""
Challenge 11; Difficulty: Medium; Points: 10 (02/26/2021)

Day 11: pandas group by basics

Can Dot spin a profit as an avocado farmer? Examine the data to find the average cost of avocados in Albany in 2017.

"""

# Solution

import pandas as pd

df = pd.read_csv('avocado.csv', index_col = 0)
df.head()

# groups data by 'region' and 'year' columns wih mean() aggregate function
region_year = df.groupby(['region', 'year']).mean()

# shows all data relevant to Albany 2017
region_year_loc = region_year.loc['Albany', 2017]

# shows the average cost of avocados in Albany 2017 (rounded to 4 decimals)
round(region_year_loc.loc['AveragePrice'], 4)

# Output
1.6378301886792455
