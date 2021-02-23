"""
Challenge 6; Difficulty: Easy; Points: 5 (02/22/2021)

Day 6: Descriptive Statistics

There are many holes in the living room's ceiling that desperately need to be fixed. Dot's measured them, and in total there are about 100. They need to figure out how much does it cost to fix all of the holes. Differently sized holes will require differently sized patches to fix them.

 ---------------------------------------------------------------------------------------
|                        Size of Hole	                                   Cost to Fix  |
 ---------------------------------------------------------------------------------------
|                    Small (less than 20 mm)	                              $1.30     |
|    Medium (above or equal to 20 mm AND less than 70mm)	                  $1.60     |
|            Large (above or equal to 70 mm)	                              $2.10     |
 ---------------------------------------------------------------------------------------

Dot needs you to look at the measurements and figure out the answers to the following questions:

What is the average sized hole?
What is the average cost to fix a hole?
What is the total cost of fixing all of the holes?

Note: Use a for loop and an if else statement to answer Q3.

###Stretch Question:###

Stretch Questions are not required to be completed to finish the challenge but are recommended to further develop your skills.

What is the maximum sized hole?
What is the minimum sized hole?
"""

# --------------------------------------------------------------------------------------------------------------------------------------

# Solution

# 1.

# Pandas version
import pandas as pd
import random 
random.seed(34)

hole_sizes = [random.randint(1, i) for i in range(1, 101)]
random.shuffle(hole_sizes)

# hole sizes in mm
hole_sizes[:5]

holeSeries = pd.Series(hole_sizes)
holeMean = holeSeries.mean()
print(holeMean)

# Arithmetic version
print(sum(hole_sizes)/len(hole_sizes))

# Output:

28.39

# 2.

count_small = 0
count_medium = 0
count_large = 0

for i in hole_sizes:
    if(i < 20):
        count_small += 1
    elif(20 <= i < 70):
        count += 1
    else:
        count += 1

print(f'Small Holes: {count_small}')
print(f'Medium Holes: {count_medium}')
print(f'Large Holes: {count_large}')

average_cost = (((count_small*1.30) + (count_medium*1.60) + (count_large*2.10))/len(hole_sizes))
average_cost = round(average_cost, 4)
print(f'Average Cost: {average_cost}')

# Output:

Small Holes: 44
Medium Holes: 52
Large Holes: 4
Average Cost: 1.488

# 3.

total_cost = 0

for i in hole_sizes:
    if(i < 20):
        total_cost += 1.30
    elif(20 <= i < 70):
        total_cost += 1.60
    else:
        total_cost += 2.10

print(round(total_cost), 4)

# Output:

148.8

# Stretch Question 1

import pandas as pd
import random 
random.seed(34)

hole_sizes = [random.randint(1, i) for i in range(1, 101)]
random.shuffle(hole_sizes)

# hole sizes in mm
hole_sizes[:5]

holeSeries = pd.Series(hole_sizes)
holeMax = holeSeries.max()
print(holeMax)

# Output:

96

# Stretch Question 2

import pandas as pd
import random 
random.seed(34)

hole_sizes = [random.randint(1, i) for i in range(1, 101)]
random.shuffle(hole_sizes)

# hole sizes in mm
hole_sizes[:5]

holeSeries = pd.Series(hole_sizes)
holeMin = holeSeries.min()
print(holeMin)

# Output:

1
