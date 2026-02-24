#AB 1st Word Counter Main

#Pseudocode
#import file_management
import file_management

#main
def main():
#parameters: none
    #show menu
    print("""Main Menu
          1. Update Document
          2. View Document
          3. Add to Document""")
    #call the relative_path_func
    relative_path = file_management.relative_path_func()
    #while true
    while True:
        #show menu
        print("""Main Menu
          1. Update Document
          2. View Document
          3. Add to Document
          4. Exit""")
        #choice is ask user to input the number of their choice
        choice = input("Input the number of the action you would like to complete: ")
        #if choice is 1 then result is file_management.update_info_func with relative_path
        if choice == "1":
            file_management.update_info(relative_path)
        #if choice is 2 then result is file_management.open_file with relative_path and read
        elif choice == "2":
            file_management.open_file("view", relative_path)
        #if choice is 3 then result is file management.open_file with relative_path and add
        elif choice == "3":
            file_management.open_file("append", relative_path)
        #if choice is 4 then exit
        elif choice == "4":
            break
        #else have them choose again
        else:
            print("Invalid choice choose again.")

main()
