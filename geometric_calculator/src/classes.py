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
import math

#rectangle class
class Rectangle:
    #initiate(self, length 1, length 2)
    def __init__(self,name, length_1, length_2):
        #initiate length 1 and 2 with self
        self.len_1 = length_1
        self.len_2 = length_2
        self.name = name
    #string(self, perimeter, area)
    def __str__(self):
        #formate all the necessary information collected
        return f"""Rectangle: {self.name}
Side 1: {self.len_1}
Side 2: {self.len_2}
Perimeter: {self.perimeter()}
Area: {self.area()}"""
    #perimeter(self)
    def perimeter(self):
        #2x length 1
        #2x length 2
        #add it all together
        return 2*self.len_1 + 2*self.len_2
    #area(self)
    def area(self):
        #mulitply length 1 by length 2
        return self.len_1*self.len_2

#square class
class Square:
    #initiate(self, length)
    def __init__(self,name,length):
        #initiate length with self
        self.length = length
        self.name = name
    #string(self, area, perimeter)
    def __str__(self):
        #formate length, perimeter, and area
        return f"""Square: {self.name}
Length: {self.length}
Perimeter: {self.perimeter()}
Area: {self.area()}
"""
    #perimeter(self)
    def perimeter(self):
        #4x length
        return 4*self.length
    #area(self)
    def area(self):
        #length^2
        return self.length**2

#circle class
class Circle:
    #initiate(self, radius)
    def __init__(self,name, radius):
        #initiate radius with self
        self.radius = radius
        self.name = name
    #string(self, area, perimeter)
    def __str__(self):
        return f"""Circle: {self.name}
Radius: {self.radius}
Perimeter: {self.perimeter()}
Area: {self.area()}
Diameter: {self.diameter()}"""
        #formate radius, perimeter, area, diameter
    #perimeter(self)
    def perimeter(self):
        #2x 3.14x radius
        return round((self.radius*2*math.pi),2)
    #area(self)
    def area(self):
        #radius x 3.14^2
        return round((self.radius**2*math.pi),2)
    #Diameter(self)
    def diameter(self):
        #radius*2
        return self.radius*2

#triangle class
class Triangle:
    #initiate(self, part of base 1, part of base 2, height)
    def __init__(self, name,base_1, base_2, height):
        #initiate all of these with self
        self.base_1 = base_1
        self.base_2 = base_2
        self.height = height
        self.name = name
    #string(self,area, perimeter)
    def __str__(self):
        return f"""Triangle: {self.name}
Base: {self.base()}
Perimeter: {self.perimeter()}
Area: {self.area()}"""
        #formate of the information
    #perimeter(self)
    def perimeter(self):
        #add both sides of the base together
        #add one side of the base squared and the height squared
        side_1 = math.sqrt(self.base_1**2+self.height**2)
        side_2 = math.sqrt(self.base_2**2+self.height**2)
        #square root the second number
        #round that number with the rounding function
        #repeat that for both sides of the base
        #add the square rooted numbers plus the lenght of the base
        #return that number
        return round(side_1+ side_2 + self.base(),2)
    #area(self)
    def area(self):
        #base length times the height
        #return the number
        return (self.base()*self.height)/2
    #base(self)
    def base(self):
        #add bases together
        return self.base_1+ self.base_2

