"""
Challenge 4; Difficulty: Easy; Points: 5 (02/20/2021)

Day 4: for loops

Challenge:
Dot needs to purchase:

1. 600 planks of Oak Wood
2. 150 liters of Blue Paint
3. 15 liters of White Paint
4. 165 liters of Paint Finish

 -------------------------------------------------------------------------------------------------
|     Item	                Needed Amount to Buy	        Wholesale Price	         Retail Price |
--------------------------------------------------------------------------------------------------     
| Plank of Oak Wood	               600	                        $ 7000	               $ 12.99    |
| 1 Liter of Blue Paint	           150	                        $ 1000	               $ 8.99     |
| 1 Liter of White Paint	       15	                        $ 1000	               $ 9.99     |
| 1 Liter of Paint Finish	       165	                        $ 800	               $ 3.99     |
--------------------------------------------------------------------------------------------------

Use a loop to determine the price Dot would pay for purchasing supplies at the retail price. Based on that calculation, which itmes should Dot buy at retail vs. wholesale?

Note: Assume the wholesale price covers all the supply Dot needs for each item, whereas the retail price is per single unit.
"""

# ------------------------------------------------------------------------------------------------------------------------------------

# Solution

item_list = ['Oak Wood', 'Blue Paint', 'White Paint', 'Paint Finish']

amount_list = [600,150,15,165]

wholesale_price_list = [7000, 1000, 1000, 800]

retail_price = [12.99, 8.99, 9.99, 3.99]


full_price = []

for i in range(len(item_list)):
    
    total_price = amount_list[i] * retail_price[i]
    full_price.append(total_price)

print(full_price)

# Output

[7794.0, 1348.5, 149.85, 658.35]