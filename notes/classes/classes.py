#AB 1st Classes notes

#example 1
class Animal:
    def __init__(self, name, species, age):
        self.name = name.capitalize()
        self.species = species.capitalize()
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}"
    
    def birthday(self):
        self.age += 1

dog = Animal("Doug", "dog", 4)
print(dog)

bunny = Animal("Gorilla", "bunny", 1)
print(bunny)

dog.birthday()

#example 2
class ClassPeriod:
    def __init__(self, subject, teacher= "Ms. LaRose", room = None):
        self.subject = subject.capitalize()
        self.teacher = teacher
        self.room = room

    def __str__(self):
        return f"Subject: {self.subject}\nTeacher:{self.teacher}\nRoom: {self.room}"
    
