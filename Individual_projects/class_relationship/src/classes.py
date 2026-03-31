#Classes File
#This file will hold all the classes

#Planning and Analysis

#Student class
#parameters: student_id, student_name, list of grades
#initiate
#string all the info together in a pretty way
#add grades
#intake a grade then add it to the list
#calculate average
#take all the scores add them together then divide by the length
#calculate grade
#use conditional to take the average of the grades and find the letter grade it belongs to

#GradeBook class
#parameters: none
#initiate
#add student
#add student with student class
#save that student to the csv
#find student
#show all the students
#ask them to input which student they want with the id
#show them the information by calling the string method in the student class
#show class info
#get all the average grades
#put them into a list
#average them
#get the highest score
#get the lowest score
#total number of students

#Pseudocode
#import helper functions
from helper import *

#student class
class Student:
#parameters: student_id, student_name, grades_list = []
    #initiate all things with self
    def __init__(self, id, name, grades_list = None):
        #if no grades list is given create an empty one
        if grades_list == None:
            grades_list = []
        #store id
        self.id = id
        #store name
        self.name = name
        #store grades list
        self.grades = grades_list

    #string
    def __str__(self):
        #take all the information including the info found using other methods and formate it in a pretty way
        return f"""Name: {self.name}
ID: {self.id}
Grade: {self.average()}
Letter Grade: {self.letter_grade()}
Grades: {self.grades}"""

    #add grades
    def add_grades(self):
        #ask for new grade
        new_grade = pos_num_sanitation(float(input("Input new grade here: ")))
        #add it to the list of grades
        self.grades.append(new_grade)
        #create a formated print that shows how many grades and the new average
        print(f"{self.name} has {len(self.grades)} grades with an average of {self.average()}")
        #return that list of grades
        return self.grades

    #average
    def average(self):
        #intake the list of grades
        total = 0
        #add them all together
        if self.grades != []:
            #loop through each grade
            for num in self.grades:
                total += num
            #divide the length of the list
            total = round(total/len(self.grades), 2)
            return total
        else:
            #if there are no grades return N/A
            return "N/A"
            
    #letter grade
    def letter_grade(self):
        #intake the average
        aver = self.average()
        #use conditionals based on letter grade list to get the correct letter grade
        grade_letter = ""
        if aver != "N/A":
            #check ranges for grade
            if aver >= 90:
                grade_letter = "A"
            elif aver >= 80:
                grade_letter = "B"
            elif aver >= 70:
                grade_letter = "C"
            elif aver >= 60:
                grade_letter = "D"
            else:
                grade_letter = "F"
        else:
            #if no average just leave blank
            grade_letter = ""
        return grade_letter

#GradeBook class
class GradeBook:
#parameters:list of students
    #initiate list of students with self
    def __init__(self, students):
        #store list of students
        self.students = students

    #view all students
    def view_students(self):
        #if there are students
        if self.students != []:
            #print header
            print("____________________________")
            print("| ID | Name | Grade | Letter |")
            #loop through students and print info
            for student in self.students:
                print(f"|{student.get('id')}|{student.get('name')}|{student.get('grade')}|{student.get('letter')}|")
        else:
            #if empty list
            print("There are no students yet.")

    #add students
    def add_students(self):
        #ask user for student id
        id = input("Enter the new student's id: ")
        #ask user for student name
        name = input("Enter the name of the new student: ")
        #create new student object
        new_student= Student(id, name)
        #get average (will be N/A at start)
        average = new_student.average()
        #get grades list (empty at start)
        grades = new_student.grades
        #get letter grade (empty at start)
        grade_letter = new_student.letter_grade()

        #create dictionary version of student
        new_student_dict = {"id": id,
                            "name": name,
                            "grade": average,
                            "letter": grade_letter,
                            "grades": grades}
        #add student to list of students
        self.students.append(new_student_dict)
        #show information about student
        print(new_student)
        #save the new list of students with save
        save(self.students)

    #add grade
    def add_grade(self):
        #if there are students
        if self.students != []:
            #print all students
            print("____________________________")
            print("| ID | Name | Grade | Letter |")
            for student in self.students:
                print(f"|{student.get('id')}|{student.get('name')}|{student.get('grade')}|{student.get('letter')}|")

            #ask for student id
            student_id = input("Input the ID number of the student you would like to select here: ")

            #find matching student
            for student in self.students:
                if student["id"] == student_id:
                    #print student info
                    print(f"""Name: {student.get('name')}
        Grade Percentage: {student.get('grade')}
        Letter Grade: {student.get('letter')}
        Grades:""")
                    #print each grade
                    for grade in student["grades"]:
                        print(grade)

                    #ask if user wants to add grade
                    choice = input("Would you like to add a grade to this student? If yes input 1 if no input 2 here: ")

                    #if yes
                    if choice == "1":
                        #turn dictionary back into student object
                        student_info = Student(student.get("id"), student.get("name"), student.get("grades"))
                        #call add grade method
                        student_info.add_grades()

                        #update dictionary with new info
                        student["grades"] = student_info.grades
                        student["grade"] = student_info.average()
                        student["letter"] = student_info.letter_grade()

                        #save changes
                        save(self.students)
                    break
            else:
                #if no student found
                print("There is no student with that ID number.")
        else:
            #if no students at all
            print("There are no students yet.")   

    #find student
    def find(self):
        #if there are students
        if self.students != []:
            print("_____________________________")
            print("| ID | Name | Grade | Letter |")
            for student in self.students:
                print(f"|{student.get('id')}|{student.get('name')}|{student.get('grade')}|{student.get('letter')}|")

            #ask for id
            student_id = input("Input the ID number of the student you would like to select here: ")

            #search for student
            for student in self.students:
                if student["id"] == student_id:
                    #print info
                    print(f"""Name: {student.get('name')}
        Grade Percentage: {student.get('grade')}
        Letter Grade: {student.get('letter')}
        Grades:""")
                    for grade in student["grades"]:
                        print(grade)
                    break
            else:
                #if not found
                print("There is no student with that ID number.")
        else:
            print("There are no students yet.")   

    #class summary
    def class_summary(self):
        #list to store averages
        aver_list = []
        #collect averages from each student
        for student in self.students:
            if student.get("grade") != "N/A":
                aver_list.append(student.get("grade"))

        #if there are averages
        if aver_list != []:
            #calculate class average
            total = sum(aver_list)
            total = round(total/len(aver_list),2)

            #sort list to find lowest and highest
            sorted_list = sorted(aver_list)
            lowest = sorted_list[0]
            highest = sorted_list[-1]

            #print all students
            print("____________________________")
            print("| ID | Name | Grade | Letter |")
            for student in self.students:
                print(f"|{student.get('id')}|{student.get('name')}|{student.get('grade')}|{student.get('letter')}|")

            #print stats
            print(f"""Class Statistics:
              class average- {total}
highes grade- {highest}
lowest grade- {lowest}""")
        else:
            #if no grades exist
            print("No grades available yet.")
