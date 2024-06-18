#we are importing logo as first task
from art import logo
import random

print(logo)
#Welcoming Message
print("Welcome to the Number Guessing Game!")
#Tell them the guessing range
print("I'm thinking of a number between 1 and 100.")
#Generate a number and show it for now as part of testing code.
Guess_number = random.randint(1,100)
print(f"Pssst, the correct answer is {Guess_number}")
#Ask whether they want hard or easy
game_level = input("Which level do you want? Type 'easy' or 'hard'\n")
#Check number of guesses for hard
if game_level.lower() == 'hard':
    attempts= 5
    print(f"You have {attempts} remaining to guess the number.")
    guess = input("Make a guess: ")
    