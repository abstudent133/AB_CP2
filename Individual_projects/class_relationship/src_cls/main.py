#Main function

#Pseudocode
#import classes
import classes

#main function
def main():
#parameters: none
    #load students from csv
    students = classes.load_students()
    #create gradebook object
    gradebook = classes.GradeBook(students)

    #loop so program keeps running until quit
    while True:
        #print menu
        print("""Main Menu:
    1.Add Student
    2.Add Grade
    3.View Students
    4.Find Student
    5.Class Summary
    6.Quit""")

        #get user choice
        choice = input("Input the number of the action you would like to preform here: ")

        #option 1 add student
        if choice == "1":
            gradebook.add_students()

        #option 2 add grade
        elif choice == "2":
            gradebook.add_grade()

        #option 3 view students
        elif choice == "3":
            gradebook.view_students()

        #option 4 find student
        elif choice == "4":
            gradebook.find()

        #option 5 class summary
        elif choice == "5":
            gradebook.class_summary()

        #option 6 quit program
        elif choice == "6":
            print("Program ending.")
            break

        #invalid input
        else:
            print("That was an invalid input.")

main()     