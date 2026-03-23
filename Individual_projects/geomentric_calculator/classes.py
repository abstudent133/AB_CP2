#These are the classes

#Personal Planning and Analysis

#Shape Classes
#rectangle class
#initiate: self, length 1, length 2
#string:formate the information into something that looks good
#find perimeter(2x each length then add it all together)
#find area(length 1 x length 2)
#return the string

#square class(rectange)
#initiate: self, length
#string:formate the information correctly
#perimeter(multiply the length times four)
#area(square the length)
#return the string

#circle class
#initiate: self, radius
#string: formate it 
#find diameter(multipyly radius by two)
#find perimeter(2x pi x the radius(possibly substitute pi for 3.141))
#find area(pi x radius squared)

#triangle class
#initiate: self, first part of base, second part of base, height
#string: formate
#perimeter(use the pythagorean theorem to find the other two sides then add everything together)
#area(add the two sides of the base then multiply by the height)

#Pseudocode
#import math

#rectangle class
    #initiate(self, length 1, length 2)
        #initiate length 1 and 2 with self
    #string(self, perimeter, area)
        #formate all the necessary information collected
    #perimeter(self)
        #2x length 1
        #2x length 2
        #add it all together
        #return that
    #area(self)
        #mulitply length 1 by length 2
        #return that

#square class
    #initiate(self, length)
        #initiate length with self
    #string(self, area, perimeter)
        #formate length, perimeter, and area
    #perimeter(self)
        #4x length
    #area(self)
        #length^2

#circle class
    #initiate(self, radius)
        #initiate radius with self
    #string(self, area, perimeter)
        #formate radius, perimeter, area, diameter
    #perimeter(self)
        #2x 3.14x radius
        #return that number
    #area(self)
        #radius x 3.14^2
        #return that number

#triangle class
    #initiate(self, part of base 1, part of base 2, height)
        #initiate all of these with self
    #string(self,area, perimeter)
        #formate of the information
    #perimeter(self)
        #add both sides of the base together
        #add one side of the base squared and the height squared
        #square root the second number
        #round that number with the rounding function
        #repeat that for both sides of the base
        #add the square rooted numbers plus the lenght of the base
        #return that number
    #area(self)
        #base length times the height
        #return the number

