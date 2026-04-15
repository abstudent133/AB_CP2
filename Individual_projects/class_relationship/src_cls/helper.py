#Helper functions
#Planning and Analysis
#convert list
#parameters: item, string_or_list
#actions:
#if the second parameter is string
#take the string and convert it to a list again
#vice versa for the list

#save stuff
#parameters: list of students
#actions:
#open the file
#for each of the students in the list
#formate the information 
#for the list of grades call convert list(list of grades, list)
#save it to the csv

#positive number
#parameters:number
#actions:
#use conditional to check if positive
#if positve return the number
#if not then show that it isn't valid
#start a while loop
#ask then to input a new positive number
#if not positive then restart the loop
#if it is then return that number

#get current students
#parameters:none
#acions:
#open the file
#get the header(so it isn't used)
#get the value from each line and turn it into a dictionary
#add that dictionary to a list

#Pseudocode
#import csv
import csv

#convert list function
def convert_list(item, type):
#parameters: item, type
    #if converting string to list
    if type == "string":
        result = item.split(",")
    #if converting list to string
    elif type == "list":
        result = ",".join([str(i) for i in item])
    #return result
    return result

#load students from csv into list of dictionaries
def load_students():
#parameters: none
    #create empty list
    students = []
    try:
        #open file
        with open("Individual_projects/class_relationship/docs/student.csv","r") as file:
            reader = csv.DictReader(file)
            #loop through each row
            for row in reader:
                #convert grades string into list
                grades = convert_list(row["grades"], "string")

                #convert grades into float list
                grade_list = []
                for grade in grades:
                    if grade != "":
                        grade_list.append(float(grade))

                #create dictionary for student
                student_dict = {
                    "id": row["student id"],
                    "name": row["student name"],
                    "grade": float(row["grade percentage"]) if row["grade percentage"] != "" else "N/A",
                    "letter": row["letter grade"],
                    "grades": grade_list
                }
                #add to list
                students.append(student_dict)
    except:
        #if file doesn't exist return empty list
        students = []
    return students

#save function
def save(students):
#parameters: list of students
    #open file to write
    with open("Individual_projects/class_relationship/docs/student.csv","w",newline='') as file:
        writer = csv.writer(file)
        #write header row
        writer.writerow(["student id","student name","grade percentage","letter grade", "grades"])
        #write each student
        for student in students:
            grades = convert_list(student.get("grades"),"list")
            writer.writerow([student.get("id"),student.get("name"),student.get("grade"),student.get("letter"),grades])

#positive number input sanitation
def pos_num_sanitation(num):
#parameters: number
    #convert to float
    num = float(num)
    #if valid
    if num > 0:
        return num
    else:
        #keep asking until valid
        while True:
            print("That was an invalid input. It must be a positive number.")
            new_num = int(input("Please input a new number here: "))
            if new_num > 0:
                return new_num
            else:
                continue

