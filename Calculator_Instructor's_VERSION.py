def print_instructions ():
    print("Welcome to the calculator.")
    print("Provide 2 numbers and then an operator.")

def add_2_numbers(number_1, number_2):
    return number_1 + number_2

def subtract_2_numbers(number_1, number_2):
    return number_1 - number_2

def multiply_2_numbers(number_1, number_2):
    return number_1 * number_2

def divide_2_numbers(number_1, number_2):
    return number_1 / number_2

print_instructions()
number_1 =float(input ("Number 1: ?"))
number_2 =float(input ("Number 2: ?"))
operation = int(input("Operation type? (1 for addition, " +\
                 "2 for subtraction, 3 for multiplication," +\
                  "4 for division "))
if operation ==1:
    result=add_2_numbers(number_1, number_2)
elif operation==2:
    result=subtract_2_numbers(number_1, number_2)
elif operation ==3:
    result=multiply_2_numbers(number_1, number_2)
elif operation ==4:
    if number_2==0:
        print("Error: division by zero")
        exit()
    result=divide_2_numbers(number_1, number_2)
else:
    print("Error: unknown operation")
    exit()
print("The final results: {:.2f}".format (result))