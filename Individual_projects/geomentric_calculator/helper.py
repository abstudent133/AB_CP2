#these are any helper functions like input sanitation

#Planning and Analysis
#input sanitation
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

#list creation
#paramters: none
#actions:
#create an empty list
#open the file
#for each shape seperated by a space create a dictionary with it's info
#add that dictionary to the list
#return the list


#Pseudocode

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

#list creation function
def list_creation():
#parameters: none
    #create an empty list
    dict_list = []
    dicti = {}
    #with open the file to read
    with open("Individual_projects/geomentric_calculator/docs/shapes.txt","r") as file:
        #read all the information
        string = file.read()
        #separate it into the different shapes and its info
        shape_blocks = string.split("\n\n")
        #for each of those shapes turn its info into a dictionary
        for thing in shape_blocks:
            if not thing.strip():
                continue
            #use a conditional to make the right dictionary for each shape
            parts = thing.split("\n")
            if parts[0]=="rectangle":
                dicti = {"type": "rectangle",
                        "name": parts[1],
                        "length 1": float(parts[2]),
                        "length 2": float(parts[3]),
                        "perimeter": float(parts[4]),
                        "area": float(parts[5])}
            elif parts[0] == "square":
                dicti = {"type": "square",
                        "name": parts[1],
                        "length 1": float(parts[2]),
                        "perimeter": float(parts[3]),
                        "area":float(parts[4])}
            elif parts[0] == "circle":
                dicti = {"type": "circle",
                        "name": parts[1],
                        "radius": float(parts[2]),
                        "diameter": float(parts[3]),
                        "perimeter": float(parts[4]),
                        "area": float(parts[5])}
            elif parts[0] == "triangle":
                dicti = {"type": "triangle",
                        "name": parts[1],
                        "base 1": float(parts[2]),
                        "base 2": float(parts[3]),
                        "length": float(parts[4]),
                        "perimeter": float(parts[5]),
                        "area": float(parts[6])}
            else:
                continue
            dict_list.append(dicti)
            #add it to the list
    #return the list
    return dict_list



