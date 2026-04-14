#AB 1st Morse Code Translator
#Project Analysis
#English to Morse
#intake the phrase
#action
#for each of the letters change it to the morse 
#show the user the new message

#Morse to English
#intake the morse
#action
#make sure it is morse
#for each of the morse symbols translate it to english
#format it for proper grammar
#show user

#Code
# create a tuple that holds all english alphabet letters and space
english_letters = (
    "a","b","c","d","e","f","g","h","i","j",
    "k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z"," "
)

# create a tuple that holds the corresponding morse code symbols
morse_code = (
    ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
    "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
    "..-","...-",".--","-..-","-.--","--..","/"
)

# english to morse code function
def english_to_morse(message):
    # make the message lowercase so it matches the tuple
    message = message.lower()

    # create an empty string to store the translated result
    translated_message = ""

    # loop through each character in the message
    for char in message:
        # check if the character exists in the english tuple
        if char in english_letters:
            # find the index of the character
            index = english_letters.index(char)
            # add the corresponding morse code and a space
            translated_message += morse_code[index] + " "
        else:
            # handle characters that are not supported
            translated_message += "? "

    # return the final translated string
    return translated_message.strip()


#morse code to english function
def morse_to_english(code):
    # split the morse code input by spaces
    code_list = code.split(" ")

    # create an empty string to store the translated result
    translated_message = ""

    # loop through each morse code symbol
    for symbol in code_list:
        # check if the symbol exists in the morse tuple
        if symbol in morse_code:
            # find the index of the morse symbol
            index = morse_code.index(symbol)
            # add the corresponding english letter
            translated_message += english_letters[index]
        else:
            # handle invalid morse symbols
            translated_message += "?"

    # return the final translated string
    return translated_message


# main function
def main():
    # introduction to explain what the program does
    print("Welcome to the Morse Code Translator!")
    print("This program can translate English to Morse Code or Morse Code to English.")
    print("Follow the menu options below to choose what you want to do.\n")

    # keep the program running until the user chooses to exit
    while True:
        # display the main menu
        print("MAIN MENU:")
        print("1. Translate from Morse Code to English")
        print("2. Translate from English to Morse Code")
        print("3. Exit\n")

        # ask the user for their choice
        choice = input("Please enter your choice (1, 2, or 3): ")

        # option 1: morse code to english
        if choice == "1":
            print("\nMORSE CODE TO ENGLISH:")
            code = input("What is the code you need translated:\n")
            result = morse_to_english(code)
            print("\nYour message says:\n")
            print(result + "\n")

        # option 2: english to morse code
        elif choice == "2":
            print("\nENGLISH TO MORSE CODE:")
            message = input("What is the message you need translated:\n")
            result = english_to_morse(message)
            print("\nYour message says:\n")
            print(result + "\n")

        # option 3: exit the program
        elif choice == "3":
            print("\nThank you for using the Morse Code Translator. Goodbye!")
            break

        # handle invalid menu choices
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.\n")

#call main
main()