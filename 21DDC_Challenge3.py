"""
Challenge 3; Difficulty: Easy; Points: 5 (02/19/2021)

Day 3: Lists, Dictionaries, & Indexing

Dot has some specific rules for what they want to change in the shopping list:

They hate oak wood, and prefer maple.
They want to paint all the rooms blue except the kitchen, which they want to paint white.
old_blueprint = {
    "Kitchen": ['Dirty', 'Oak', "Damaged", "Green"],
    "Dining Room": ['Dirty', 'Pine', 'Good Condition', 'Grey'],
    "Living Room": ['Dirty', 'Oak', 'Damaged', 'Red'],
    "Bedroom" : ["Clean", 'Mahogany', 'Good Condition', 'Green'],
    "Bathroom": ["Dirty", 'White Tile', 'Good Condition','White'],
    "Shed"    : ['Dirty', "Cherry", "Damaged", "Un-painted"]
}

shopping_list = ['20 x Oak Plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'White Paint', 'White Paint']
Note: The blueprint above is in a dictionary format and we won't be needing to work with dictionaries in the challenge, use the blueprint as reference only.

Use python's pop(), insert(), and append() list functions to change the shopping_list above so that it reflects the right materials needed.

The list should be ordered by wood types first, then paint types.

example_shopping_list = ['wood type in room A', 'wood type in room b','paint type in room a','paint type in room b']

Create a paint_list list from the new_shopping_list list using the built in python list indexing ability.
"""

# ------------------------------------------------------------------------------------------------------------------------------------

# Solution

new_shopping_list = shopping_list
print(new_shopping_list)

# Output

['20 x Oak plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'White Paint', 'White Paint']

new_shopping_list.pop(-1)
print(new_shopping_list)

# Output

['20 x Oak plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'White Paint']

new_shopping_list.pop(-1)
print(new_shopping_list)

# Output

['20 x Oak plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint']

new_shopping_list.append('Blue Paint')
print(new_shopping_list)

# Output

['20 x Oak plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'Blue Paint']

new_shopping_list.append('Blue Paint')
print(new_shopping_list)

# Output

['20 x Oak plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'Blue Paint', 'Blue Paint']

new_shopping_list.append('Blue Paint')
print(new_shopping_list)

# Output

['20 x Oak plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'Blue Paint', 'Blue Paint', 'Blue Paint']

new_shopping_list.append('Blue Paint')
print(new_shopping_list)

# Output

['20 x Oak plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'Blue Paint', 'Blue Paint', 'Blue Paint', 'Blue Paint']

new_shopping_list.append('Blue Paint')
print(new_shopping_list)

# Output

['20 x Oak plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'Blue Paint', 'Blue Paint', 'Blue Paint', 'Blue Paint', 'Blue Paint']

new_shopping_list.pop(0)
new_shopping_list.insert(0, "20 x Maple Plank")
print(new_shopping_list)

# Output

['20 x Maple Plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'Blue Paint', 'Blue Paint', 'Blue Paint', 'Blue Paint', 'Blue Paint']

new_shopping_list.pop(1)
new_shopping_list.insert(1, "20 x Maple Plank")
print(new_shopping_list)

# Output

['20 x Maple Plank', '20 x Maple Plank', '20 x Cherry Plank', 'White Paint', 'Blue Paint', 'Blue Paint', 'Blue Paint', 'Blue Paint', 'Blue Paint']

new_shopping_list = ['20 x Maple Plank', '20 x Maple Plank', '20 x Cherry Plank', 'White Paint', 'Blue Paint','Blue Paint','Blue Paint','Blue Paint', 'Blue Paint']
print(new_shopping_list)

# Output

['20 x Maple Plank', '20 x Maple Plank', '20 x Cherry Plank', 'White Paint', 'Blue Paint','Blue Paint','Blue Paint','Blue Paint', 'Blue Paint']

paint_list = new_shopping_list[3:]
print(paint_list)

# Output

['White Paint', 'Blue Paint', 'Blue Paint', 'Blue Paint', 'Blue Paint', 'Blue Paint']