"""
Challenge 1; Difficulty: Easy; Points: 5 (02/17/2021)

Day 1: Python Variables & print Functions

Modify the lease agreement with your signature without changing the original lease variable.

lease = '''Dear Dot, 
           This document validates that you are beholden to a monthly payment of rent for this house.
           Rent is to be paid by the first of every month.
           Fill in your signature to agree to these terms.  
            -------------
            Please Sign Here: 
'''
"""

# ------------------------------------------------------------------------------------------------------------------------------------

#Solution

signature = "Dot"

new_lease = f'''
Dear Dot, 
This document validates that you are beholden to a monthly payment of rent for this house.
Rent is to be paid by the first of every month.
Fill in your signature to agree to these terms.
-------------
Please Sign Here: {signature} 
'''
print(new_lease)

# Output

Dear Dot, 
This document validates that you are beholden to a monthly payment of rent for this house.
Rent is to be paid by the first of every month.
Fill in your signature to agree to these terms.
-------------
Please Sign Here: Dot 
