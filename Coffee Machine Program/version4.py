from menu import menu

print("Welcome to the Coffe-Maker Machine")
starting_measure_of_ingredients ={
        'water':300,
        'coffee':100,
        'milk':200, 
}
profit = 0
print(starting_measure_of_ingredients)
def choice_of_drink(request):
    if request == 'latte':
        cost = menu['latte']['cost']
    elif request == 'cappuccino':
        cost = menu['cappuccino']['cost']
    elif request == 'espresso':
        cost = menu['espresso']['cost']
    print(menu[request]['ingredients'])
    for item in starting_measure_of_ingredients:
        starting_measure_of_ingredients[item]-= menu[request]['ingredients'][item]
        
    print(starting_measure_of_ingredients)
    global profit
    global total_pay
    if total_pay == cost:
        print("Here is your coffee ☕. Enjoy") 
        profit+=cost
        return True
    elif total_pay < cost:
        print("Sorry, not enough money")
        return False
    elif total_pay > cost:
        balance = total_pay-cost
        print("Here is your coffee ☕. Enjoy")
        print(f"Here is your balance: {balance: .2f}")
        profit+=cost
        return True
def resource_check (order_ingredient):#here, I was checking to ensure that the order ingredient was not higher than my current store
    for item in order_ingredient:
        if order_ingredient[item] > starting_measure_of_ingredients[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True
def play ():
    global request
    request = input("What would you like? (espresso/latte/cappuccino): ")
    print(request) 
continue_asking = True
while continue_asking:
    play()
    if request == "off":
        continue_asking = False
    elif request == "report":
        print(f"Water: {starting_measure_of_ingredients['water']}ml")
        print(f"Milk: {starting_measure_of_ingredients['milk']}ml")
        print(f"Coffee: {starting_measure_of_ingredients['coffee']}g")
        print(f"Money: ${profit}")
    else:  
        beverage = menu[request]
        if resource_check(beverage['ingredients']): #here, I called the function of checking whether a new order can be made.
            
        
            print("Please insert coins: ")
            quarters = int(input("how many quarters?  "))
            dimes = int(input("how many dimes?  "))
            nickles = int(input("how many nickles?  "))
            pennies = int(input("how many pennies?  "))
            def calculate_coins(quarters,dimes,nickles,pennies):
                total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
                return total
            total_pay = (calculate_coins(quarters,dimes,nickles,pennies))
            choice_of_drink(request=request)
