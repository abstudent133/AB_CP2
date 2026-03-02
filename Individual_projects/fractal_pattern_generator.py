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
    #else 
    else:
        #call the sierpinski function with half the length and depth - 1
        sierpinski(depth-1, length/2)
        #move right
        t.right(180)
        t.forward(length/2)
        #call the sierpinski function with half the length and depth - 1
        sierpinski(depth-1, length/2)
        #move to the tip of this triangle
        t.forward(length/2)
        #call the sierpinski function with half the length and depth - 1\
        sierpinski(depth-1, length/2)
        # Return to original position

def draw(length):
#draw function
#parameters: length
    #for 3 times
    for i in range(3):
        #go forward length
        t.forward(length)
        #turn 120 degrees to the right
        t.right(120)

def main():
#main function
#parameter: none
    #explain the program
    print("This is a Sierpinski Triangle generator.")
    #while true
    while True:
        #show them the menu of exiting or generating
        print("""Menu:
              1. Generate
              2. Exit""")
        choice = input("Please enter the number of the action you would like to complete: ")
        #if they choose generating then 
        if choice == "1":
            #ask for the color
            color = input("Please enter the name of the color you would like to pattern to be: ")
            #setup turtle and starting point
            t.home()
            t.color(color)
            t.pendown()
            #depth is ask user for the depth out of five
            depth = int(input("Please enter a depth out of five for the pattern: "))
            #call the sierpinski function with depth and 200 as the length
            sierpinski(depth, 400)
            t.done()
        #else if exit
        elif choice == "2":
            #break
            break

#call main function
main()

    


