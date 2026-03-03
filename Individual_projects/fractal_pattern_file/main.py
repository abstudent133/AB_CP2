#AB 1st Main

import turtle as t
import fractal_pattern_generator

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
            t.color(color)
            t.clear()
            t.penup()
            t.goto(-200, -150)
            t.setheading(0)
            t.pendown()
            #depth is ask user for the depth out of five
            depth = int(input("Please enter a depth out of five for the pattern: "))
            if depth in range(1,6):
            #call the sierpinski function with depth and 200 as the length
                fractal_pattern_generator.sierpinski(depth, 400)
        #else if exit
        elif choice == "2":
            #break
            break
         

#call main function
main()
t.done()