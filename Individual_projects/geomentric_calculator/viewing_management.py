#This is Equation Management and it includes:
#Viewing all the equations used when finding the measurments of shapes
#Taking an input from the user and getting the rest of the values

#Personal Planning and Analysis

#Viewing all equations
#parameters: None
#actions:
#give them the option to view all equations or quit
#have all equations in a list
#formate that list 
#show that formated list to the user
#or they quit

#viewing all shapes
#parameters: none
#actions:
#open the file
#take each and turn it into a dictionary
#print the information of each dictionary nicely

#Pseudocode
#Import helper
from helper import *

#Viewing equations
def viewing_equations():
#parameters: none
    #create a list of all the equations
    #formate the list
    #print it out
    print("""---EQUATIONS---
          Rectangle:
          perimeter- (Length 1 x 2) + (Length 2 x 2)
          area- Length 1 x Length 2
          
          Square:
          perimeter- Length x 4
          area- Length squared

          Circle:
          diameter- Radius x 2
          perimeter- 2 x Radius x pi
          area- Radius squared x pi

          Triangle:
          perimeter- Length 1 + Length 2 + Length 3
          area- (Base x Height)/2
          """)

#view all shapes list
def view_shapes():
#paramters: none
    #call list function
    list = list_creation()
    #formate the information in that list
    for item in list:
        string = f"""{item.get("type").capitalize()} {item.get("name").capitalize()}:
Perimeter: {item.get("perimeter").capitalize()}
Area: {item.get("area").capitalize()}
"""
        print(string)
    #print it outc
    

