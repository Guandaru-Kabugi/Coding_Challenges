class Book:
    total_books = 0
    def __init__(self, name):
        self.name = name
        Book.total_books+=1
    
    def count (cls):
        return cls.total_books
    
book1 = Book('Wall')
book2 = Book('Speaks')
print(Book.total_books)

class Calculator:
    @staticmethod
    def add(a,b):
        return a + b
    @staticmethod
    def multiply(a, b):
        return a * b
nu = Calculator()
print(nu.add(3,5))
print(nu.multiply(3,5))

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def create_child(cls, origin):
        return Person(name=origin, age=0)
    def __str__(self) -> str:
        return f"Your name is {self.name} and your age is {self.age}"


child = Person.create_child('James')
print(child)
