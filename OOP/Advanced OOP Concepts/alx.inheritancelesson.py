class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

lassie = Dog("Lassie")
lassie.make_sound()  # Output: Woof!

class Flyer:
  def fly(self):
    print("Flying...")

class Swimmer:
  def swim(self):
    print("Swimming...")

class Duck(Flyer, Swimmer):
  pass

duck = Duck()
duck.fly()  # Output: Flying...
duck.swim()  # Output: Swimming...

class Vehicle:
  def move(self):
    print("Moving...")

class Car(Vehicle):
  pass

class ElectricCar(Car):
  def charge(self):
    print("Charging...")

tesla = ElectricCar()
tesla.move()  # Output: Moving...
tesla.charge()  # Output: Charging...

#method resolution order (mro)
class A:
    def greet(self):
        return "Hello from class A"

class B(A):
    def greet(self):
        return "Hello from class B"

class C(A):
    def greet(self):
        return "Hello from class C"

class D(B, C):
    pass

# Creating an instance of class D
obj_d = D()
print(obj_d.greet())  # Output: "Hello from class B"