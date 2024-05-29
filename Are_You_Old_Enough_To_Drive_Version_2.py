#remember the value of indentation to ensure each command is excuted separately
country = input(
    "What is your country? (Select from: India, France, Mexico, or South Africa: "
)
if country in {"India", "France", "Mexico", "South Africa"}:
    user_age = int(input("What is your age?"))
    if country == "South Africa":
        if user_age >= 17:
            print("You can drive in South Africa!")
        if user_age < 17:
            print("You cannot drive in South Africa!")
    if country == "Mexico":
        if user_age >= 18:
            print("You can drive in Mexico!")
        if user_age >= 16 and user_age < 18:
            print("You can drive with parental agreement in Mexico!")
        if user_age >= 15 and user_age < 16:
            print("You can drive with parental supervision in Mexico!")
        else:
            print("You cannot drive in Mexico!")
    if country == "India":
        if user_age >= 18:
            print("You can drive in India!")
        else:
            print("You are too young to drive in India!")
    if country == "France":
        if user_age >= 18:
            print("You can drive in France")
        if user_age >= 15 and user_age < 18:
            print("You can drive with supervision in France!")
else:
    print("Data not available in your country!")
print("End of program!")
