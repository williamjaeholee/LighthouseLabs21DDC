"""
Challenge 2; Difficulty: Easy; Points: 5 (02/18/2021)

Day 2: math with Python

Dot has a few lists you can use as reference: their grocery list, the prices they used to pay in the city, and the prices for the rural grocer. What is the price difference between groceries in the city vs. groceries in the country, as a percentage of country prices?

Note: The index position for each item is consistent across all three lists.

# Grocery List (19 items)
grocery_list = ['Bananas', 'Clementines', 'Baguette', 'Oat Milk', 'Olive Oil', 'Coffee Beans',
                'Chocolate Bar', 'Brocolli', 'Eggplant', 'Chickpeas', 'Lentils', 'Tomatoes',
                'Pasta', 'Rice', 'Yogurt', 'Blueberries', 'Onions', 'Garlic', 'Truffles']

# City Price
city_price = [6.49, 4.99, 4.39, 4.29, 11.99, 17.99,          
              3.49, 3.99, 1.10, 1.99, 2.99, 4.68,            
              1.59, 8.99, 3.49, 6.99, 2.99, 1.98, 14.99]

# Country Price
country_price = [4.49, 4.12, 3.42, 6.99, 7.99, 14.99,              
                2.99, 2.49, 0.99, 1.49, 2.49, 1.99,              
                1.59, 6.99, 3.89, 4.99, 1.69, 1.87, 11.49]
"""

# ------------------------------------------------------------------------------------------------------------------------------------

# Solution

citygroceries_Sum = sum(city_price)
countrygroceries_Sum = sum(country_price)

difference = (citygroceries_Sum - countrygroceries_Sum)/ countrygroceries_Sum

print(round(difference,4))

# Output

0.2582