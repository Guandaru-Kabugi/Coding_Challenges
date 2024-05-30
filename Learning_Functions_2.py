def Double_Number (Number):
    return Number * 2
print(Double_Number(2))

def get_user_name ():
    return input("What is your name? ")
    #return User_Name
def get_user_age ():
    return input("What is your age? ")
def welcome_user (name,age):
    print("Hello " + name)
    print("You are " + (age) + " years old. Welcome.")


name = get_user_name()
age = get_user_age()
welcome_user(name,age)
    