Groceries = ["Milk", "Oranges", "Bananas", "Avocado", "Onions", "Grapes", "Spinach", "Bell Pepper","Tomatoes", "Cauliflower"]
#Groceries = []
#Groceries.append("Oranges")
#Groceries.append("Milk")
#Groceries.append("Bananas")
#print(Groceries)
Item = input("What item do you want from our store? ")
if Item in Groceries:
    print("What quantity do you want for your item? ")
else:
    print("Sorry, we don't have that item in our store.")