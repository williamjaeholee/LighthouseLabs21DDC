"""
Challenge 18; Difficulty: Medium; Points: 10 (03/07/2021)

Day 18: Matplotlib Stylistic Methods

1. What are the top 5 boardgame categories in this dataset that are not targeted for young children?

Note: For the question above, use a filter to acquire boardgames with an inteded age of 13+, there is an age column in our dataset.

2. Which categories of boardgames that are not targeted for young children are the same compared to the top 5 boardgames categories in the overall dataset?

##Stretch##

Try out the various matplotlib plot styles from this article.

"""

# ------------------------------------------------------------------------------------------------------------------------------------

# Solution

# 1. What are the top 5 boardgame categories in this dataset that are not targeted for young children?

# Note: For the question above, use a filter to acquire boardgames with an inteded age of 13+, there is an age column in our dataset.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('boardgames.csv')

gamesFilter = df['age'] >= 13
gamesFiltered = df[gamesFilter]

categoryFilter = gamesFiltered['category'].value_counts().head()
categoryFilter

# Output

Card Game, Fantasy       30
Wargame, World War II    28
Card Game                24
Economic, Trains         14
Fantasy                  14
Name: category, dtype: int64

# 2. Which categories of boardgames that are not targeted for young children are the same compared to the top 5 boardgames categories in the overall dataset?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('boardgames.csv')

gamesFilter = df['age'] >= 13
gamesFiltered = df[gamesFilter]

categoryFilter = gamesFiltered['category'].value_counts().head().index

dataFrame = df['category'].value_counts().head().index

np.intersect1d(categoryFilter, dataFrame)

# Output

array(['Card Game', 'Card Game, Fantasy', 'Wargame, World War II'],
      dtype=object)
