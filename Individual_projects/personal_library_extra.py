#Code
#save funtion
def save_books(books):
    file = open("library.txt", "w")
    for book in books:
        file.write(f"{book[0]}|{book[1]}|{book[2]}|{book[3]}|{book[4]}\n")
    file.close()

#load books funtion
def load_books():
    books = []
    try:
        file = open("library.txt", "r")
        for line in file:
            title, first, last, genre, year = line.strip().split("|")
            books.append({"title": title, "first":first,"last": last,"genre": genre,"year": year})
        file.close()
    except FileNotFoundError:
        books = []
    return books
#view function
def view(books):
#parameters are the book list
#result is an empty list
    result = ""
#for each of the tuples in book list
    for i in range(len(books)):
#format it 
        title = books[i]["title"]
        first = books[i]["first"]
        last = books[i]["last"]
        genre = books[i]["genre"]
        year = books[i]["year"]
        result += f"Title:{title} Author:{first} {last} Genre:{genre} Year Created:{year} \n"
#add it to result
#return result
    return result

#add item function
def add(books):
#parameters book info list
#print instructions
    print("Please input the first and last name of the author, the title, the genre, and the year the book was published. ")
    print("If you don't know the information just type N/A.")
#new_name = input new name
    first = input("First name: ").strip().title()
    last = input("Last name: ").strip().title()
#print instruction
#new_title = input new title
    title = input("Title: ").strip().title()
    genre = input("Genre:").strip().title()
    year = input("Year published:")
    print(f"You add: Title:{title} Author:{first} {last} Genre: {genre} Year Published: {year}")
#add a list of the names and title to books list
    books.append((title,first,last,genre,year))
    
#return books
    return books

#remove items funtion

def remove(books):
#parameters book info list
#show all the names of the books and there authors and have them numbered
    result = ""
    num = 1
    for i in range(len(books)):
        title = books[i]["title"]
        first = books[i]["first"]
        last = books[i]["last"]
        genre = books[i]["genre"]
        year = books[i]["year"]
        result += f"{num}. Title:{title} Author:{first} {last} Genre: {genre} Year Published: {year}\n"
        num += 1
    print(result)
#choice = the number of the book they want to remove
    print("Please input the number of the item you would like to remove")
    choice = int(input("Number: "))
#remove the book by taking the number choice subtracting 1 and poping that index
    remove = books.pop(choice-1)
    print(f"You removed: Title:{remove["title"]} Author:{remove["first"]} {remove["last"]} Genre: {remove["genre"]} Year Published: {remove["year"]}")
  
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
        num = "first"
    elif choice == 2:
        num = "last"
    elif choice == 3:
        num = "title"
    for item in range(len(books)):
        if books[item][num].lower() == searching.lower():
            result += f"Title:{books[item]["title"]} Author:{books[item]["first"]} {books[item]["last"]} Genre:{books[item]["genre"]} Year Published:{books[item]["year"]} \n"
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
#books list
    books = load_books()
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
            "6. Delete library" \
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
            save_books(books)
            print("Library saved. Thank you for using your personal library.")
            break
#elif choice is 6:
        elif choice == 6:
            books = []
            save_books(books)
            print("Library reset.")
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