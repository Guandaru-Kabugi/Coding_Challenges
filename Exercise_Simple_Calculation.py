import time

First_Number = int(input("Give me the first number of your choice: "))
#print(type(First_Number))
time.sleep(1.5)
Second_Number = int(input("Give me the second number of your choice: "))
#print(type(Second_Number))
time.sleep(1.5)
Total = First_Number + Second_Number
time.sleep(1.5)
#remember that str comes after the plus and followed by a bracket
print("The sum is: " + str (Total))
