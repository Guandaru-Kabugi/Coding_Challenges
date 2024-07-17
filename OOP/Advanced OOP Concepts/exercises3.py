import random
names = [
    'michael',
    'ernest',
    'stephen',
    'daniel'
]
class Student:
    count = 0
    def __init__(self, name, age, course):
        self._name = name
        self.age = age
        self.course = course
        Student.count+=1
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if new_name not in names:
            raise ValueError(f"{new_name} not found in the list")
        else:
            self._name = new_name
    @staticmethod
    def random_student():
        return random.choice(names)
    @classmethod
    def count_number_students(cls):
        return cls.count


student1 = Student('Alex', 27, 'BE')
student1 = Student('Ernest', 25, 'BaE')
student1 = Student('Dnaiel', 24, 'BSE')
student1.name = 'ernest'
ta = Student.random_student()
print(ta)
# print(student1.name)
print(Student.count)