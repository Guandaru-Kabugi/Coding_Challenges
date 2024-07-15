class Student:
    score = 15
    announcement = "Welcome to the Class"

    def __init__(self,grade):
        self.grade = grade
    def add_grade(self):
        self.grade = self.grade + 10
    @classmethod
    def score_add_to_grade(cls):
        cls.score = cls.score + 80
    @classmethod
    def announce_to_class(cls):
        return f"Here is the announcement: {cls.announcement}"


student1 = Student(70)
student2 = Student(67)
student3 = Student(90)
student4 = Student(67)
student5 = Student(80)
list_students = [student1,student2,student3,student4,student5]
print(*(student.grade for student in list_students))
for student in list_students:
    print(student.grade)
    print()
for student in list_students:
    print(Student.announcement)
    print()
