#Main
#four projects are movie recommender, geometeric calculator, class relationships, and morse code translator


#import graphics
from graphics_tkinter import *
import geomentric_calculator.src.main
import movie_recomender_folder.movie_recommeder
import class_relationship.src.main
import morse_code

#main function
def main_portfolio():
    #show them the projects
    while True:
        show("This is my personal project portfolio!")
        menu = Menu(["Movie Recommender","Geometric Calculator","Simple Gradebook","Morse Code Translator","Exit"]).use()
        #depending on which they choose run that project if they click run project

        if menu == "Movie Recommender":
            stuff = """This was my Movie Recommender project.
            What it does:
            This project intakes specific requirements and recommends a movie, from the vast list of them, and gives you some that meet your requirements
            
            What I learned:
            This was one of my first projects where I had to use a csv file, so I learned how 
            to work with those.
            Challenges:
            -I struggled get some function that interpreted the file to work"""
            show(stuff)
            play = Menu(["Run Program","Exit"]).use()
            if play == "Run Program":
                movie_recomender_folder.movie_recommeder.main()
            else:
                continue
        elif menu == "Geometric Calculator":
            stuff = """This was my Geometric Calculator project.
            What it does:
            This project intakes specific dimensions of shapes and proforms opporations to get other values for that shape. You can create shapes, view saved shapes, compare shapes, sort shapes, and view a formula guide.
            
            What I learned:
            This was one of my first projects where I had to use classes and different relationships between classes, so this project built on my little knowledge of classes.
            
            Challenges:
            -I struggled get some function that interpreted the classes to work
            -It took some effort to figure out the math using python"""
            show(stuff)
            play = Menu(["Run Program","Exit"]).use()
            if play == "Run Program":
                geomentric_calculator.src.main.main()
            else:
                continue
        elif menu == "Simple Gradebook":
            stuff = """This was my Simple Gradebook project.
            What it does:
            This project manages the grade of students for a class by using classes. In this program you can add new students, add grades to students, view all students, find a specific student, and view class summary.
            
            What I learned:
            This was one of my first projects where I had to use classes and different relationships between classes, so this project built on my little knowledge of classes.
            
            Challenges:
            -I struggled get some function that interpreted the classes to work"""
            show(stuff)
            play = Menu(["Run Program","Exit"]).use()
            if play == "Run Program":
                class_relationship.src.main.main()
            else:
                continue
        elif menu == "Morse Code Translator":
            stuff = """This was my Morse Code Translating project.
            What it does:
            This project translates English to morse code and back again.
            
            What I learned:
            I learned a lot about morse code and using indexes of different lists to translate information.
            
            Challenges:
            -I struggled with understanding morse code at first"""
            show(stuff)
            play = Menu(["Run Program","Exit"]).use()
            if play == "Run Program":
                morse_code.main()
            else:
                continue
        elif menu == "Exit":
            show("Thank you for using my personal portfolio program!")
            break

main_portfolio()


