#AB 1st Fractal Pattern Generator
#Project Analysis

#draw_triangle function
#parameters(length)
#actions
#repeat 3 times
#go forward length
#turn 120 degrees


#draw funciton
#parameters: depth
#actions:
#start at the starting point
#get a starter side length based on depth
#draw a triangle
#draw the line for one of the next smallest
#repeat that for the depth
#start filling in the next biggest triangle
#repeat that for the whole triangle
#start with the bottom right corner

#main function
#parameters: none
#actions
#ask user for the color
#ask user for depth out of five
#setup turtle
#call the draw function with the depth
#ask if they would like to create a new one

#Pseudocode
#import turtle
import turtle as t

#sierpinski function
def sierpinski(depth, length):
#parameters: depth, length
    #if depth is 0 then draw a triangle with length
    if depth == 0:
        draw(length)
    else:
        #create starting point
        start_pos = t.pos()
        start_heading = t.heading()
        # go to bottom left corner
        sierpinski(depth-1, length/2)
        # go to bottom right corner
        t.penup()
        t.goto(start_pos)
        t.setheading(start_heading)
        t.forward(length/2)
        t.pendown()
        sierpinski(depth-1, length/2)
        #got to the top
        t.penup()
        t.goto(start_pos)
        t.setheading(start_heading)
        t.left(60)
        t.forward(length/2)
        t.right(60)
        t.pendown()
        sierpinski(depth-1, length/2)
        #go to the original spot
        t.penup()
        t.goto(start_pos)
        t.setheading(start_heading)
        t.pendown()

def draw(length):
#draw function
#parameters: length
    #for 3 times
    for i in range(3):
        #go forward length
        t.forward(length)
        #turn 120 degrees to the right
        t.right(120)



    


