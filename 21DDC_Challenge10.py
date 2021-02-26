"""
Challenge 10; Difficulty: Easy; Points: 5 (02/26/2021)

Day 10: pandas Data Modification

Help Dot figure out how profitable selling fresh milk can be, by looking at the dataset for the cow farm. Fill in the values for the following columns based on the available data:

1. Total Milk Production
2. Total Revenue

How much revenue did the cow farm make in the year 2020?

"""

# Solution

# The code below will results in the 'Total Milk Production' and 'Total Revenue' columns being filled with the appropriate values

import pandas as pd

df = pd.read_csv('milk_32.csv')

df['Total Milk Production'] = df['Monthly milk production: pounds per cow'] * df['Number of Cows']
df['Total Revenue'] = df['Total Milk Production'] * df['Price_Per_Pound']

df.tail(n=20)

# The code below will result in printing the monthly revenue of the year 2020 followed by the total revenue of 2020 from selling milk

Twenty20 = df['Total Revenue'][155:167]
print(Twenty20)

count = 0
sum = 0
for i in Twenty20:
    sum += i
    count += 1
print(sum)

# Output

155    16129.92
156    16546.56
157    15514.88
158    17697.28
159    17915.52
160    19165.44
161    18590.08
162    17776.64
163    17022.72
164    14989.12
165    14989.12
166    15812.48
Name: Total Revenue, dtype: float64
202149.76
