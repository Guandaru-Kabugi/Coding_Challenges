from menu import menu

print("Welcome to the Coffe-Maker Machine")
request = input("What would you like? (espresso/latte/cappuccino): ")
print (request)
starting_measure_of_ingredients ={
        'water':300,
        'coffee':100,
        'milk':200, 
}

if request == 'latte':
    requirements = menu[1]['ingredients']
    print (requirements)
    for item in starting_measure_of_ingredients:
        starting_measure_of_ingredients[item]-= menu[1]['ingredients'][item]
    print(starting_measure_of_ingredients)
    print("Here is your coffee ☕. Enjoy")
elif request == 'cappucino':
    requirements = menu[2]['ingredients']
    print (requirements)
    for item in starting_measure_of_ingredients:
        starting_measure_of_ingredients[item]-= menu[2]['ingredients'][item]
    print(starting_measure_of_ingredients)
    print("Here is your coffee ☕. Enjoy")    
elif request == 'espresso':
    requirements = menu[0]['ingredients']
    print (requirements)
    for item in starting_measure_of_ingredients:
        starting_measure_of_ingredients[item]-= menu[0]['ingredients'][item]
    print(starting_measure_of_ingredients)
    print("Here is your coffee ☕. Enjoy")