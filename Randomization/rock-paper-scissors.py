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

choice_of_draw = int(input("Which option do you pick? 0 for rock, 1 for paper, and 2 for scissors "))
computer_choice_of_draw = random.randint(0,2)
#computer_choice_of_draw = 0
if choice_of_draw == 0 and computer_choice_of_draw == 0:
    print(choice_of_draw)
    print(rock)
    print ("computer chose: ")
    print(rock)
    print("It is a draw")
if choice_of_draw == 1 and computer_choice_of_draw == 1:
    print(choice_of_draw)
    print(paper)
    print ("computer chose: ")
    print(paper)
    print("It is a draw")
if choice_of_draw == 2 and computer_choice_of_draw == 2:
    print(choice_of_draw)
    print(scissors)
    print ("computer chose: ")
    print(scissors)
    print("It is a draw")
if choice_of_draw == 0 and computer_choice_of_draw == 1:
    print(choice_of_draw)
    print(rock)
    print ("computer chose: ")
    print(paper)
    print("You lose")
if choice_of_draw == 0 and computer_choice_of_draw == 2:
    print(choice_of_draw)
    print(rock)
    print ("computer chose: ")
    print(scissors)
    print("You win!")
if choice_of_draw == 1 and computer_choice_of_draw == 0:
    print(choice_of_draw)
    print(paper)
    print ("computer chose: ")
    print(rock)
    print("You lose")
if choice_of_draw == 1 and computer_choice_of_draw == 2:
    print(choice_of_draw)
    print(paper)
    print ("computer chose: ")
    print(scissors)
    print("You lose")
if choice_of_draw == 2 and computer_choice_of_draw == 0:
    print(choice_of_draw)
    print(scissors)
    print ("computer chose: ")
    print(rock)
    print("You lose")
if choice_of_draw == 2 and computer_choice_of_draw == 1:
    print(choice_of_draw)
    print(scissors)
    print ("computer chose: ")
    print(paper)
    print("You win")