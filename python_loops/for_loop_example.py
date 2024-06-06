
student_heights = input("What are the heights?").split()
print(student_heights)
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
number_of_students = 0
for n in range (len(student_heights)):
  number_of_students+=1
#print(number_of_students)
sum = 0
for student_height in student_heights:
  sum+=student_height
average = sum/len(student_heights)
average = round(average)
print(f"total height = {sum}")
print(f"number of students = {number_of_students}")
print(f"average height = {average}")