

menu_list = ["pizza", "burger", "soda", "milk", "yoghurt", "chocolate", "chips", "samosa"]
order_list = []
total_price = 0
print("Hello, welcome to the restaurant!")
print("Here is the menu: ")
for i, index in enumerate (menu_list):
  print(str(i+1), str(index))
print("Would you like to order? (yes or no)")
if input () == "yes":
    while True:
        print("What do you want to order? (1-8)")
        order = input ()
        order_list.append(order)
        total_price+=10