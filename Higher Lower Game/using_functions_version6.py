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
score = 0
pick_1 = get_random_card()
pick_2 = get_random_card()
if pick_1 ==pick_2:
    pick_2 = get_random_card()
playing = True
while playing:
    comparison_list = [pick_1['follower_count'],pick_2['follower_count']]

    print(format_random_pick(pick_1))
    print(vs)
    print(format_random_pick(pick_2))
    print(comparison_list)

    user_choice = input("Who has more followers? Type 'A' or 'B'\n").lower()
    if user_choice == 'a':
        if comparison_list[0] > comparison_list[1]:
            score+=1
            print(f"Well done. your score: {score}")
            pick_1 = pick_2
    
        elif comparison_list[1] > comparison_list[0]:
            playing = False
            print(f"Sorry!, Wrong guess! your score: {score}")
    elif user_choice == 'b':
        if comparison_list[1] > comparison_list[0]:
            score+=1
            print(f"Well done. your score: {score}")
            pick_1 = pick_2
        elif comparison_list[1] < comparison_list[0]:
            playing = False
            print(f"Sorry!, Wrong guess! your score: {score}")
    
    if playing:
        pick_2 = get_random_card()
        while pick_2 ==pick_1:
            pick_2 = get_random_card()
            
    