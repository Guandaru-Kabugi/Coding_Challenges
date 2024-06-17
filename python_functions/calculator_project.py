

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

# num_1 = int(input("What is the first number?\n"))

# for key in operations:
#     print(key)
# operations_symbol = input("Pick an operation from those above: ")
# num_2 = int(input("What is the second number?\n"))
# calculation_function = operations[operations_symbol]
# answer_1 = calculation_function(n1=num_1, n2=num_2)
# # if operations_symbol == "+":
# #     answer = addition(n1=num_1, n2=num_2)
# # elif operations_symbol == "-":
# #     answer = subtraction(n1=num_1, n2=num_2)
# # elif operations_symbol == "*":
# #     answer = multiplication(n1=num_1,n2=num_2)
# # elif operations_symbol == "/":
# #     answer = division(n1=num_1,n2=num_2)
# #print(answer)
# print(f"{num_1} {operations_symbol} {num_2} = {answer_1}")
# operations_symbol = input("Pick another: ")
# num_3 = int(input("What is the third number?"))
# calculation_function = operations[operations_symbol]
# answer_2 = calculation_function(n1=answer_1,n2=num_3)
# print(f"{answer_1} {operations_symbol} {num_3} = {answer_2}")
continue_asking = True
while continue_asking:
    num_1 = int(input("What is the first number?\n"))
    for key in operations:
        print(key)
    operations_symbol = input("Pick an operation from those above: ")
    num_2 = int(input("What is the second number?\n"))
    calculation_function = operations[operations_symbol]
    answer_1 = calculation_function(n1=num_1, n2=num_2)
    print(f"{num_1} {operations_symbol} {num_2} = {answer_1}")
    check_if_new_operation_needed = input(f"Do you want to continue calculating with {answer_1}?: y for yes and n for no: ")
    if check_if_new_operation_needed == "n".lower():
        continue_asking = False
        print(f"{num_1} {operations_symbol} {num_2} = {answer_1}")
    elif check_if_new_operation_needed == "y".lower():
        operations_symbol = input("Pick another operation: ")
        num_next = int(input("What is the next number?"))
        calculation_function = operations[operations_symbol]
        answer_2 = calculation_function(n1=answer_1,n2=num_next)
        print(f"{answer_1} {operations_symbol} {num_next} = {answer_2}")
    
    