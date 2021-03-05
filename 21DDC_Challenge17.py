"""
Challenge 17; Difficulty: Easy; Points: 5 (03/04/2021)

Day 17: Bar Plots and Specific Data

Help Dot by answering the following questions using a bar plot:

1. What are the top 5 rated books in the dataset?

2. What are the top 5 books with the highest average rating?

Note: Filter out books that have low ratings_count, for question 2 filter out books with a ratings_count less than the mean.

Stretch

As an optional bonus question, try answering this as well:

1. What are the top 5 authours with the most books in the dataset?

"""

# ------------------------------------------------------------------------------------------------------------------------------------

# Solution

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("books.csv")

# 1. What are the top 5 rated books in the dataset?

top5ratingscount = df.sort_values(['ratings_count'], ascending=False).head()
top5ratingscount


# 2. What are the top 5 books with the highest average rating?

top5averagerating = df[df['ratings_count'] > df['ratings_count'].mean()].sort_values('average_rating', ascending=False).head()
top5averagerating

##STRETCH##

# 1. What are the top 5 authours with the most books in the dataset?

authorcount = df.groupby('authors').count().sort_values('title', ascending=False).head()
print(authorcount.index.values)

# Output

['Stephen King' 'P.G. Wodehouse' 'Rumiko Takahashi' 'Orson Scott Card' 'Agatha Christie'] # Answer
