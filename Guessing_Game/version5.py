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
#print(f"Pssst, the correct answer is {Guess_number}")
#Ask whether they want hard or easy
game_level = input("Which level do you want? Type 'easy' or 'hard'\n")
#Check number of guesses for hard

def check_guess_continuation (game_level):
    if game_level.lower() == 'hard':
        attempts= 5
        print(f"You have {attempts} remaining to guess the number.")
    elif game_level.lower() == 'easy':
        attempts = 10
        print(f"You have {attempts} remaining to guess the number.")
    Guessed_number = False
    while not Guessed_number:
        guess = int(input("Make a guess: "))
        attempts-=1
        if attempts==0:
            if guess < Guess_number:
                Guessed_number = True
                print("Too low.\nOops! You have run out of guesses 😤.")
            elif guess>Guess_number:
                Guessed_number = True
                print("Too high.\nOops! You have run out of guesses 😤.")
        else:
            if guess < Guess_number:
                print("Too low.\nGuess again 🙃.")
            elif guess> Guess_number:
                print("Too high.\nGuess again 🙃.")
            elif guess == Guess_number:
                Guessed_number = True
                print("Well done.\nYou made a correct guess 😁.")
check_guess_continuation(game_level)          
    