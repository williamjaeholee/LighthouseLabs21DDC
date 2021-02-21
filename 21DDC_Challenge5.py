"""
Challenge 5; Difficulty: Medium; Points: 10 (02/21/2021)

Day 5: Conditional Logic & Control Flows

Dot's okay with paying a bit of a surplus for convenience, but they don't want to go broke buying dustpans and glass cleaner. Help them figure out which items cost over 10% more at the nearby store, so they can avoid buying these items.

Using Python, develop a list of items that are too expensive for Dot to purchase at the nearby store.
"""

# --------------------------------------------------------------------------------------------------------------------------------------

# Solution

# Cleaning Supplies List (19 items)
cleaningsupplies_list = ['Broom', 'Mop', 'Dustpan', 'Garbage Bags', 'Glass Cleaner', 'Vinegar',
                        'Soap', 'Bleach', 'Duster', 'Floor Cleaner', 'Sponges', 'Dish Soap',
                        'Drain Cleaner', 'Paper Towels', 'Cleaning Rags', 'Toilet Cleaner', 
                        'Rubber Gloves', 'Alcohol Wipes', 'Squeegee']

# City Price
city_price = [6.49, 4.99, 3.39, 4.29, 3.99, 1.99, 
              1.50, 3.99, 4.99, 5.99, 2.99, 2.99, 
              5.99, 2.99, 3.49, 6.99, 2.99, 1.98, 11.99]

# Country Price
country_price = [5.49, 4.69, 4.42, 5.99, 5.99, 2.50,
                1.25, 2.49, 4.50, 6.75, 2.49, 1.99, 
                6.25, 3.99, 3.59, 4.99, 1.69, 1.87, 10.99]

newlist = []
for i, j in zip(city_price, country_price):
    if(((j-i)/i)>0.10):
        newlist.append(cleaningsupplies_list[city_price.index(i)])

print(newlist)

# Output: 