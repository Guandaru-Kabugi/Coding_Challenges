import random
from art import logo


print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculator ():
    
    playing = input("Do you want to play a game of blackjack? Type 'y' for yes and 'n' for no\n")
    My_cards = []
    computer_card = []
    results = 0
    results_comp = 0
    if playing == 'y':
        for number in range (2):
            random_card = random.choice(cards)
            My_cards.append(random_card)
        for card in My_cards:
            results+=card
        print(f"Your current cards are {My_cards}, current score: {results}")
        for number in range (2):
            random_comp_cards = random.choice(cards)
            computer_card.append(random_comp_cards)
        for card in computer_card:
            results_comp+= card
        print(f"Computer first hand: {computer_card[0]}")
        if results == 21:
            print("You win by BLACKJACK")
            print(f"Your final cards are: {My_cards}, final score: {results}")
            print(f"Computer final cards are: {computer_card}, final score: {results_comp}")
            calculator()
        if results_comp ==21:
            print("Computer won by BLACKJACK")
            print(f"Your final cards are: {My_cards}, final score: {results}")
            print(f"Computer final cards are: {computer_card}, final score: {results_comp}")
            calculator()
        
    elif playing == 'n':
        calculator()
    continue_playing = True
    while continue_playing:
        
        Another_card = input('Type "y" to get another card, type "n" to pass:\n')
        if Another_card == "y":
            random_card = random.choice(cards)
            My_cards.append(random_card)
            results+=random_card
            print(f"Your cards are: {My_cards}, current score: {results}")
            random_comp_cards = random.choice(cards)
            computer_card.append(random_comp_cards)
            results_comp+=random_comp_cards
            if results>21 and results_comp<=21:
                continue_playing = False
                print(f"Your final cards are: {My_cards}, final score: {results}")
                print(f"Computer final cards are: {computer_card}, final score: {results_comp}")
                print("Computer wins")
                calculator()
            elif results ==21:
                print("You win by a blackjack")
                print(f"Your final cards are: {My_cards}, final score: {results}")
                print(f"Computer final cards are: {computer_card}, final score: {results_comp}")
                calculator()
            elif results_comp == 21:
                print("Computer wins by a blackjack")
                print(f"Your final cards are: {My_cards}, final score: {results}")
                print(f"Computer final cards are: {computer_card}, final score: {results_comp}")
                calculator()
            elif results<=21 and results_comp>21:
                print("You win")
                continue_playing = False
                print(f"Your final cards are: {My_cards}, final score: {results}")
                print(f"Computer final cards are: {computer_card}, final score: {results_comp}")
                calculator()
            elif results >21 and results_comp>21:
                continue_playing = False
                print("Game over. You both went above 21")
                print(f"Your final cards are: {My_cards}, final score: {results}")
                print(f"Computer final cards are: {computer_card}, final score: {results_comp}")
                calculator()
        elif Another_card == "n":
            continue_playing = False
            random_comp_cards = random.choice(cards)
            computer_card.append(random_comp_cards)
            results_comp+=random_comp_cards
            
            if results<=21 and results>results_comp:
                print("You win")
            elif results <21 and results<results_comp and results_comp<=21:
                print("Computer wins")
            elif results> 21:
                print("Game over. You went beyond the required score")
            elif results_comp> 21:
                print("Computer went over. You win")
            elif results == 21:
                print("You win by Blackjack")
            elif results_comp == 21:
                print("Computer wins by Blackjack")
            else:
                print("IT IS A DRAW")
            print(f"Your final cards are: {My_cards}, final score: {results}")
            print(f"Computer final cards are: {computer_card}, final score: {results_comp}")
            calculator()
calculator()