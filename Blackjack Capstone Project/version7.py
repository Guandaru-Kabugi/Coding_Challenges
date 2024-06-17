import random
import os
from art import logo

def deal_card ():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculator_score (cards):
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare (results, results_comp):
    if results >21 and results_comp>21:
        return "You went over. You lose 😤"
    if results == results_comp:
        return "Draw 🙃"
    elif results_comp == 0:
        return "You lose 😱. Computer won by BLACKJACK"
    elif results == 0:
        return "You win with a Blackjack 😎"
    elif results >21:
        return "You went over. You lose 😤"
    elif results_comp>21:
        return "Computer went over. You win 😁"
    elif results>results_comp:
        "You win 😃"
    else:
        return "You lose 😤"
def play_game():
    print(logo)
    My_cards = []
    computer_card = []
    
    for _ in range (2):
        My_cards.append(deal_card())
        computer_card.append(deal_card())
    continue_playing = True
    while continue_playing:
        results = calculator_score(My_cards)
        results_comp = calculator_score(computer_card)
        print(f"Your cards are: {My_cards}, current score: {results}") 
        print(f"Computer first hand: {computer_card[0]}")
        if results == 0 or results_comp == 0 or results > 21:
            continue_playing = False
        else:
           Another_card = input('Type "y" to get another card, type "n" to pass:\n')
           if Another_card == 'y':
               My_cards.append(deal_card()) 
           else:
               continue_playing = False
    while results_comp !=0 and results_comp<17:
        computer_card.append(deal_card())      
        results_comp = calculator_score(computer_card)
    print(f"Your final cards are: {My_cards}, final score: {results}")
    print(f"Computer final cards are: {computer_card}, final score: {results_comp}")
    print(compare(results, results_comp))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('cls')
  play_game()
      