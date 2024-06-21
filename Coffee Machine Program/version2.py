from menu import menu

print("Welcome to the Coffe-Maker Machine")
request = input("What would you like? (espresso/latte/cappuccino): ")
print (request)
starting_measure_of_ingredients ={
        'water':300,
        'coffee':100,
        'milk':200, 
}
print(starting_measure_of_ingredients)
def choice_of_drink(request):
    if request == 'latte':
        index = 1
        cost = menu[1]['cost']
    elif request == 'cappuccino':
        index = 2
        cost = menu[2]['cost']
    elif request == 'espresso':
        index = 0
        cost = menu[0]['cost']
    requirements = menu[index]['ingredients']
    print (requirements)
    for item in starting_measure_of_ingredients:
        starting_measure_of_ingredients[item]-= menu[index]['ingredients'][item]
    print(starting_measure_of_ingredients)
    global total_pay
    if total_pay == cost:
        print("Here is your coffee ☕. Enjoy") 
    elif total_pay < cost:
        print("Sorry, not enough money")
    elif total_pay > cost:
        balance = total_pay-cost
        print("Here is your coffee ☕. Enjoy")
        print(f"Here is your balance: {balance: .2f}")

print("Please insert coins: ")
quarters = float(input("how many quarters?  "))
dimes = float(input("how many dimes?  "))
nickles = float(input("how many nickles?  "))
pennies = float(input("how many pennies?  "))
def calculate_coins(quarters,dimes,nickles,pennies):
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total
total_pay = (calculate_coins(quarters,dimes,nickles,pennies))
choice_of_drink(request=request)