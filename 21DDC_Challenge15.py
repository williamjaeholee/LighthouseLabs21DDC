"""
Challenge 15; Difficulty: Hard; Points: 20 (03/02/2021)

Day 15: Data Visualization (using Matplotlib)

Dot already has a few seeds they can use for their garden. They need to figure out which of the seeds will produce the biggest potential harvest. Can you help Dot decide which seeds are best, by using data visualization?

Create a bar graph with Matplotlib that shows each vegetable and the size of the potential harvest that Dot can expect from them.

1. Which of Dot's seeds will produce the largest harvest?

"""

# Key Points

# The process for basic plot-building in Matplotlib can be divided into 3 parts: the frame, the plot, and the styling.

plt.figure()                        # The Frame: We start our plot with a figure
plt.bar(x = data, height = data)    # The Body: Declaring the specific bar plot statment
plt.title("Example Bar Plot")       # Styling: Adding the title
plt.show()                          # To show our plot, we need to end our plot with a plt.show()

# ------------------------------------------------------------------------------------------------------------------------------------

# Solution

import pandas as pd
import matplotlib.pyplot as plt

seeds = {
    'Vegetable' : ['Carrots', 'Tomatoes', 'Potatoes', 'Eggplant', 'Cucumbers'],
    'Seeds_Count' : [300,10,90,100,15],
    'Each_Seed_Produces': [1,140,10,5, 90]
}

vegetable = seeds.get('Vegetable')
seedcount = seeds.get('Seeds_Count')
seedproduction = seeds.get('Each_Seed_Produces')

def add_production(sC, sP):
    newlist = []
    sum = 0
    for i, j in zip(sC, sP):
            sum = (i * j)
            newlist.append(sum)
    return newlist
    
totalproduction = add_production(seedcount, seedproduction)

df = pd.DataFrame(seeds)
df

plt.figure()
plt.bar(x = vegetable, height = totalproduction)
plt.show()

# Output

# Bar graph showing the different types of vegetables and their respective production capabilities

Tomatoes [1400] # Answer
