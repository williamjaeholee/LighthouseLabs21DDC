"""
Challenge 21; Difficulty: Hard; Points: 20 (03/09/2021)

Day 21: Grand Ol' Smashin' Finale

Dot wants to play retro video games with all their new friends! Help them figure out which games would be best.

Questions:

1. What is the correlation coefficient between Critic_Score and User_Score?

Note: You may have to clean some of the columns and fill it with the median value (if numerical).

2. Plot the top 5 best selling games released before the year 2000.

Note: Use Global_Sales

3. Create a new column called Aggregate_Score, which returns the proportional average between Critic Score and User_Score based on Critic_Count and User_Count. Plot a horizontal bar chart of the top 5 highest rated games by Aggregate_Score, not published by Nintendo before the year 2000. From this bar chart, what is the highest rated game by Aggregate_Score?

Note: Critic_Count should be filled with the mean. User_Count should be filled with the median.

##Stretch:##

Don't stop at the above challenges, be inquisitive of your given dataset, dive deeper, and share your insights on the forum. For your reference, the dataset used in today's challenge can be downloaded for free from Kaggle.

"""

# ------------------------------------------------------------------------------------------------------------------------------------

# Solution

# 1. What is the correlation coefficient between Critic_Score and User_Score?

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('video_games.csv')

criticScoreMedian = df['Critic_Score'].median()
userScoreMedian = df['User_Score'].median()

df['Critic_Score'] = df['Critic_Score'].fillna(value = criticScoreMedian)
df['User_Score'] = df['User_Score'].fillna(value = userScoreMedian)

plt.figure()
plt.scatter(x=df['Critic_Score'], y=df['User_Score'])
plt.show()

print(round((df['Critic_Score']).corr(df['User_Score']), 4))

# 2. Plot the top 5 best selling games released before the year 2000.

# Note: Use Global_Sales

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('video_games.csv')

yearFilter = df['Year_of_Release'] < 2000
yearFiltered = df[yearFilter]

bestSellingFiltered = yearFiltered.sort_values('Global_Sales', ascending=False).head()
bestSellingFiltered

plt.figure()
plt.bar(x=bestSellingFiltered.Name, height=bestSellingFiltered.Global_Sales)
plt.show()

# Output

# Bar plot of the top 5 best selling video games by net global sales

# 3. Create a new column called Aggregate_Score, which returns the proportional average between Critic Score and User_Score based on Critic_Count and User_Count. Plot a horizontal bar chart of the top 5 highest rated games by Aggregate_Score, not published by Nintendo before the year 2000. From this bar chart, what is the highest rated game by Aggregate_Score?

# Note: Critic_Count should be filled with the mean. User_Count should be filled with the median.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('video_games.csv')

criticScoreMedian = df['Critic_Score'].median()
userScoreMedian = df['User_Score'].median()
criticCountMedian = df['Critic_Count'].mean()
userCountMedian = df['User_Count'].median()

# filling in NaN values in respective columns
df['Critic_Score'] = df['Critic_Score'].fillna(value = criticScoreMedian)
df['User_Score'] = df['User_Score'].fillna(value = userScoreMedian)
df['Critic_Count'] = df['Critic_Count'].fillna(value = criticCountMean)
df['User_Count'] = df['User_Count'].fillna(value = userCountMedian)

# adding Aggregate_Score column to dataframe

df['Aggregate_Score'] = ((Critic_Count*Critic_Score)+(User_Count*User_Score))/(User_Count+Critic_Count)

# filter data

nintendoFilter = df['Publisher'] != 'Nintendo'
nintendoFiltered = df[nintendoFilter]

nintendoYearFiltered = nintendoFiltered['Year_of_Release'] < 2000

top5Nintendo = nintendoYearFiltered.sort_values('Aggregate_Score', ascending=False).head()
top5Nintendo

# graph plot

plt.figure()
plt.barh(y=top5Nintendo.Name, width=top5Nintendo.Aggregate_Score)
plt.show()

# Output

# horizontal bar plot of top 5 non-Nintendo-published video games before the year 2000 by their aggregate scores



"""
That's it folks!
"""
