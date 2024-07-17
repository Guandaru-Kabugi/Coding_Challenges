class Shape:
    def __init__(self, Length, Width) -> None:
        self.length = Length
        self.width = Width
    def calculate_area(self):
        return self.length * self.width
    
class Rectangle(Shape):
    def __init__(self, Length, Width) -> None:
        super().__init__(Length, Width)
    # def calculate_area(self):
        
        # return super().calculate_area()
shape1 = Rectangle(2,4)
print(shape1.calculate_area())

class Bird:
    def fly (self):
        return 'flying.....'
class Mammal:
    def run(self):
        return 'running......'
class Bat(Mammal, Bird):
    pass
bat = Bat()
print(bat.fly())
print(bat.run())

class Dog:
    def make_sound(self):
        return "Barking woof woof..."
class Cat:
    def make_sound(self):
        return "meow meoew...."
class Horse:
    def make_sound(self):
        return "neigh neigh..."
class Bird:
    def make_sound(self):
        return "chirping ..."

def let_them_speak(*args):
    for object in args:
        print(object.make_sound()) 

let_them_speak(Dog(), Cat(), Horse(), Bird())
