class Animal:
  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

animal1 = Dog()
animal2 = Animal()
# animals = [Dog(), Animal()]
animals = [animal1, animal2]
for animal in animals:
  animal.make_sound()  # Output: Woof! (for Dog), Generic animal sound (for Animal)
  
  
class Duck:
    def quack (self):
        return 'Duck Quacks'
class Person:
    def quack (self):
        return "Person imitates duck"
def make_sound (object):
    return object.quack()

duck = Duck()
person = Person()

print(make_sound(duck))
print(make_sound(person))