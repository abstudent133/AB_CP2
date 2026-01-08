#AB 1st Decorator

def decorator(func):
    def wrapper():
        print("Befor calling the funtion.")
        func()
        print("After calling the function.")
    return wrapper

@decorator
def greet():
    print("Hello, world")

greet()

@decorator
def add():
    print(1+1)


add()