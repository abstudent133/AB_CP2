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
    #if item type is a string
    if type == "string":
        #split the item with a split function
        result = item.split(",")
    #if item type is a list
    elif type == "list":
        #use the join function to join all the grades
        result = ",".join(item)
    #return the converted value
    return result

#save function
def save(students):
#parameters: list of students
    #with open the file as file
    with open("Individual_projects/class_relationship/docs/student.csv","w",newline='') as file:
        writer = csv.writer(file)
        #add the title
        writer.writerow(["student id","student name","grade percentage","letter grade", "grades"])
        #for each student in the list of students
        for student in students:
            #add the student to the csv
            grades = convert_list(student.get("grades"),list)
            writer.writerow([student.get("id"),student.get("name"),student.get("grade"),student.get("letter"),grades])

#positive number input sanitation
def pos_num_sanitation(num):
#parameters: number
    #if the number is greater than 0 return the number
    num = float(num)
    if num > 0:
        return num
    #else
    else:
        #while true
        while True:
            #tell the user that that was an invalid input
            print("That was an invalid input. It must be a positive number.")
            #ask then for a new positive number
            new_num = int(input("Please input a new number here: "))
            #if the number is greater than 0 then return the number
            if new_num > 0:
                return new_num
            #else:
            else:
                #continue
                continue
