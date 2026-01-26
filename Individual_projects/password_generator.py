#AB 1st Password Generator
#Project Analysis
#lower case
#actions
#generate a random number between 97 and 122
#get that letter based on ascii

#upper case
#actions
#generate a random number between 65 and 90
#get the letter based on ascii

#special character
#actions
#generate a random number between 33 and 47,58 and 64
#get that symbol in ascii

#number
#actions
#generate random number betweem 48 and 57
#get that number based on ascii

#length
#actions
#ask for length
#set the length to that

#determine number of each
#actions
#for each determine a percentage
#multipy the length by that individual percentages
#round each

#arrangement
#actions
#find a random place for how ever many of each thing
#make sure no 2 are in the same place

#Psuedocode
#import random
import random

#print intro to explain program
print("Hello! This is a Password Generator.")
print("You will choose password requirements and receive 4 passwords based on those requirements.")


#random function
#intake the range and if it a character(char) or just a random number(numb)
def random_value(start, end, value_type):

    #num is a random integer between the numbers of range
    num = random.randint(start, end)

    #if type is "char"
    if value_type == "char":
        #character is chr(num)
        return chr(num)

    #else
    else:
        #character = num
        return str(num)


#character function
#intake what types of characters are allowed
def build_character_list(lower, upper, numbers, special):

    #characters list starts empty
    characters = []

    #if lowercase allowed add lowercase ascii
    if lower:
        for i in range(97, 123):
            characters.append(chr(i))

    #if uppercase allowed add uppercase ascii
    if upper:
        for i in range(65, 91):
            characters.append(chr(i))

    #if numbers allowed add number ascii
    if numbers:
        for i in range(48, 58):
            characters.append(chr(i))

    #if special allowed add special ascii
    if special:
        for i in range(33, 48):
            characters.append(chr(i))

    #return characters list
    return characters


#generator function
#intake length and character list
def generate_password(length, characters):

    #password list starts empty
    password = []

    #for each position in length
    for i in range(length):

        #choose a random character from list
        #append to password
        password.append(random.choice(characters))

    #return password as a string
    return "".join(password)


#main function
def main():

    #loop menu until user exits
    while True:

        #print menu options
        print("\nMAIN MENU")
        print("1. Generate Passwords")
        print("2. Exit")

        #choice = user menu selection
        choice = input("Choose an option: ").strip()

        #if choice is generate passwords
        if choice == "1":

            #ask for password length
            length = int(input("How long does the password need to be: "))

            #ask for character requirements
            lower = input("Lowercase letters (Y/N): ").upper() == "Y"
            upper = input("Uppercase letters (Y/N): ").upper() == "Y"
            numbers = input("Numbers (Y/N): ").upper() == "Y"
            special = input("Special characters (Y/N): ").upper() == "Y"

            #build character list based on choices
            characters = build_character_list(lower, upper, numbers, special)

            #if no character types selected
            if len(characters) == 0:
                print("You must select at least one character type.")
                continue

            #print password header
            print("\nPossible Passwords:\n")

            #generate 4 passwords
            for i in range(4):
                print(generate_password(length, characters))

        #if choice is exit
        elif choice == "2":
            break

        #if invalid option
        else:
            print("Invalid option.")

    #end message
    print("Thank you for using the password generator.")


#run program
main()
