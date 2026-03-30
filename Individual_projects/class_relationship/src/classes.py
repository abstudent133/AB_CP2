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
    def __init__(self, id, name, grades_list = []):
        self.id = id
        self.name = name
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
        #make sure it is a valid grade input
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
            for num in self.grades:
                total += num
            #divide the length of the list
            total = round(total/len(self.grades), 2)
            return total
        else:
            total = "N/A"
            
    #letter grade
    def letter_grade(self):
        #intake the average
        aver = self.average()
        #use conditionals based on letter grade list to get the correct letter grade
        grade_letter = ""
        if aver != "N/A":
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
            grade_letter = ""
        return grade_letter

#GradeBook class
class GradeBook:
#parameters:list of students
    #initiate list of students with self
    def __init__(self, students):
        self.students = students
    #add students
    def add_students(self):
        #ask user for student id
        id = input("Enter the new student's id: ")
        #ask user for student name
        name = input("Enter the name of the new student: ")
        new_student= Student(id, name)
        average = new_student.average()
        grades = new_student.grades
        grade_letter = new_student.letter_grade()
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
    #find student
    def add_grade(self):
        #show all the students
        #for each student formate the information in the list in a neat way
        if self.students != {}:
            while True:
                print("____________________________")
                print("| ID | Name | Grade | Letter |")
                for student in self.students:
                    print(f"|{student.get("id")}|{student.get("name")}|{student.get("grade")}|{student.get("letter")} ")
                #ask which student they want from their id
                student_id = input("Input the ID number of the student you would like to select here: ")
                #show information on the student
                for student in self.students:
                    if student["id"] == student_id:
                        print(f"""Name: {student.get("name")}
        Grade Percentage: {student.get("grade")}
        Letter Grade: {student.get("letter")}
        Grades:""")
                        for grade in student["grades"]:
                            print(grade)
                #ask if they would like to add a grade
                        choice = "Would you like to add a grade to this student? If yes input 1 if no input 2 here: "
                #if yes then call the add grade method in student class with the id and name
                        if choice == "1":
                            student_info = Student(student.get("id"), student.get("name"), student.get("grades"))
                            student_info.add_grades()
                    #if no the move on
                        else:
                            break
                    else:
                        print("There is no student with that ID number. Please choose again.")
        else:
            print("There are no students yet.")   
    #add grade
    def find(self):
        if self.students != {}:
            while True:
                print("_____________________________")
                print("| ID | Name | Grade | Letter |")
                for student in self.students:
                    print(f"|{student.get("id")}|{student.get("name")}|{student.get("grade")}|{student.get("letter")} ")
                #ask which student they want from their id
                student_id = input("Input the ID number of the student you would like to select here: ")
                #show information on the student
                for student in self.students:
                    if student["id"] == student_id:
                        print(f"""Name: {student.get("name")}
        Grade Percentage: {student.get("grade")}
        Letter Grade: {student.get("letter")}
        Grades:""")
                        for grade in student["grades"]:
                            print(grade)
                        break
                    else:
                        print("There is no student with that ID number. Please choose again.")
        else:
            print("There are no students yet.")   
    #class summary
    def class_summary(self):
        #get all the average grades of the students
        aver_list = []
        for student in self.students:
            aver_list.append(student.get("grade"))
        #add them
        total = 0
        for thing in aver_list:
            total += thing
        #divide them by the number
        total = round(total/len(aver_list),2)
        #then get the highest and lowest scores and the total number of students
        sorted_list_lowest = aver_list.sort()
        sorted_list_highest = aver_list.sort(reverse=True)
        #display this along with each student
        print("____________________________")
        print("| ID | Name | Grade | Letter |")
        for student in self.students:
            print(f"|{student.get("id")}|{student.get("name")}|{student.get("grade")}|{student.get("letter")} ")
        print(f"""Class Statistics:
              class average- {total}
highes grade- {sorted_list_highest[0]}
lowest grade- {sorted_list_lowest[0]}""")
    



