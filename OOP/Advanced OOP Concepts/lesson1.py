#constructors, destructors, magic methods, inheritance, and composition.
# Constructors (__init__)
# Destructors (__del__)
# Magic Methods (e.g., __str__, __repr__)
#1. Constructors
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

# Create a Point object
point = Point(3, 5)
print(f"Point coordinates: ({point.x}, {point.y})")  # Output: Point coordinates: (3, 5)
#2. Destructors
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')  # Open the file for reading

    def read_data(self):
        return self.file.read()

    def __del__(self):
        self.file.close()  # Close the file when the object is destroyed

# Create an object of FileHandler
file_obj = FileHandler('OOP/Advanced OOP Concepts/sample.txt')
print(file_obj.read_data())
# Object is no longer needed, it will be garbage collected, and __del__ method will be called automatically to close the file
#3. Additional magic methods
class Person:
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    def __repr__(self) -> str:
        return f"Person: Name = {self.name}, Age = {self.age}"


person = Person("Alice", 30)
print(person)  # Output: Name: Alice, Age: 30
print(repr(person))