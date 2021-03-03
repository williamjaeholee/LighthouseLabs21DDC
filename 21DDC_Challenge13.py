"""
Challenge 13; Difficulty: Easy; Points: 5 (03/01/2021)

Day 13: sorting with pandas

Use the pandas sort function and the pandas filter function from the previous challenge to answer these questions:

1. Which wines had a quality of 8 or higher and a residual sugar level above 5?
2. How many wines in total had a quality of 8 and 7 and a citric acid level below 0.4?

Note: Use the index positions of the wines as the wine names.

"""

# ------------------------------------------------------------------------------------------------------------------------------------

# Solution

# 1. Which wines had a quality of 8 or higher and a residual sugar level above 5?

import pandas as pd
wine_df = pd.read_csv('winequality-red.csv')
wine_df

filterQuality = wine_df['quality'] >= 8
filteredQuality = wine_df[filterQuality]

filterSugar = wine_df['residual sugar'] > 5
filteredSugar = wine_df[filterSugar]

filteredSweetQuality = filteredQuality + filteredSugar

filteredSweetQuality.sort_values(by=['residual sugar', 'quality'], ascending=False)

# Output

"""
All other table values are NaN except the top two which have the following conditions of filteredQuality and filteredSugar.

These are rows 278 and 455.

"""

# OR

import pandas as pd
wine_df = pd.read_csv('winequality-red.csv')
wine_df

filterQuality = wine_df['quality'] >= 8
filteredQuality = wine_df[filterQuality]

filteredSugar = filteredQuality['residual sugar'] > 5

filteredSweetQuality = filteredQuality[filteredSugar]

print(filteredSweetQuality.index.values)

# Output

[278 455]

# 2. How many wines in total had a quality of 8 and 7 and a citric acid level below 0.4?

import pandas as pd
wine_df = pd.read_csv('winequality-red.csv')
wine_df


wine_df = pd.read_csv('winequality-red.csv')
wine_df

filterQuality7 = wine_df['quality'] == 7
filteredQuality7 = wine_df[filterQuality7]

filterQuality8 = wine_df['quality'] == 8
filteredQuality8 = wine_df[filterQuality8]

concatenateFiltered = pd.concat([filteredQuality7, filteredQuality8])

filterCitricAcid = concatenateFiltered['citric acid'] < 0.4
filteredCitricAcid = concatenateFiltered[filterCitricAcid]

filteredCitricAcid.count()

# OR

filter_wine_2 = wine_df['citric acid'] < 0.4
filtered_df_2 = wine_df[filter_wine_2]

filtered_df_2['quality'].value_counts()

# Output

5    534
6    436
7     96
4     45
8      9
3      7
Name: quality, dtype: int64

print(96+9)
        
# Output

105
