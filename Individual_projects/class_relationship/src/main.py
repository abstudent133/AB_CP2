#Main function

#Pseudocode
#import classes
import classes

#main function
#parameters: none
    #print a menu with all the options-add student, view students, find student, add grade, class statistics
    print("""Main Menu:
    1.Add Student
    2.Add Grade
    3.View Students
    4.Find Student
    5.Class Summary
    6.Quit""")
    #choice is asking the user to choose which they would like to preform
    choice = input("Input the number of the action you would like to preform here: ")
    #use conditional and use correct method based on choice
    if choice == "1":
        student_id = input("Input the new student's ID number here: ")
        name = input("Input the student's name here: ")
        