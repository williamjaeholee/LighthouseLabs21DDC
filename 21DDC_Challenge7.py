"""
Challenge 7; Difficulty: Medium; Points: 10 (02/23/2021)

Day 7: Simple Functions and Data Cleaning

Dot has a lot of different boxes laying around. They need a system for how to unpack them, or they'll just continue procrastinating. Help Dot sort the boxes by their weight.

     --------------------------------------------
    |    Box:	                   Weight (kg)   |
     --------------------------------------------
    |    Box 1	                        4        |
    |    Box 2	                        2        |
    |    Box 3	                        18       |
    |    Box 4	                        21       |
    |    Box 5	                        14       |
    |    Box 6	                        13       |
     --------------------------------------------

Create a function that will open the boxes according to their weight, from lightest to heaviest.

"""

# --------------------------------------------------------------------------------------------------------------------------------------

# Solution

#example dicitonary
user_boxes = {'weight': [4,2,18,21,14,13],
              'box_name': ['box1','box2', 'box3', 'box4', 'box5', 'box6']
             }

def LightesttoHeaviest(lon):
    for n in range(len(lon)-1,0,-1):
        for i in range(n):
            if(lon[i]>lon[i+1]):
                temp = lon[i]
                lon[i] = lon[i+1]
                lon[i+1] = temp

lon = user_boxes['weight']
LightesttoHeaviest(lon)
print(lon)

# Output

[2, 4, 13, 14, 18, 21]

# OR

def open_box_order(user_boxes):
    
    for i in range(len(user_boxes['weight'])):
        
        for j in range(len(user_boxes['weight']) - 1):
            
            if user_boxes['weight'][j] > user_boxes['weight'][j+1]:
                
                user_boxes['weight'][j], user_boxes['weight'][j+1] = user_boxes['weight'][j + 1],user_boxes['weight'][j]
                user_boxes['box_name'][j], user_boxes['box_name'][j+1] = user_boxes['box_name'][j + 1],user_boxes['box_name'][j]
                
    return print(user_boxes['box_name'])

open_box_order(user_boxes)

# Output

['box2', 'box1', 'box6', 'box5', 'box3', 'box4']

user_boxes

# Output

{'weight': [2, 4, 13, 14, 18, 21],
 'box_name': ['box2', 'box1', 'box6', 'box5', 'box3', 'box4']}