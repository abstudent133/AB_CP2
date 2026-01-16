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
#books = list with mini tuples of the book title and author first name and last name

#add item function
#parameters book info list
#new_name = input new name
#first, last = new_name.split(" ")
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




