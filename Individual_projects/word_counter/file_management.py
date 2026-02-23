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
#parameters: relative path
    #create the variable time as the time function
    #word_count is word_count_func
    #formate time and word_count into a multi-line string
    #try to open the file with relative path and read+ as file
        #read each line and turn it into a string
        #add to the bottom of that string
        #write over the current file with this one
        #close the file
    #except open a file with relative path and write as file
        #write a new file
        #write the formated word_count and time string
        #close file
    #print that the file was updated and show word count

#word_counter_func
#parameters:relative_path
    #try opening file with relative path as file
        #read the file and turn it into a string
        #split the string at the first enter
        #words is the string the user wrote.split
        #count is len(string)
    #except:
        #count is 0
    #return count

#relative_path_func
#parameters:none
    #tell user what a relative path is 
    #ask user for the relative path
    #return relative path

#Code
#import time management
import time_management

#open_file function
def open_file(action):
#parameters: action
    #relative_path = call relative_path_func()
    relative_path = relative_path_func()
    #if action is view
    if action == "view":
        #try to open the file with relative path and read as file:
        try:
            string = """"""
            with open(relative_path, "r") as file:
            #read each line and add it to the total string
                for line in file:
                    string += line
            #split the huge string at the first enter
            parts = string.split("" \
            "")
            #display the first part that is the part they've writen
            print(parts[0])
        #except if that doesn't work
        except:
            #open a file with the relative path and read and write as file
            with open(relative_path, "w") as file:
            #display a message about an empty document
                print("This is an empty document")
    #if action is append
    elif action == "append":
        #ask user what they want to add
        add_this = input("What would like to add to your document(press enter when you are done): ")
        #open read each line and add to the total string
        with open(relative_path, "r+") as file:
            string = file.read()
        #split at the first enter
            parts = string.split("" \
            "")
        #append the new stuff to the first part of the split
            parts[0].append(add_this)
            for part in parts:
                string_two += part
        #write the new stuff into the file
            file.write(string_two)


#update info function
def update_info(relative_path):
#parameters: relative path
    #create the variable time as the time function
    time = time_func()
    #word_count is word_count_func
    word_count = word_count_func(relative_path)
    #formate time and word_count into a multi-line string
    formate = f"""
    Words: {word_count}
    Last Updated: {time}"""
    #try to open the file with relative path and read+ as file
    try:
        #read each line and turn it into a string
        with open(relative_path, "r+") as file:
            string = """"""
            for line in file:
                string += line
            string_total = string + formate
        #add to the bottom of that string
        #write over the current file with this one
            file.write(string_total)
        #close the file
    #except open a file with relative path and write as file
    except:
        with open(relative_path, "w") as file:
        #write a new file
        #write the formated word_count and time string
            file.write(formate)
        #close file
    #print that the file was updated and show word count
    print(f"File updated. Word count: {word_count}")

#word_counter_func
def word_count_func(relative_path):
#parameters:relative_path
    #try opening file with relative path as file
    try:
        with open(relative_path,"r") as file:
            string = """"""
        #read the file and turn it into a string
            for line in file:
                string += line
        #split the string at the first enter
            parts = string.split("" \
            "")
        #words is the string the user wrote.split
            words = parts[0].split()
        #count is len(string)
            count = len(words)
    #except:
    except:
        #count is 0
        count = 0
    #return count
    return count

#relative_path_func
def relative_path_func():
#parameters:none
    #tell user what a relative path is 
    print("To access your file you must enter the relative path. To do so right click on your file and click the button that says copy relative path.")
    #ask user for the relative path
    relative_path = input("Pleas input that here: ")
    #return relative path
    return relative_path