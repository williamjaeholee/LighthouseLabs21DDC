"""
Challenge 10; Difficulty: Easy; Points: 5 (02/26/2021)

Day 10: pandas Data Modification

Help Dot figure out how profitable selling fresh milk can be, by looking at the dataset for the cow farm. Fill in the values for the following columns based on the available data:

1. Total Milk Production
2. Total Revenue

How much revenue did the cow farm make in the year 2020?

"""

# ------------------------------------------------------------------------------------------------------------------------------------

# Solution

import pandas as pd

# reads csv file 'milk_32.csv'
df = pd.read_csv('milk_32.csv')

# fills 'Total Milk Production column' with the product of the 'Monthly milk production: pounds per cow' and 'Number of Cows' columns
df['Total Milk Production'] = df['Monthly milk production: pounds per cow'] * df['Number of Cows']

# fills 'Total Milk Production column' with the products of the 'Total Milk Production column' and 'Price_Per_Pound' columns
df['Total Revenue'] = df['Total Milk Production'] * df['Price_Per_Pound']

# shows the last 20 indices of the table
df.tail(n=20)

# variable assigned to all rows in the year 2020
Twenty20 = df['Total Revenue'][155:167]
print(Twenty20)

# loops through every iteration of Twenty20 and adds them together
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
202149.76 # Total Revenue (2020)
