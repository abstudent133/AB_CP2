#Main User Interface

#Pseudocode
from Individual_projects.geomentric_calculator.src.shape_management import *
from viewing_management import *

#main function
def main():
#parameters: none
    #print a message about the program
    print("This is a Geometric Calculator. You can choose to do one of the following:")
    #while true
    while True:
        #show option menu
        print("""---MAIN MENU---
              1.Create New Shape
              2.View Shapes
              3.Compare Shapes
              4.Sort Shapes
              5.Formula Guide
              6.Quit""")
        #ask them to input their choice
        choice = input("Please input the number of the action you would like to complete: ")
        #make sure choice is valid
        #call corrisponding function to the action
        if choice == "1":
            new_shape()
        elif choice == "2":
            view_shapes()
        elif choice == "3":
            compare_shapes_formating()
        elif choice == "4":
            sorting()
        elif choice == "5":
            viewing_equations()
        #if they choose to exit then break
        elif choice == "6":
            print("Thanks for using the Geometric Calculator!")
            break
            #but first print a thank you message

main()
