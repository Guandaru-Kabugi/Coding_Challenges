print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name?")
score_1 = 0
score_2 = 0
Combine_names = name1+name2
lower_case_combined_names = Combine_names.lower()

t = lower_case_combined_names.count('t')
r = lower_case_combined_names.count('r')
u = lower_case_combined_names.count('u')
e = lower_case_combined_names.count('e')
first_digit_of_calculator = t+r+u+e

l = lower_case_combined_names.count('l')
o = lower_case_combined_names.count('o')
v = lower_case_combined_names.count('v')
e = lower_case_combined_names.count('e')
second_digit_of_calculator = l+o+v+e

concatenated_names = str(first_digit_of_calculator) + str(second_digit_of_calculator)
concatenated_names_int = int(concatenated_names)

if concatenated_names_int<10 and concatenated_names_int>90:
    print(f"Your score is {concatenated_names_int}, you go together like coke and mentos.")
elif concatenated_names_int>=40 and concatenated_names_int<=50:
    print(f"Your score is {concatenated_names_int}, you are alright together.")
else:
    print(f"Your score is {concatenated_names_int}.")