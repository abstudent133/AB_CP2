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

#create new shape function
#parameters: none
    #show the options for all the shapes they can create
    #ask which they would like to create
    #if it is a rectangle
        #create a dictionary
        #ask for the necessary information then add that information to the dictionary
        #create a rectangle with the rectangle class
        #ask for a name
        #formate it while including that it is a rectangle
        #the add the name as a value to the name key in the dictionary
        #get the perimeter with the perimeter method then add it as a value
        #do the same for area
    #do this same thing for each of the shapes
    #formate the information in dictionary to display
    #formate the information in dictionary to put in the file
    #with open the file to append
        #append the formated infomation


#compare shapes formating function
#parameters: none
    #call the list making function
    #num is 1
    #show some opening message
    #for each of dictionaries
        #grab some of the info
        #formate it
        #show it with a corrisponding number
        #add 1 to num
    #ask for the first shape they would like to compare by the number
    #ask for the second shape they would like to compare by the number
    #make sure they are valid inputs
    #ask what if they would like to compare area or perimeter by entering a corrisponding number
    #call the compare function
    #tell them that the one that was returned has a greater (perimeter or area) and by how much

#compare function
#parameters: name of shape 1, name of shape 2, comparing
    #call the list making function
    #go through each of the dictionaries and search for the name of shape 1
    #do the same for shape 2
    #if comparing perimeter then get the perimeter value
    #if comparing area then get the area value
    #then use a conditional to see which is greater
    #subtract the bigger form the smaller
    #round it with round() 2 places
    #return a list with the larger shape, amount it is bigger

#sorting function
#parameters: none
    #call list function
    #show them the options of what to sort by(shape, perimeter, area)
    #if sorting by shape then sort the list by rectangle, square, circle, triangle
    #if sorting by perimeter use the sorting function to sort it by perimeter
    #do the same for area
    #show some sort of opening message
    #for each dictionary in the sorted list
        #formate it and print it









