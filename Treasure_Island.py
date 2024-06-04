print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island. Your mission is to find the treasure.")
Direction = input ("Do you want to go left or right? ")
if not Direction == "left".lower():
    print("Oops! You have fallen into a hole! Game over!")
    exit()
else:
    Swim_wait = input("Do you want to swim across or wait? swim or wait ")
    if not Swim_wait== "wait".lower():
        print("Wooah! You have been Attacked by a trout. You are dead. Game Over.")
        exit()
    else:
        Door = input("Which door do you want to open? Red or Blue or Yellow ")
        if Door == "Yellow".lower():
            print("Congratulations! You win")
        elif Door== "Red".lower():
            print("Oh no! you have been burned. You are dead. Game over")
        elif Door == "Blue".lower():
            print("Oh no! You have been eated by beasts. You are dead")
        else:
            print("Game over!!!")