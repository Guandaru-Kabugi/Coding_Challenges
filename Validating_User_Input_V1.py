Groceries = ["Milk", "Oranges", "Bananas", "Avocado", "Onions", "Grapes", "Spinach", "Bell Pepper","Tomatoes", "Cauliflower"]
Item = input("What item do you want from our store? ")
if  Item not in Groceries:
    print("Unfortunately, we do not have that item in stock.")
    exit()
    #we use exit () to end the program
else:
    print("What quantity do you want for your item? ")