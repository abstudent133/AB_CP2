#Class relationships notes

#Inheritance "Is a"
#Parent Class
class Vehical:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")

#Child Class
class Car(Vehical):
    pass

class Boat(Vehical):
    def move(self):
        print("Sail!")\

class Plane(Vehical):
    def move(self):
        print("Fly!")


car = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "747")

print(car.brand)
print(car.model)
boat.move()
car.move()
plane.move()


# Aggregation "Has a"
class Library:
    def __init__(self,name,cataloge = []):
        self.name = name
        self.cataloge = cataloge

    def add_book(self, book):
        self.cataloge.append(book)

    def remove_boo(self, book):
        if book in self.cataloge:
            self.cataloge.pop(book)
        else:
            print("That book isn't in the library")

    def view_cataloge(self):
        for book in self.cataloge:
            print(book)

class Book:
    def __init__(self, title, author):
        self.title = title.title()
        self. author = author
    def __str__(self):
        return f"{self.title} by {self.author}"
    
lib = Library("Provo Library")

lib.add_book(Book("Way of Kings", "Brandon Sanderson"))
lib.add_book(Book("Fellowship of the Ring", "J.R.R. Tolkien"))
lib.add_book(Book("The Last Battle", "C.S. Lewis"))

lib.view_cataloge()

#Composition