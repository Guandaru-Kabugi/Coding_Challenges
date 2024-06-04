print("Thank you for choosing Python Pizza Deliveries! ")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill =0

if size == 'S'.lower():
    bill += 15
    if add_pepperoni == 'Y'.lower():
        print("pepperoni costs $2")
        bill+=2
    if extra_cheese == 'Y'. lower():
        print("Extra cheese costs $1")
        bill+=1
    print(f"Your final bill is : ${bill}")
if size == 'M'.lower():
    bill = 20
    if add_pepperoni == 'Y'.lower():
        print("pepperoni costs $3")
        bill+=3
    if extra_cheese == 'Y'. lower():
        print("Extra cheese costs $1")
        bill+=1
    print(f"Your final bill is : ${bill}")
if size == 'L'.lower():
    bill = 25
    if add_pepperoni == 'Y'.lower():
        print("pepperoni costs $3")
        bill+=3
    if extra_cheese == 'Y'. lower():
        print("Extra cheese costs $1")
        bill+=1
    print(f"Your final bill is : ${bill}")