#remember the value of using indentations to separate each command!
user_country = input(
    "What is your country? (Choose either India, France, Mexico, or South Africa)"
)
user_age = int(input("What is your age?"))
if user_country == "South Africa":
    if user_age >= 17:
        print("You can drive in South Africa!")
    if user_age < 17:
        print("You cannot drive in South Africa!")
elif user_country == "Mexico":
    if user_age >= 18:
        print("You can drive in Mexico!")
    elif user_age >= 16 and user_age < 18:
        print("You can drive with parental agreement in Mexico!")
    elif user_age >= 15 and user_age < 16:
        print("You can drive with parental supervision in Mexico!")
    else:
        print("You cannot drive in Mexico!")
elif user_country == "India":
    if user_age >= 18:
        print("You can drive in India!")
    else:
        print("You are too young to drive in India!")
elif user_country == "France":
    if user_age >= 18:
        print("You can drive in France")
    if user_age >= 15 and user_age < 18:
        print("You can drive with supervision in France!")
else:
    print("Data not Avaiable for your country!")
print("End of Program")
