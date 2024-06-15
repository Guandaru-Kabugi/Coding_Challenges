import os
from art import logo
def addition (n1,n2):
    return n1+n2
def subtraction (n1,n2):
    return n1-n2
def multiplication (n1,n2):
    return n1*n2
def division (n1,n2):
    return n1/n2

operations = {
    "+" : addition,
     "-": subtraction,
     "*": multiplication,
     "/": division         
}
print(logo)
def calculation():
    num_1 = float(input("What is the first number?\n"))
    for key in operations:
            print(key)
    continue_asking = True
    while continue_asking:
        operations_symbol = input("Pick an operation from those above: ")
        num_2 = float(input("What is the next number?\n"))
        calculation_function = operations[operations_symbol]
        answer = calculation_function(n1=num_1, n2=num_2)
        print(f"{num_1} {operations_symbol} {num_2} = {answer}")
        
        check_if_new_operation_needed = input(f"Do you want to continue calculating with {answer}?: y for yes, and n to start a new calculation: ")
        if check_if_new_operation_needed == "y".lower():
            num_1 = answer
        else:
            continue_asking = False
            os.system('cls')
            calculation()
calculation()