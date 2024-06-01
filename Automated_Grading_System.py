grade_list = []


def program_instructions():
    print("Hello. Welcome.")  #helps break into lines
    print("The program requires you to input " +\
    "your grade score so that it calculates " +\
    "the average, min, and max")


def grade_input():
    Remain_in_grade_System = True
    while Remain_in_grade_System:
        grade = int(input("What is the grade? (1-10). " +\
                      "input -1 to stop the grade request: "))
        if grade == -1:
            Remain_in_grade_System = False
        elif grade >= 0 and grade <= 10:
            grade_list.append(grade)
        else:
            print("You gave wrong grade. Try again")


def minimum_of_list(Grade_List):
    minimum = Grade_List[0]
    for i in range(len(Grade_List)):
        if minimum > Grade_List[i]:
            minimum = Grade_List[i]
    return minimum


def maximum_of_list(Grade_List):
    maximum = Grade_List[0]
    for i in range(len(Grade_List)):
        if maximum < Grade_List[i]:
            maximum = Grade_List[i]
    return maximum


def average_of_list(Grade_List):
    sum_of_grades = 0
    for grade in Grade_List:
        sum_of_grades += grade
    average = sum_of_grades / len(Grade_List)
    return average


program_instructions()
grade_input()
#remember to include an if to check list greater than zero
if len(grade_list) == 0:
    print("The list is empty")
    exit()
print("The grade list is : " + str(grade_list))
print("The minimum grade is : " + str(minimum_of_list(grade_list)))
print("The maximum grade is : " + str(maximum_of_list(grade_list)))
print("The average grade is : " + str(average_of_list(grade_list)))
#Below shows another way to write the max function
#for grade in Grade_List:
#   if grade < minimum:
#       minimum = grade
#return minimum
#Below shows another way to write the Max function
#def max_of_list (Grade_List):
#maximum = Grade_List[0]
#for grade in Grade_List:
#if grade > maximum:
#maximum = grade
#return maximum
#below shows another way to write the average function
#def average_of_list(Grade_List):
#sum_of_grades = 0
#for i in range(len(Grade_List)):
#sum_of_grades = sum_of_grades + Grade_List[
# i]  #sum of grades+=grade_list[i]

#average = sum_of_grades / len(Grade_List)
#return average
