from menu import menu

print("Welcome to the Coffe-Maker Machine")
request = input("What would you like? (espresso/latte/cappuccino): ")
print (request)
starting_measure_of_ingredients ={
        'water':300,
        'milk':200,
        'coffee':100, 
}
print(starting_measure_of_ingredients['water'])
print(starting_measure_of_ingredients['milk'])
print(starting_measure_of_ingredients['coffee'])

print(menu[0]['cost'])

