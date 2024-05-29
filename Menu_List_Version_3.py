import time

menu_list = [
    "pizza", "burger", "soda", "milk", "yoghurt", "chocolate", "chips",
    "samosa"
]
order_list = []
total_price = 0
print("Hello, welcome to the restaurant!")
print("Here is the menu: ")
for i, index in enumerate(menu_list):
    print(str(i + 1), str(index))
continue_numbering = True
while continue_numbering:
    answer = print("Would you like to order? (yes or no)")
    answer = input().lower()
    if answer == "yes":
        print("What would you like to order? (1-8)")
        order = input()
        order_index = int(order) - 1
        order_list.append(menu_list[order_index])
        total_price += 10
    if answer == "no":
        #break
        continue_numbering = False
if total_price == 0:
    print("Thank you for your interest in our services")
elif total_price > 0:
    answer = input("Would you like to tip? (yes or no)").lower()
    if answer == "yes":
        tip = float(input("How much would you like to tip? (2-25%) "))
        total_price = total_price + (total_price * (float(tip) / 100))
        print("Thank you for your order!")
        time.sleep(1)
        print("You need to pay {: .2f} dollars".format(total_price))
        # print(f"You need to pay {total_price: .2f} dollars.")
        time.sleep(1)
        print("Here is your order list: ")
        time.sleep(1)
        print(order_list)
    if answer == "no":
        print("Thank you for your order!")
        time.sleep(1)
        print("You need to pay " + str(total_price) + " dollars.")
        time.sleep(1)
        print("Here is your order list: " + str(order_list))
