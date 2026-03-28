#This is Shape Management including:
#Creating New Shapes
#Compare Shapes
#Sort Shapes

#Planning and Analysis

#creating new shape
#parameters: none
#actions
#ask for the shape they would like to create
#use the classes to create that shape
#Make it into a dictionary
#open the file
#formate the information in the dictionary
#save it
#close the file
#display the atributes in a neat fashion

#compare shapes formating function
#parameters: none
#actions:
#display a list of all the names of the shapes
#ask if they would like to compare perimeter or area
#use that to compare
#print the answer

#compare shapes function
#parameters: name of shape 1, name of shape 2, what to compare
#actions:
#open the file
#get the information to compare
#use if statements to compare
#return formated statement

#sort function
#paramters: none
#call the 
#ask how they want to sort it
#compare each shape by that quality
#display it

#Pseudocode
#import helper
from helper import *
import classes as classes

#create new shape function
def new_shape():
#parameters: none
    #show the options for all the shapes they can create
    print("""---MENU---
          You can choose between creating any of these shapes. Please input the corrisponding number of the shape you choose in the indicated spot.
          1. Rectangle
          2. Square
          3. Circle
          4. Triangle""")
    #ask which they would like to create
    choice = input("Please input your choice here: ")
    #create a dictionary
    dicti = {}
    #if it is a rectangle
    if choice == "1":
        #ask for the necessary information then add that information to the dictionary
        #create a rectangle with the rectangle class
        #ask for a name
        dicti["type"] = "rectangle"
        dicti["name"] = input("Please give you shape a name and input it here: ")
        dicti["length 1"] = pos_num_sanitation(input("Put the first side length value here: "))
        dicti["length 2"] = pos_num_sanitation(input("Put the second side length value here: "))
        rectangle = classes.Rectangle(dicti.get("name"),dicti.get("length 1"),dicti.get("length 2"))
        dicti["perimeter"] = rectangle.perimeter()
        dicti["area"] = rectangle.area()
        print(rectangle)
        #formate it while including that it is a rectangle
        #the add the name as a value to the name key in the dictionary
        #get the perimeter with the perimeter method then add it as a value
        #do the same for area
    #do this same thing for each of the shapes
    elif choice == "2":
        dicti["type"] = "square"
        dicti["name"] = input("Please give you shape a name and input it here: ")
        dicti["length"] = pos_num_sanitation(int(input("Put the side length value here: ")))
        square = classes.Square(dicti.get("name"),dicti.get("length"))
        dicti["perimeter"] = square.perimeter()
        dicti["area"] = square.area()
        print(square)
    elif choice == "3":
        dicti["type"] = "circle"
        dicti["name"] = input("Please give you shape a name and input it here: ")
        dicti["radius"] = pos_num_sanitation(input("Put the radius length value here: "))
        circle = classes.Circle(dicti.get("name"),dicti.get("radius"))
        dicti["diameter"] = circle.diameter()
        dicti["perimeter"] = circle.perimeter()
        dicti["area"] = circle.area()
        print(circle)
    elif choice == "4":
        dicti["type"] = "triangle"
        dicti["name"] = input("Please give you shape a name and input it here: ")
        dicti["length 1"] = pos_num_sanitation(int(input("Put the first part of the length of the base  value here: ")))
        dicti["length 2"] = pos_num_sanitation(int(input("Put the second part of the length of the base value here: ")))
        dicti["height"] = pos_num_sanitation(int(input("Put the value of the length of the height of the triangle here: ")))
        triangle = classes.Triangle(dicti.get("name"),dicti.get("length 1"),dicti.get("length 2"), dicti.get("height"))
        dicti["perimeter"] = triangle.perimeter()
        dicti["area"] = triangle.area()
        print(triangle)
    #formate the information in dictionary to display
    #formate the information in dictionary to put in the file
    #with open the file to append
    with open("Individual_projects/geomentric_calculator/docs/shapes.txt","a") as file:
        #append the formated infomation
        for item in dicti.values():
            file.write(f"{item}\n")
        file.write("\n")


