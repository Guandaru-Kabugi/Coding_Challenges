from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_item = Menu() #creating an instance of an object
coffee_maker = CoffeeMaker() #creating an instance of an object
money_machine = MoneyMachine() #creating an instance of an object
is_on = True
while is_on:
    user_choice = input("​What would you like? (espresso/latte/cappuccino): ") 
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        report = coffee_maker.report() #I would call this an attribute
        report = money_machine.report() #the right portion of this would be called the methods
    else:
        drink_choice = menu_item.find_drink(user_choice)
        drink_choice.ingredients
        if coffee_maker.is_resource_sufficient(drink_choice):
            if money_machine.make_payment(drink_choice.cost):
                make_coffee = coffee_maker.make_coffee(drink_choice)