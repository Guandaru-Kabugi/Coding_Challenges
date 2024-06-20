import random
from game_data import data
#import ascii
from art import vs
from art import logo
print(logo)
#welcome the user
print("Welcome to the Higher Lower Game")
#create a comparison_list_of_followers
playing = True
score_tracker = 0
while playing:
    
    comparison_list = []
    pick_list = []
    #pick two random dictionaries
    for _ in range (2):
        pick = random.choice (data)
        comparison_list.append(pick['follower_count'])
        pick_list.append(pick)    
    print(comparison_list)
    print(f"Compare A : {pick_list[0]['name']}, {pick_list[0]['description']}, from {pick_list[0]['country']}")
    print(vs)
    print(f"Against B : {pick_list[1]['name']}, {pick_list[1]['description']}, from {pick_list[1]['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B'\n").lower()
   
    if user_choice == "a":
        if comparison_list[0] > comparison_list [1]:
            score_tracker+=1
            print(f"Well done. Current Score: {score_tracker}")
        elif comparison_list[0]< comparison_list[1]:
            playing = False
            print(f"Sorry that is wrong. Final score: {score_tracker}")
    elif user_choice == "b":
        if comparison_list[1] > comparison_list [0]:
            score_tracker+=1
            print(f"Well done. Current Score: {score_tracker}")
        elif comparison_list[1]< comparison_list[0]:
            playing = False
            print(f"Sorry that is wrong. Final score: {score_tracker}")

    