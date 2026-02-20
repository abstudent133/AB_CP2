#file management

#Project Analysis

#opening file function
#parameters: action(adding, viewing)
#actions:
#if action is adding
#open file
#turn into a string
#clean up
#ask what they want to add
#append it
#if viewing
#open file
#turn into a string
#clean up
#return that string

#update info function
#parameters: time, word count, relative path
#actions:
#take the time and word count and formate them
#open the file
#append the formated stuff
#tell the user it has been updated

#word counter function
#parameters:none
#actions:
#open the file
#read the first part
#count each word as a string separated by a space
#return the count

#relative path function
#parameters: none
#actions
#ask user for relative path
#return relative path


#Pseudocode
#import time management

#open_file function
#parameters: action
    #relative_path = call relative_path_func()
    #if action is view
        #try to open the file with relative path and read as file:
            #read each line and add it to the total string
            #split the huge string at the first enter
            #display the first part that is the part they've writen
        #except if that doesn't work
            #open a file with the relative path and read and write as file
            #display a message about an empty document
    #if action is append
        #ask user what they want to add
        #try to open file with relative path and append as file
            #open read each line and add to the total string
            #split at the first enter
            #append the new stuff to the first part of the split
    #return the string with what the user wrote

#update info function

