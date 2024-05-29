



menu_list = ["pizza", "burger", "soda", "milk", "yoghurt", "chocolate", "chips", "samosa"]
order_list = []
total_price = 0
print("Hello, welcome to the restaurant!")
print("Here is the menu: ")
for i, index in enumerate (menu_list):
  print(str(i+1), str(index))
while True:
    print("Would you like to order? (yes or no)")
    answer = input()
    if answer == "yes":
        print("What would you like to order? (1-8)")
        order = input()
        order_list.append(order)
        total_price += 10
    if answer == "no":
        break
if total_price==0:
    print("Thank you for your interest in our services")
else:
    print("Your total price is " + str(total_price) + "$")