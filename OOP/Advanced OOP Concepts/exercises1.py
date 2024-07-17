class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('__del__ was called')


# if __name__ == '__main__':
#     person = Person('John Doe', 23)
#     person = None
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self) -> str:
        return f"Book by {self.author} is called {self.title} and has {self.pages}"
    def __repr__(self) -> str:
        return f"Book: (Author = {self.author}, Title = {self.title}, Pages = {self.pages})"
book1 = Book('Wall Speaks', 'Jerr', 200)
print(str(book1))
print(repr(book1))

class Animal:
    def __init__(self, eat, sleep):
        self.eat = eat
        self.sleep = sleep
    def sound(self):
        return 'uuwi'

class Dog(Animal):
    def __init__(self, eat, sleep):
        super().__init__(eat, sleep)
    def bark (self):
        return 'woof'

dog1 = Dog('meat', 'night')
print(dog1.bark())
dog2 = Animal('meat', 'night')
print(dog2.sound())