import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
# Rock beats scissors by crushing them.
# Scissors beat paper by cutting the paper in two.
# Paper beats rock by covering the rock.
game_images = [rock, paper, scissors]
choice_of_draw = int(input("Which option do you pick? 0 for rock, 1 for paper, and 2 for scissors \n"))
computer_choice_of_draw = random.randint(0,2)
#computer_choice_of_draw = 0
if choice_of_draw>2 or choice_of_draw<0:
    print("Invalid selection!")
    exit()
else:
    print(choice_of_draw)
    print(game_images[choice_of_draw])
    print(f"Computer chose: {game_images[computer_choice_of_draw]}")
    if choice_of_draw == computer_choice_of_draw:
        print("It is a draw")
    elif computer_choice_of_draw == 0 and choice_of_draw == 2:
        print("You lose")
    elif choice_of_draw ==0 and computer_choice_of_draw == 2:
        print("you win!")
    elif choice_of_draw> computer_choice_of_draw:
        print("You win!")
    else:
        print("You lose")