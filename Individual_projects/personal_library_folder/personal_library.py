#AB 1st Personal library
#Project Analysis
#Books
#list
# book name and the author

#Adding new items
#necessary info: new item name and author
#actions:
#get name
#get author
#format it to put in the list
#put in list
#confirm what they added

#search items
#necessary info: defining trait for search
#actions:
#have user choose which trait to use
#search list based on that
#tell user which books match the search

#remove items
#info: get the number of the item to be removed
#actions:
#show all possible items
#confirm it is the right item
#remove item

#Pseudocode
#books = main funtion

#view function
#parameters are the book list
#result is an empty list
#for each of the tuples in book list
#format it 
#add it to result
#return result

#add item function
#parameters book info list
#print instructions
#new_name = input new name
#first, last = new_name.split(" ")
#print instruction
#new_title = input new title
#add a tuple of the names and title to books list
#return books

#remove items funtion
#parameters book info list
#show all the names of the books and there authors and have them numbered
#choice = the number of the book they want to remove
#remove the book by taking the number choice subtracting 1 and poping that index
#return books list

#search items function
#intake books list
#choice = input ask it they want to search by author or title
#searching = ask what it is they are looking for
#result = []
#use nested for loops to check the information in by books list to see if it matches the search
#for item in range(books):
    #for info in range(books[item])
        #if info == searching
            #result += item
        #else:
            #continue
#use conditionals to check if there is a result
#if ther was a result use a for loop to formate the info in a new list
#return that list

#main function
#books list
#while loop
#print all the options with a number
#choice = choice of what to do
#if choice is 1
    #print(view function)
#elif choice is 2
    #result = run add function
#elif choice is 3
    #result = run remove function
#elif choice is 4
    #print search function
#elif choice is 5
    #print message about personal library
    #break
#else:
    #print invalid choice
    #continue
#books = result
#after while loop
#return books



#Code
#view function
def view(books):
#parameters are the book list
#result is an empty list
    result = ""
#for each of the tuples in book list
    for i in range(len(books)):
#format it 
        title = books[i][0]
        first = books[i][1]
        last = books[i][2]
        result += f"{title} by {first} {last}\n"
#add it to result
#return result
    return result

#add item function
def add(books):
#parameters book info list
#print instructions
    print("Please input the first and last name of the author and title of the book. ")
#new_name = input new name
    first = input("First name: ").strip().title()
    last = input("Last name: ").strip().title()
#print instruction
#new_title = input new title
    title = input("Title: ").strip().title()
    print(f"You add {title} by {first} {last}")
#add a tuple of the names and title to books list
    books.append((title,first,last))
    
#return books
    return books

#remove items funtion

def remove(books):
#parameters book info list
#show all the names of the books and there authors and have them numbered
    result = ""
    num = 1
    for i in range(len(books)):
        title = books[i][0]
        first = books[i][1]
        last = books[i][2]
        result += f"{num}. {title} by {first} {last}\n"
        num += 1
    print(result)
#choice = the number of the book they want to remove
    print("Please input the number of the item you would like to remove")
    choice = int(input("Number: "))
#remove the book by taking the number choice subtracting 1 and poping that index
    removed_books = books.pop(choice-1)
    print(f"You removed {removed_books[0]} by {removed_books[1]} {removed_books[2]}")
  
#return books list
    return books

#search items function
def search(books):
#intake books list
    print("How would you like to search for the specified book:\n" \
    "1. Author's first name\n" \
    "2. Author's last name\n" \
    "3. Title ")
#choice = input ask it they want to search by author or title
    choice = int(input("Number: "))
#searching = ask what it is they are looking for
    searching = input("Input the information you selected of the book you are trying to find :")
#result = ""
    result = ""
#use nested for loops to check the information in by books list to see if it matches the search
    num = 0
    if choice == 1:
        num = 1
    elif choice == 2:
        num = 2
    elif choice == 3:
        num = 0
    for item in range(len(books)):
        if books[item][num].lower() == searching.lower():
            result += f"{books[item][0]} by {books[item][1]} {books[item][2]}\n"
        else:
            continue
        
#use conditionals to check if there is a result
    if result != "":
        return result
    else:
        return "Sorry, there is nothing that matches that search."
#if there was a result use a for loop to formate the info in a new list
#return that list

#main function
def main():
    books = []
#while loop
    while True:
        if books != []:
    #print all the options with a number
            print("This is a personal library manager. Here are you options:\n" \
            "1. View\n"
            "2. Add\n" \
            "3. Remove\n" \
            "4. Search\n" \
            "5. Exit\n" \
                )
            choice = int(input("Number: "))
        else:
            print("This is a personal library manager. Here are you options:\n" \
            "1. Add\n" \
            "2. Exit")            
    #choice = choice of what to do
            choice = int(input("Number: "))
            if choice == 1:
                choice = 2
            elif choice == 2:
                choice = 5
#if choice is 1
        if choice == 1:
    #print(view function)
            print(view(books))
#elif choice is 2
        elif choice == 2:
    #result = run add function
            result = add(books)
#elif choice is 3
        elif choice == 3:
    #result = run remove function
            result = remove(books)
#elif choice is 4
        elif choice == 4:
    #print search function
            print(search(books))
#elif choice is 5
        elif choice == 5:
            print("Thank you for using your personal library.")
            break
#else:
        else:
    #print invalid choice
            print("Invalid choice. Choose again.")
    #continue
            continue
#books = result
        if choice in [2,3]:
            books = result
#after while loop
#return books
    return books

main()