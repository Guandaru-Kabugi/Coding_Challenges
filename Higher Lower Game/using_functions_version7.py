from art import logo
import random
from game_data import data
from art import vs
import os

print(logo)
print("Welcome to the game😁")
def get_random_card ():
    return random.choice(data)

def format_random_pick(pick):
    name = pick['name']
    description = pick['description']
    country = pick['country']
    return f"{name}, {description}, from {country}"
def evaluate_answer (guess, pick_1_followers,pick_2_followers):
    if pick_1_followers>pick_2_followers:
        return guess == 'a'
    else:
        return guess == 'b'
score = 0
pick_1 = get_random_card()
pick_2 = get_random_card()
if pick_1 ==pick_2:
    pick_2 = get_random_card()
playing = True
while playing:
    pick_1 = pick_2
    pick_2 = get_random_card()
    while pick_1 == pick_2:
        pick_2 = get_random_card()
    pick_1_followers = pick_1['follower_count']
    pick_2_followers = pick_2['follower_count']
    comparison_list = [pick_1['follower_count'],pick_2['follower_count']]

    print(format_random_pick(pick_1))
    print(vs)
    print(format_random_pick(pick_2))
    print(comparison_list)

    user_choice = input("Who has more followers? Type 'A' or 'B'\n").lower()
    answer_is_correct = evaluate_answer(user_choice,pick_1_followers,pick_2_followers)
    os.system('cls')
    print(logo)
    if answer_is_correct:
        score+=1
        print(f"Well done. your score: {score}")
    else:
        playing = False
        print(f"Sorry!, Wrong guess! your score: {score}")
            
    