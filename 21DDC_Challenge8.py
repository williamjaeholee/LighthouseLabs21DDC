"""
Challenge 8; Difficulty: Easy; Points: 5 (02/24/2021)

Day 8: pandas DataFrame

After playing around with the functions above, you can start helping Dot figure out when the best time to rent a cow might be. With this dataset, you can take a look at how cows produce milk over time.

Answer the following questions for Dot:

At what year and month did company x produce the most milk?
At what year and month did company x produce the least milk?

##Stretch##

Stretch questions are not required to be completed for the challenge, but you can test your skills with more advanced challenges.

Which year produced the most milk?

"""

# Solution

# At what year and month did company x produce the most milk?

df.iloc[df['Monthly milk production: pounds per cow'].idxmax()]

# Output

Month                                      19-Jun
Monthly milk production: pounds per cow       969
Name: 148, dtype: object

# At what year and month did company x produce the least milk?

df.iloc[df['Monthly milk production: pounds per cow'].idxmin()]

# Output

Month                                      07-Dec
Monthly milk production: pounds per cow       553
Name: 10, dtype: object
        
# Stretch



# Output

