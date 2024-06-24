from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

user_choice = input("​What would you like? (espresso/latte/cappuccino): ")
menu_item = Menu()
coffee_maker = CoffeeMaker()
drink_choice = menu_item.find_drink(user_choice)
drink_choice.ingredients
resource_extent = coffee_maker.is_resource_sufficient(drink_choice)
print(resource_extent)
money_machine = MoneyMachine()
coins_accepted = money_machine.make_payment(drink_choice.cost)
print(coins_accepted)
money_machine.report()
make_coffee = coffee_maker.make_coffee(drink_choice)

