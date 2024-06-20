import random
from game_data import data

from art import vs
from art import logo
print(logo)

print("Welcome to the Higher Lower Game")


pick_1 = random.choice (data)
pick_2 = random.choice (data)
if pick_1 == pick_2:
    pick_1 =random.choice(data)
playing = True
score_tracker = 0
while playing:
    
    comparison_list = []
    pick_list = []
    pick_list = [pick_1,pick_2]
    comparison_list = [pick_1['follower_count'], pick_2['follower_count']]
    print(f"Compare A : {pick_1['name']}, {pick_1['description']}, from {pick_1['country']}")
    print(vs)
    print(f"Against B : {pick_2['name']}, {pick_2['description']}, from {pick_2['country']}")
    print(comparison_list)
    user_choice = input("Who has more followers? Type 'A' or 'B'\n").lower()
   
    if user_choice == "a":
        if comparison_list[0] > comparison_list [1]:
            score_tracker+=1
            print(f"Well done. Current Score: {score_tracker}")
            pick_1 = pick_2
        elif comparison_list[0]< comparison_list[1]:
            playing = False
            print(f"Sorry that is wrong. Final score: {score_tracker}")
    elif user_choice == "b":
        if comparison_list[1] > comparison_list [0]:
            score_tracker+=1
            print(f"Well done. Current Score: {score_tracker}")
            pick_1 = pick_2
        elif comparison_list[1]< comparison_list[0]:
            playing = False
            print(f"Sorry that is wrong. Final score: {score_tracker}")
    if playing:
        pick_2 = random.choice(data)
        while pick_2 ==pick_1:
            pick_2 = random.choice(data)