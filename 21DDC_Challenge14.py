"""
Challenge 14; Difficulty: Medium; Points: 10 (03/02/2021)

Day 14: combining our knowledge

Dot's neighbour said that he only likes wine from Stellenbosch, Bordeaux, and the Okanagan Valley, and that the sulfates can't be that high. The problem is, Dot can't really afford to spend tons of money on the wine. Dot's conditions for searching for wine are:

1. Sulfates cannot be higher than 0.6.
2. The price has to be less than $20.

Use the above conditions to filter the data for questions 2 and 3 below.

Questions:

1. Where is Stellenbosch, anyway? How many wines from Stellenbosch are there in the entire dataset?
2. After filtering with the 2 conditions, what is the average price of wine from the Bordeaux region?
3. After filtering with the 2 conditions, what is the least expensive wine that's of the highest quality from the Okanagan Valley?

##Stretch Question:##

What is the average price of wine from Stellenbosch, according to the entire unfiltered dataset?

Note: Check the dataset to see if there are missing values; if there are, fill in missing values with the mean.

"""

# ------------------------------------------------------------------------------------------------------------------------------------

# Solution

# 1. Where is Stellenbosch, anyway? How many wines from Stellenbosch are there in the entire dataset?

import pandas as pd
df = pd.read_csv('winequality-red_2.csv')
df = df.drop(columns = ['Unnamed: 0'])

df.head()

SB = df.groupby(['region'])
Stellenbosch = SB.get_group('Stellenbosch')
StellenboschValues = Stellenbosch.index.values
print(len(StellenboschValues))

# Output

35

# OR

df['region'].value_counts()

# 2. After filtering with the 2 conditions, what is the average price of wine from the Bordeaux region?

sulp = df['sulphates'] <= 0.6
sulphate = df[sulp]

prc = sulphate['price'] < 20
price = sulphate[prc]

filterwithregion = price['region'] == 'Bordeaux'
filteredwithregion = price[filterwithregion]

priceValues = filteredwithregion['price']
print(priceValues.mean())

# Output

11.3

# 3. After filtering with the 2 conditions, what is the least expensive wine that's of the highest quality from the Okanagan Valley?

sulp = df['sulphates'] <= 0.6
sulphate = df[sulp]

prc = sulphate['price'] < 20
price = sulphate[prc]

filterwithregion = price['region'] == 'Okanagan Valley'
filteredwithregion = price[filterwithregion]

filteredwithregion.sort_values(by=['price', 'quality'], ascending=[True, False])

# Table outputted through sort_values(). Choose top on list.

1025 # Answer

# Stretch Question: What is the average price of wine from Stellenbosch, according to the entire unfiltered dataset?
# Note: Check the dataset to see if there are missing values; if there are, fill in missing values with the mean.