#compare shapes formating function
def compare_shapes_formating():
#parameters: none
    #call the list making function
    shape_list = list_creation()
    #num is 1
    num = 1
    #show some opening message
    print("This is shape comparison. You can choose between two things to compare then choose two shapes to compare.")
    #for each of dictionaries
    for thing in shape_list:
        #grab some of the info
        #formate it
        #show it with a corrisponding number
        print(f"""{num}. {thing.get("type")} {thing.get("name")}
Perimeter- {thing.get("perimeter")}
Area- {thing.get("area")}\n""")
        #add 1 to num
        num += 1
    #ask for the first shape they would like to compare by the number
    choice_1 = int(input("Please input the number of the first shape to compare: "))
    #ask for the second shape they would like to compare by the number
    choice_2 = int(input("Please input the number of the second shape to compare: "))
    #make sure they are valid inputs
    #ask what if they would like to compare area or perimeter by entering a corrisponding number
    print("You can choose to compare perimeter or area. If you choose perimeter pick 1. If you choose area pick 2.")
    choice_3 = input("Input the number corrisponding to your choice here: ")
    if choice_3 == "1":
        comparing = "perimeter"
    elif choice_3 == "2":
        comparing = "area"
    name_1 = choice_1 - 1
    name_2 = choice_2 - 1
    #call the compare function
    result = compare(shape_list,name_1,name_2,comparing)
    #tell them that the one that was returned has a greater (perimeter or area) and by how much
    print(f"Shape {result[0]} is greater by {result[1]}")

#compare function
def compare(shape_list, index_1,index_2,comparing):
#parameters: shape_list, name of shape 1, name of shape 2, comparing
    #if comparing perimeter then get the perimeter value
    if comparing == "perimeter":
        peri_1 = shape_list[index_1]["perimeter"]
        peri_2 = shape_list[index_2]["perimeter"]
        if peri_1 > peri_2:
            difference = peri_1 - peri_2
            top = shape_list[index_1]["name"]
        elif peri_2 > peri_1:
            difference = peri_2 - peri_1
            top = shape_list[index_2]["name"]
        else:
            list_result = ["both", 0]
    #if comparing area then get the area value
    elif comparing == "area":
        area_1 = shape_list[index_1]["area"]
        area_2 = shape_list[index_2]["area"]
        if area_1 > area_2:
            difference = area_1 - area_2
            top = shape_list[index_1]["name"]
        elif area_2 > area_1:
            difference = area_2 - area_1
            top = shape_list[index_2]["name"]
        else:
            list_result = ["both", 0]
    #then use a conditional to see which is greater
    #subtract the bigger form the smaller
    #round it with round() 2 places
    difference = round(difference,2)
    list_result = [top, difference]
    #return a list with the larger shape, amount it is bigger
    return list_result


#sorting function
def sorting():
#parameters: none
    #call list function
    shape_list = list_creation()
    #show them the options of what to sort by( perimeter, area)
    print("This is sorting. Would you like to sort the shapes by perimeter or area? If perimeter the put 1. If area input 2.")
    choice = input("Input your choice here: ")
    #if sorting by perimeter use the sorting function to sort it by perimeter
    if choice == "1":
        new_shape_list = sorted(shape_list, key=lambda x: x["perimeter"], reverse=True)
    #do the same for area
    elif choice == "2":
        new_shape_list = sorted(shape_list, key=lambda x: x["area"], reverse=True)
    else:
        print("Invalid choice.")
        return
    #show some sort of opening message
    print("This is the sorted list:")
    num = 1
    #for each dictionary in the sorted list
    for item in new_shape_list:
        #formate it and print it
        print(f"""{num}. {item.get("type")} {item.get("name")}
Perimeter- {item.get("perimeter")}
Area- {item.get("area")}
""")
        num += 1









