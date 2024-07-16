#Class Inheritance and Composition:
#1. Inheritance
class Animal:
  def __init__(self, name, origin):
    self.name = name
    self.origin = origin

  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def __init__(self, name, origin, breed):
    super().__init__(name, origin)  # Call parent class constructor
    self.breed = breed

  def make_sound(self):
    print(f"{self.name} is from {self.origin}, belongs to the breed {self.breed} and barks like this: Woof!")

dog = Dog("Buddy", "Canada", "Labrador")
dog.make_sound()  # Output: Woof!
dog2 = Animal("GS", "USA")
dog2.make_sound()

#2. Composition
# Composition is another technique for code reuse \
    # that involves creating objects of one class within another class. \
        # This allows you to combine functionalities from different classes \
            # without directly inheriting from them.
class Car:
  def __init__(self, engine):
    self.engine = engine  # Engine object as an attribute

  def start(self):
    self.engine.start()

class Engine:
  def start(self):
    print("Engine starting...")
car_engine = Engine()
# car_engine.start()
# car = Car(Engine()) #we have both a Car instance and also an Engine instance
# car.start()  # Output: Engine starting...
car = Car(car_engine)
car.start()

